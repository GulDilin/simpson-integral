from math import sin, log


class Integral:
    def __init__(self, func, e, left, right):
        self.func = func
        self.e = e
        self.left = left
        self.right = right

    def calculate(self):
        n = 2
        e = None
        old_res = None
        res = None

        while e is None or e > self.e:
            h = abs(self.right - self.left) / n / 2
            res = self.func(self.left) + 4 * sum([self.func(self.left + h * (2 * i - 1)) for i in range(1, n + 1)])
            res += 2 * sum([self.func(self.left + h * (2 * i)) for i in range(1, n)]) + self.func(self.right)
            res *= h / 3
            e = abs(res - old_res) / 15 if old_res else None
            old_res = res if not old_res else old_res
            n *= 2
        return res


if __name__ == '__main__':

    funcs = {"5/x": lambda x: 5 / x, "sin(x)": lambda x: sin(x), "ln(x)": lambda x: log(x)}
    for name in funcs.keys():
        integral = Integral(funcs[name], 0.001, 0, 1)
        print(f'{name} from {integral.left} to {integral.right} = {integral.calculate()}')
