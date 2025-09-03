#Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій.
# class Car:
#     def __init__(self,name,year,manufacturer,engine_displacement,color,price):
#         self.name = name
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_displacement = engine_displacement
#         self.color = color
#         self.price = price
#
#     def get_price(self):
#         return self.price
#     def get_color(self):
#         return self.color
#     def get_engine_displacement(self):
#         return self.engine_displacement
#     def get_manufacturer(self):
#         return self.manufacturer
#     def get_year(self):
#         return self.year
#     def get_name(self):
#         return self.name
#
#     def set_price(self,price):
#          self.price = price
#          return self
#     def set_color(self,color):
#          self.color = color
#          return self
#     def set_engine_displacement(self,engine_displacement):
#          self.engine_displacement = engine_displacement
#          return self
#     def set_manufacturer(self,manufacturer):
#          self.manufacturer = manufacturer
#          return self
#     def set_year(self,year):
#          self.year = year
#          return self
#     def set_name(self,name):
#          self.name = name
#          return self
#
# new_car = Car("bmw","1999","bmw company","5.0","svart","111111")

# Завдання 2
# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Book:
    def __init__(self, name, year, manufacturer, type, author, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.type = type
        self.author = author
        self.price = price

    def get_price(self):
        return self.price

    def get_author(self):
        return self.author

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def get_year(self):
        return self.year

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price
        return self

    def set_author(self, author):
        self.author = author
        return self

    def set_type(self, type):
        self.type = type
        return self

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_name(self, name):
        self.name = name
        return self


new_book = Book("drabina", "1999", "drabina company", "horror" , "Vasia")

# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Stadium:
    def __init__(self, name, year, land, city, kapasitet, price):
        self.name = name
        self.year = year
        self.land = land
        self.city = city
        self.kapasitet = kapasitet

    def get_kapasitet(self):
        return self.kapasitet

    def get_city(self):
        return self.city

    def get_land(self):
        return self.land

    def get_year(self):
        return self.year

    def get_name(self):
        return self.name

    def set_kapasitet(self, kapasitet):
        self.kapasitet = kapasitet
        return self

    def set_city(self, city):
        self.city = city
        return self

    def set_land(self, land):
        self.land = land
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_name(self, name):
        self.name = name
        return self


new_stadium = Stadium("Old trafford", "1889", "England", "Manchester" , "111111")