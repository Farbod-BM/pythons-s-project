def f(x):
    return x ** 3 - x ** 2 + 2

def df(x):
    return 3 * x ** 2 - 2 * x

def nr(x):
    p = f(x) / df(x)
    while abs(p) >= 0.000000001:
        p = f(x) / df(x)
        x = x - p
    print(x)

x0 = 10
nr(x0)