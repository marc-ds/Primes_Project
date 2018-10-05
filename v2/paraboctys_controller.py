from main_controller import *


class Paraboctys():
    """return an iterable with a line in a given range"""

    def __init__(self, p1, p2, p3, p1_step=0, p2_step=0, p3_step=1, init=-20, end=20):
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.init = int(init)
        self.end = int(end)
        self.p1_step = int(p1_step)
        self.p2_step = int(p2_step)
        self.p3_step = int(p3_step)
        self.p_range = range(self.init, self.end + 1)

    def __call__(self, y):
        for i in self.p_range:
            p1 = self.p1 + (self.p1_step * i)
            p2 = self.p2 + self.p2_step * i
            p3 = self.p3 + (self.p3_step * i)
            yield XPn(p1, p2, p3, y)
