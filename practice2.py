class UIElement:
    def __init__(self, functionality):
        self.functionality = functionality

    def display(self):
        print('display UIElement')


class InteractiveElement:
    def __init__(self, a, b):
        pass

    def click(self):
        print('click, click')


class Button(UIElement, InteractiveElement):
    def __init__(self, functionality, label):
        super().__init__(functionality)
        self.label = label

    def display(self):
        print('display button')


class Menu(UIElement, InteractiveElement):
    def __init__(self, functionality, info):
        super().__init__(functionality)
        self.info = info

    def display(self):
        print('display Menu')


class FieldInput(UIElement, InteractiveElement):
    def __init__(self, functionality, text):
        super().__init__(functionality)
        self.text = text

    def display(self):
        print('display Field')


button = Button('', 'Open')
menu = Menu('', 'very useful program')
field = FieldInput('', 'Your login')

button.display()
menu.display()
field.display()

button.click()
menu.click()
field.click()
