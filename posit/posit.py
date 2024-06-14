import math

class Posit:
    def __init__(self, value, total_bits=16, exponent_bits=1):
        self.total_bits = total_bits
        self.exponent_bits = exponent_bits
        self.sign = 0
        self.k = 0
        self.exponent = 0
        self.fraction = 0
        self.is_zero = False
        self.is_nan = False
        self.update_by_value(value)

    def update_by_value(self, value):
        self.is_zero = False
        self.is_nan = False

        if value == 0:
            self.sign = 0
            self.k = 0
            self.exponent = 0
            self.fraction = 0
            self.is_zero = True
            return

        if math.isnan(value):
            self.sign = 1
            self.k = 0
            self.exponent = 0
            self.fraction = 0
            self.is_nan = True
            return

        self.sign = 0 if value >= 0 else 1
        if self.sign == 1:
            value *= -1

        scale = 2 ** (2 ** self.exponent_bits)
        self.k = 0
        while value > scale:
            self.k += 1
            value /= scale
        while value < 1:
            self.k -= 1
            value *= scale

        self.exponent = 0
        while value >= 2:
            self.exponent += 1
            value /= 2

        self.fraction = (value - 1) * scale

    def calculate_float_value(self):
        if self.is_zero:
            return 0.0
        if self.is_nan:
            return float('nan')

        scale = 2 ** (2 ** self.exponent_bits)
        decoded_number = scale ** self.k * 2 ** self.exponent * (1.0 + self.fraction / scale)
        if self.sign == 1:
            decoded_number *= -1

        return decoded_number

    def __add__(self, other):
        result = Posit(0, self.total_bits, self.exponent_bits)
        result.update_by_value(self.calculate_float_value() + other.calculate_float_value())
        return result

    def __sub__(self, other):
        result = Posit(0, self.total_bits, self.exponent_bits)
        result.update_by_value(self.calculate_float_value() - other.calculate_float_value())
        return result

    def __mul__(self, other):
        result = Posit(0, self.total_bits, self.exponent_bits)
        result.update_by_value(self.calculate_float_value() * other.calculate_float_value())
        return result

    def __truediv__(self, other):
        result = Posit(0, self.total_bits, self.exponent_bits)
        result.update_by_value(self.calculate_float_value() / other.calculate_float_value())
        return result

    def __str__(self):
        return f"Posit value: {self.calculate_float_value()}"
