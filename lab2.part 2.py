from math import factorial

a = 0.2
b = 1.5
h = 0.02
d = 0.001

def term(x, d):
    n = 1
    sum = 0
    elem = x

    while abs(elem) > d:
        sum += elem
        n += 1
        elem =(x - 1) ** (2*n + 1) / factorial(n)

    return sum

#Табуляція 
def tab_term(a, b, h, d):
    res = []
    x = round(a, 2)

    while x <= b:
        y = term(x, d)
        res.append((x, y))
        x = round(x + h, 3)

    return res

res = tab_term(a, b, h, d)

#Вивід результатів
for x, y in res:
    print(f"x = {x: .2f}, f(x) = {y: .3f}")
