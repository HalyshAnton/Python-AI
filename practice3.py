class CPU:
    def __init__(self, num_kernel):
        print('init from CPU')
        self.num_kernel = num_kernel


class GPU:
    def __init__(self, memmory):
        print('init from GPU')
        self.memmory = memmory


class RAM:
    def __init__(self, capacity):
        print('init from RAM')
        self.capacity = capacity


class Motherboard:
    def __init__(self, type_socket):
        print('init from Motherboard')
        self.type_socket = type_socket


class Computer(CPU, GPU, RAM, Motherboard):
    def __init__(self, num_kernel, memmory, capacity, type_socket):
        print(f'init from {type(self).__name__}')
        super().__init__(num_kernel)
        GPU.__init__(self, memmory)
        RAM.__init__(self, capacity)
        Motherboard.__init__(self, type_socket)


obj = Computer(1, 200, 30, 'type')
