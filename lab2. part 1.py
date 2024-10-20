from math import sin, cos, e, log as ln

# Встановлюємо параметри
a = 5
b = 8
h = 0.2

# Табулювання функції
x = a
while x <= b:
     while x < 6:
        print (round(x,3) , "-", round((1 / (1 - ln(x + 1))), 3))
        x += h
     while 6 <= x < 7:
        print (round(x, 3) , "-", round(sin(cos(x)), 3))
        x += h
     while x <= 8:
        print (round(x, 3) , "-", round(ln(e*x+x*2), 3))
        x += h
        x = round(x ,2)
        