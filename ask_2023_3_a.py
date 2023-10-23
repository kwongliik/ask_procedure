def f(x = 2, y = 3):
    x = x + y
    y = y * 4 - x
    print(x, y)

f()
f(3, 4)