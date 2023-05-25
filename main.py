def xd1():

    flavors = ["Ваниль", "Шоколад", "Клубника", "Миндаль"]
    class IceCreamStand:
        def __init__(self, name, cuisine_type):
            self.flavors = flavors
            self.name = name
            self.cuisine_type = cuisine_type

        def info(self):
            print(f"{self.name} - {self.cuisine_type}")

        def list_flavors(self):
            print("Доступные вкусы:")
            for flavor in self.flavors:
                print("- " + flavor)

    ice_cream = IceCreamStand("Лизун", "Кафе мороженое")
    ice_cream.info()
    ice_cream.list_flavors()

def xd2():
    flavors = ["Ваниль", "Шоколад", "Клубника", "Миндаль"]
    class IceCreamStand:
        def __init__(self, name, cuisine_type, location, time):
            self.flavors = flavors
            self.name = name
            self.cuisine_type = cuisine_type
            self.location = location
            self.time = time

        def info_name(self):
            print(f"{self.name} - {self.cuisine_type}")

        def info_location(self):
            print(f"Находится по адресу: {self.location}")

        def info_time(self):
            print(f"Время работы: {self.time}")

        def add_flavor(self,):
            quantity1 = input("Сколько новых вкусов вы бы хотели увидеть в меню? ")
            while int(quantity1) > 0:
                new = input("Какие именно вкусы? ")
                flavors.append(new)
                quantity1 = int(quantity1) - 1

        def del_flover(self,):
            quantity2 = input("Сколько вкусов в текущем меню вы бы хотели убрать? ")
            while int(quantity2) > 0:
                flavors.remove(input("Какие именно вкусы? "))
                quantity2 = int(quantity2) - 1

        def check_flavor(self):
            availability = (input("Какого вкуса мороженое проверить на наличие? "))
            if availability in flavors:
                print("Этот вкус в наличии")
            else:
                print("К сожалению этого вкуса сейчас нет")

        def list_flavors(self):
            print("Доступные вкусы:")
            for flavor in self.flavors:
                print("- " + flavor)

        def stick(self):
            stick_choice = input("Вы хотите мороженное на палочке?")
            if stick_choice == 'да':
                print('На палочке, так на палочке')

        def soft(self):
            soft_choice = input("Может тогда мягкое мороженное?")
            if soft_choice == 'да':
                print('Любитель мягкого значит')
            else:
                print('Покиньте помещение, если ничего не нравится')



    ice_cream = IceCreamStand("Лизун", "Кафе мороженое", "Санкт-Петербург, Улица Пушкина, Дом 28", "Пн-Пт с 8 до 22 / Сб-Вс с 10 до 18")
    ice_cream.info_name()
    ice_cream.info_location()
    ice_cream.info_time()
    ice_cream.add_flavor()
    ice_cream.del_flover()
    ice_cream.check_flavor()
    ice_cream.list_flavors()
    ice_cream.stick()
    ice_cream.soft()

def xd3():

    import tkinter as tk

    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = flavors

            self.root = tk.Tk()
            self.root.title("Ice Cream Stand")

            self.flavors_label = tk.Label(self.root, text="Вкусы которые у нас есть")
            self.flavors_label.pack()

            for flavor in self.flavors:
                flavor_label = tk.Label(self.root, text="- " + flavor)
                flavor_label.pack()

            self.root.mainloop()

    flavor = IceCreamStand(["Ваниль", "Шоколад", "Клубника", "Миндаль"])

xd3()
