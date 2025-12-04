f1 = lambda lst: list(filter(lambda x: x % 3 == 0 and x > 5, lst))

f2 = lambda lst: list(filter(lambda x: x == x[::-1], lst))

f3 = lambda lst: list(filter(lambda x: lst.index(x) % 2 == 1, lst))

f4 = lambda lst: list(filter(lambda x: x[0].isupper(), lst))

f5 = lambda lst: list(filter(lambda x: x > 0 and x % 2 != 0, lst))

f6 = lambda lst, n: list(filter(lambda x: len(x) >= n, lst))
