# Створіть клас "Квартира", який має зберігати інформацію про кількість кімнат та площу.
# Застосуйте інкапсуляцію для забезпечення тільки читання цих даних


class Apartment:
    def __init__(self, num_rooms, area):
        self.__num_rooms = num_rooms
        self.__area = area

    def get_num_rooms(self):
        return self.__num_rooms

    def get_area(self):
        return self.__area


apartment = Apartment(4, 45)
print(f'{apartment.get_num_rooms()=}')
print(f'{apartment.get_area()=}')

# Розробіть систему для організації подій та завдань.
# Кожна подія має мати назву, дату та опис.
# Реалізуйте методи для додавання нових подій, зміни дати та опису.
# Використайте інкапсуляцію для захисту дати від неправильних змін.


class Event:
    count = 0

    def __init__(self, name=None, date=None, desc=None):
        self.__name = name
        self.__date = date
        self.__desc = desc
        Event.count += 1

    def set_date(self, new_date):
        self.__date = new_date

    def set_desc(self, new_desc):
        self.__desc = new_desc

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_desc(self):
        return self.__desc

    def __del__(self):
        Event.count -= 1
        del self


event1 = Event()
event2 = Event()
event3 = Event()

print(Event.count, event1.count)

del event3
print(Event.count, event1.count)