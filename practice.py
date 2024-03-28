# Багаторівневе успадкування
class GrandParent:
    def go(self):
        print('I go')

    def method(self):
        print('GrandParent method')


class Parent(GrandParent):
    def walk(self):
        print('I walk')

    def go(self):
        print('Parent go')

    def method(self):
        print('Parent method')


class Child(Parent):
    def method(self):
        print('Child method')


# child = Child()
# child.go()
# child.walk()
# child.method()


# Множинне успадкування
class ClassA:
    def methodA(self):
        print('hello from A')

    def method(self):
        print('method from A')


class ClassB:
    def methodB(self):
        print('hello from B')

    def method(self):
        print('method from B')


class ClassC(ClassA, ClassB):
    def methodA(self):
        print('modified methodA')

    def get_super(self):
        print(super().methodA())


obj = ClassC()
# obj.methodA()
# obj.methodB()
# obj.method()

# print(Child.__mro__)
#
# print(Child.mro())
# child = Child()
# child.method()

# import time
# print(type(time).__mro__)
#
#
# def func():
#     return 1
#
# print(type(func))
#
# func.attr = 3
# print(func.attr)

#print(ClassC.mro())
print(obj.get_super())
