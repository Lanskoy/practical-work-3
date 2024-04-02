print("Введите три переменные.")

x = float(input())
y = float(input())
z = float(input())

drob = (x + 2 * y + 3 * z) / min(x+y,y+z,)
u = 2 + max(drob,x / z)
print(u)