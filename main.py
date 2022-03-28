import math

a = 1
b = 4
c = 3.5
d = b ** 2 - 4 * a * c
print("Дискриминант D =  %.2f"  % d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
