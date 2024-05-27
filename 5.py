def num1():
    s = [1, 2, 3, 4, 5]
    a= int(input("Введите число "))
    if h in s:
        print("Ваше число есть в списке", s, a)
    else:
        print("Вашего числа нет в списке")

def num2():
    s = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 3]
    a = set()
    b = set()
    for i in s:
        if i in b:
            a.add(i)
        else:
            b.add(i)
    if a:
        print("Элементы,повторяющиеся в списке")
        for i in a:
            print(i)
    else:
        print("В списке нет повторяющиихся элементов ")

def num3()

    settimana = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

    a = int(input("Сколько вы хотите выходных? - "))
    settimana1 = settimana[-a:]
    settimana2 = settimana[:-a]
    print("Ваши выходные дни: ", ', '.join(settimana1))
    print("Ваши рабочие дни:", ', '.join(settimana2))

num1()
num2()
num3()





