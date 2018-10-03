from main_controller import *


class Blockbuster():
    """return an iterable with n P1P2P3 objects where n is the number of P1P2P3 asked (**kwarg) on given y"""

    def __init__(self, y_start, y_stop):
        self.y_range = range(y_stop, y_start - 1, -1)
        self.y_range_inv = range(y_start, y_stop + 1)
        self.p_data = list()

    def __call__(self, y):
        for p in self.p_data:
            yield P1P2P3(p[0], p[1], p[2], y)

    def add(self, p1, p2, p3):
        self.p_data.append([p1, p2, p3])

    def y_vertex(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def offset(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def delta(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def c_g(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def a(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def b(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value

    def c(self):
        for p in self.p_data:
            value = (P1P2P3(p[0], p[1], p[2], 0))
            yield value
