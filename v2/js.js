a, b, c = self.a, self.b, self.c
        f = self.offset
        _a0 = a
        _b0 = b + 2 * (a * f)
        _c0 = c + a * (f ** 2) + (b * f)
        self.a0 = abs(_a0)
        self.b0 = -abs(_b0)
        if _a0 <= 0:
            self.c0 = -(_c0)
        else:
            self.c0 = _c0