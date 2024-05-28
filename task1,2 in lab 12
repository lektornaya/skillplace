def numeros1():

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

        

    class IceCreamStand(Restaurant):
        def __init__(self, flavors):
            self.flavors = flavors

        def describe_flavors(self):
            for i in self.flavors:
                print(i)

    icecream = IceCreamStand(['ваниль', 'трюфель','манго','персик','шоколад','черная смородина','крем-брюле','соле','фрагола','карамель'])
    icecream.describe_flavors()

def numeros2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f'Ресторан {self.restaurant_name}:  {self.cuisine_type} кухня')

        def open_restaurant(self):
            print(f'Ресторан {self.restaurant_name} открыт')

        def newRating(self, new_rating):
            self.rating = new_rating
            print(f'Рейтинг ресторана: {self.rating} звёзд')

    class IceCreamStand(Restaurant):
        
        def add_flavors(self):
            self.flavors.append(input('Введите вкус, который хотите добавить: '))
        
        def describe_flavors1(self):
            for i in self.flavors:
                print(i)
                
        def delete_flavors(self):
            self.flavors.remove(input('Введите вкус, который хотите удалить: '))                

        def check_flavors(self):
            G = input('Введите вкус, который хотите проверить в наличии: ')
            if G in self.flavors:
                print(f'Il gusto "{G}" есть в меню')
            else:
                print(f'Il gusto "{G}" нет в меню')
        
        def __init__(self, flavors, location, worktime):
            self.flavors = flavors
            self.location = location
            self.worktime = worktime
            

    icecream = IceCreamStand(['ваниль', 'трюфель','манго','персик','шоколад','черная смородина','крем-брюле','соле','фрагола','карамель'], 'Адрес: наб. реки Фонтанки, 30', 'Режим работы: 12:00-23:00')
    icecream.add_flavors()
    icecream.delete_flavors()
    icecream.check_flavors()
    print('Меню, с учетом редакции сортов мороженного:')
    icecream.describe_flavors1()


numeros1()
numeros2()
