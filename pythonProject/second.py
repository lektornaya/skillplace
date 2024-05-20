
def f(num):

while True:
    try:
        num = int(input("Введите число: "))
    except ValueError:
        continue
    break
if 