from decimal import Decimal


class Calc:

    def add(self, a, b):
        return float(Decimal(str(a)) + Decimal(str(b)))

    def div(self, a, b):
        return a / b

