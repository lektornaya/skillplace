a = input("Введите год ")
if a // % 4 == 0 and a % 100 != 0 and (a % 400 == 0):
    print("весокосный")
else:
    print("Этот год не весокосный")
