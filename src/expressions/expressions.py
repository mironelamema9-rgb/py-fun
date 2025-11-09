class Expressions:
    def __init__(self, numbers=None):
        self.numbers = numbers if numbers is not None else [4, 12, 3, 8, 17, 12, 1, 8, 7]

        # a) number of numbers
        self.a = len(self.numbers)

        # b) first three numbers
        self.b = self.numbers[:3]

        # c) last three numbers
        self.c = self.numbers[-3:]

        # d) last three numbers reversed
        self.d = self.c[::-1]

        # e) odd numbers
        self.e = [n for n in self.numbers if n % 2]

        # f) number of odd numbers
        self.f = len(self.e)

        # g) sum of odd numbers
        self.g = sum(self.e)

        # h) remove duplicates (keep first appearance)
        seen = set()
        self.h = [x for x in self.numbers if not (x in seen or seen.add(x))]

        # i) number of duplicates
        self.i = len(self.numbers) - len(self.h)

        # j) ascending squared numbers without duplicates
        self.j = [n**2 for n in sorted(set(self.numbers))]

        # k) classify list length
        self.k = "EMPTY_LIST" if not self.numbers else ("ODD_LIST" if len(self.numbers) % 2 else "EVEN_LIST")

    def print_results(self):
        print(f"a) number of numbers: {self.a}")
        print(f"b) first three numbers: {self.b}")
        print(f"c) last three numbers: {self.c}")
        print(f"d) last three numbers reversed: {self.d}")
        print(f"e) odd numbers: {self.e}")
        print(f"f) number of odd numbers: {self.f}")
        print(f"g) sum of odd numbers: {self.g}")
        print(f"h) duplicate numbers removed: {self.h}")
        print(f"i) number of duplicate numbers: {self.i}")
        print(f"j) ascending squared numbers (no duplicates): {self.j}")
        print(f"k) length label: {self.k}")
