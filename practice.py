class Animal:
    def sound(self):
        print("Some sound: hrrr")

    def make_noise(self):
        self.sound()
        self.sound()
        self.sound()


class Dog(Animal):
    def run(self):
        print('dog is running')

    def sound(self):
        print("Hav, hav")


class Cat(Animal):
    def sound(self):
        super().sound()
        print("Miau")

    def get_super(self):
        print(super())


# obj = Dog()
# print(obj.sound())
# print()
# obj.make_noise()

#cat = Cat()
#cat.sound()

class Figure:
    def __init__(self, area):
        self._area = area
        print('init from Figure')


class Circle(Figure):
    def __init__(self, area, radius):
        super().__init__(area)
        self._radius = radius

        print('init from Circle')

    def print_info(self):
        print(f'{self._area=}')
        print(f'{self._radius=}')


obj = Circle(20, 3)
obj.print_info()