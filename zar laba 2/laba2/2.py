mesto = int(input("Введите номер маста "))
s = "верхнее" if mesto // 2 % 2 == 0 else "нижнее"
z = "боковое" if mesto // 4 % 2 == 0 else "купе"
print(s)
print(z)
