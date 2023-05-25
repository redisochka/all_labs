def xd1():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на {self.cuisine_type} кухне")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    newRestaurant = Restaurant("Клод Моне", "Итальянская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def xd2():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Клод Моне", "Итальянская")
    restaurant2 = Restaurant("Хачачурка", "Кавказская")
    restaurant3 = Restaurant("Харакири", "Японская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def xd3():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} специализируется на кухне {self.cuisine_type},\nИзначальный рейтинг ресторана {self.restaurant_name}: {self.rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

    newRestaurant = Restaurant("Клод Моне", "Итальянская", 4.8)
    newRestaurant.describe_restaurant()
    newRestaurant.update_rating(5)

xd1()
xd2()
xd3()