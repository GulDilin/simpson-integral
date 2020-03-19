from math import sin, log


class Integral:
    def __init__(self, func, e, left, right):
        self.func = func
        self.e = e
        self.left = left if left < right else right
        self.right = right if left < right else left

    def calculate(self):
        n = 2
        e = None
        old_res = None
        res = None

        while (e is None or e > self.e) and n <= 524288:
            h = abs(self.right - self.left) / n / 2

            f = [None for _ in range(n * 2 + 1)]
            for i in range(n * 2 + 1):
                try:
                    f[i] = self.func(self.left + h * i)
                except Exception:
                    f[i] = 0

            res = f[0] + 4 * sum([f[2 * i - 1] for i in range(1, n + 1)])
            res += 2 * sum([f[2 * i] for i in range(1, n)]) + f[2 * n]
            res *= h / 3
            e = abs(res - old_res) / 15 if old_res is not None else None
            old_res = res if old_res is None else old_res
            n *= 2
        return res


if __name__ == '__main__':
    funcs = {"5/x": lambda x: 5 / x, "sin(x)": lambda x: sin(x), "ln(x)": lambda x: log(x)}
    print("Choose function:")
    func_names = list(funcs.keys())
    for i in range(len(func_names)):
        print(f'\t{i}. {func_names[i]}')

    chosen = None
    left = None
    original_left = None
    right = None
    original_right = None
    limit = None
    koef = 1

    while True:
        try:
            chosen = int(input('Type a number of function: ').strip())
        except ValueError:
            continue
        if chosen >= (len(funcs.keys())) or chosen < 0:
            print("Incorrect number")
            continue
        break

    name = func_names[chosen]

    while True:
        left_right = input('Type left right limits: ').strip().split(" ")
        if len(left_right) != 2:
            print('Incorrect limits format')
            continue
        try:
            left, right = float(left_right[0]), float(left_right[1])
            original_left, original_right = left, right
            if left > right:
                left, right = right, left
                koef = -1
            if 'ln' in name and left <= 0:
                print('You cant use that limits. Arg must be > 0.')
            if '/x' in name:
                if left == 0 or right == 0:
                    print('You cant use zero limits.')
                    continue
                else:
                    if left < 0 and right > 0:
                        dif = abs(abs(right) - abs(left))
                        if abs(left) < abs(right):
                            left = right - dif
                        else:
                            right = left + dif

        except ValueError:
            print("Incorrect values")
            continue
        break

    while True:
        try:
            limit = float(input('Type error limit: '))
        except ValueError:
            print("Incorrect values")
            continue
        break

    integral = Integral(funcs[name], limit, left, right)
    print(f'\nIntegral {func_names[chosen]} from {original_left} to {original_right} = {koef * integral.calculate()}')
