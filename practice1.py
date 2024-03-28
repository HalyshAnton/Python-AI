class GrandParent:
    def __init__(self, history):
        self.history = history


class Parent(GrandParent):
    def __init__(self, history, family_info):
        super().__init__(history)
        self.family_info = family_info


class Child(Parent):
    def __init__(self, history, family_info, dreams):
        super().__init__(history, family_info)
        self.dreams = dreams

    def get_info(self):
        print(self.history)
        print(self.family_info)
        print(self.dreams)


# child = Child('history', 'family', 'dreams')
# child.get_info()

# Множинне успадкування
class ClassA:
    def __init__(self, a):
        self.a = a


class ClassB:
    def __init__(self, b):
        self.b = b


class ClassC(ClassA, ClassB):
    def __init__(self, a, b, c):
        super().__init__(a)
        ClassB.__init__(self, b)
        self.c = c

    def get_info(self):
        print(self.a)
        print(self.b)
        print(self.c)


obj = ClassC(1, 2, 3)
obj.get_info()