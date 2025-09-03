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