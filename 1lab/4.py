color1 = input("введите цвет (красный,синий,желтый) :")
color2 = input("введите цвет (красный,синий,желтый) :")
if (color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный'):
    print("фиолетовый")
    if (color1 == 'желтый' and color2 == 'синий') or (color1 == 'синий' and color2 == 'желтый'):
        print("зеленый")
        if (color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный'):
            print("оранжевый")
