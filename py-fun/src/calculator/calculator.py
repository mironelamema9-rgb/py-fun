class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Calculator(metaclass=SingletonMeta):
    ENGLISH_NUMBERS = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10
    }

    SPANISH_NUMBERS = {
        "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
        "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
        "diez": 10
    }

    RUSSIAN_NUMBERS = {
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
        "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
        "десять": 10
    }

    CHINESE_NUMBERS = {
        "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
        "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10
    }

    ROMAN_NUMERAL_MAP = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    def add(self, a, b):
        return self.parse_input(a) + self.parse_input(b)

    def sub(self, a, b):
        return self.parse_input(a) - self.parse_input(b)

    def mul(self, a, b):
        return self.parse_input(a) * self.parse_input(b)

    def div(self, a, b):
        b_num = self.parse_input(b)
        if b_num == 0:
            raise ValueError("Cannot divide by zero")
        return self.parse_input(a) / b_num

    def factorize(self, n):
        n_num = self.parse_input(n)
        if not isinstance(n_num, int) or n_num < 2:
            raise ValueError("Can only factorize integers >= 2")
        factors = []
        divisor = 2
        while divisor * divisor <= n_num:
            while n_num % divisor == 0:
                factors.append(divisor)
                n_num //= divisor
            divisor += 1
        if n_num > 1:
            factors.append(n_num)
        return factors

    def parse_input(self, val):
        if isinstance(val, (int, float)):
            return val

        val = val.strip().lower()

        # Dictionaries
        for d in [self.ENGLISH_NUMBERS, self.SPANISH_NUMBERS,
                  self.RUSSIAN_NUMBERS, self.CHINESE_NUMBERS]:
            if val in d:
                return d[val]

        # Try float conversion
        try:
            return float(val)
        except ValueError:
            pass

        # Try Roman numeral
        try:
            return self.parse_roman(val.upper())
        except ValueError:
            pass

        raise ValueError(f"Cannot parse input: {val}")

    def parse_roman(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.ROMAN_NUMERAL_MAP.get(char, 0)
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        if total <= 0:
            raise ValueError(f"Invalid Roman numeral: {roman}")
        return total
