class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def write(self):
        print(f'{self.name} {self.lastname}, {self.age}')


class Worker(Person):
    def __init__(self, name, lastname, age,  hire_date):
        super().__init__(name, lastname, age)
        self.hire_date = hire_date
        self.position = "none"

    def write(self):
        print(f'{self.name} {self.lastname}, {self.age}, Hired since {self.hire_date} as {self.position}')


class Driver(Worker):
    def __init__(self, name, lastname, age, hire_date, category):
        super().__init__(name, lastname, age, hire_date)
        self.position = "Driver"
        self.category = category

    def write(self):
        super().write()
        self.__info()

    def __info(self):
        print(f"Category {self.category}")


class Keeper(Worker):
    def __init__(self, name, lastname, age, hire_date):
        super().__init__(name, lastname, age, hire_date)
        self.position = "Keeper"


person1 = Person("Patryk", "Ledzion", 22)
person1.write()

worker1 = Worker("Jan", "Kowalski", 31, 2021)
worker1.write()

driver = Driver("Jan", "Nowak", 54, 2019, "C")
driver.write()

keeper = Keeper("Wojciech", "Szczesny", 30, 2017)
keeper.write()
