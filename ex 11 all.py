def res():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating = 0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
        def describe_restauranto(self):
            print(f"Ресторан {self.restaurant_name} открыт!")
        def describe_restauro(self, new_rating):
            if 0 <= new_rating <= 5:
                self.rating = new_rating
                print("Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")
            else:
                print("Рейтинг должен быть в диапазоне от 0 до 5")

    rest1 = Restaurant('King Pong', 'Паназиаткая', 4.6)
    rest2 = Restaurant('Чеховъ', 'Русская', 4.7)
    rest3 = Restaurant('Medici Italian bistro', 'Итальянская', 4.9)
    rest1.describe_restaurant()
    rest1.describe_restauranto()
    print()
    rest2.describe_restaurant()
    rest2.describe_restauranto()
    print()
    rest3.describe_restaurant()
    rest3.describe_restauranto()
    print()
    rest1.describe_restauro(5.0)
    rest1.describe_restaurant()
res()

