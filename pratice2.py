class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity


# TODO
class CD(Product):
    def __init__(self, name, price, quantity, singer, num_songs):
        super().__init__(name, price, quantity)
        self._singer = singer
        self._num_songs = num_songs

    def get_singer(self):
        return self._singer

    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_num_songs(self):
        return self._num_songs

    def set_num_songs(self, new_num_songs):
        self._num_songs = new_num_songs


# TODO
class MusicalInstrument(Product):
    def __init__(self, name, price, quantity, instrument_type, material):
        super().__init__(name, price, quantity)
        self._type = instrument_type
        self._material = material


cd = CD('CD_name', 200, 1, "Elsa`s Ocean", 10)
print(cd.get_singer())

