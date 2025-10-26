from src.calculator.calculator import Calculator

def main():
    c1 = Calculator()
    c2 = Calculator()

    if id(c1) == id(c2):
        print("same Calculator instance")
    else:
        print("different Calculator instances")

    print(f'1: c1.add(1, 2)        -> {c1.add(1, 2)}')
    print(f'2: c2.add(8, 3)        -> {c2.add(8, 3)}')
    print(f'3: c1.add("1", "1")    -> {c1.add("1", "1")}')
    print(f'4: c1.add("X", "V")    -> {c1.add("X", "V")}')
    print(f'5: c2.factorize(99)    -> {c2.factorize(99)}')
    print(f'6: c1.add("1", "1.600")        -> {c1.add("1", "1.600")}')
    print(f'7: c1.add("three", "1.600")    -> {c1.add("three", "1.600")}')
    print(f'8: c1.add("cinco", "siete")    -> {c1.add("cinco", "siete")}')
    print(f'9: c1.add("семь", "восемь")    -> {c1.add("семь", "восемь")}')
    print(f'10: c1.add("III", "   VIII")   -> {c1.add("III", "   VIII")}')
    print(f'11: c1.add("三", "五")           -> {c1.add("三", "五")}')
    print(f'12: c1.add("0", "X")            -> {c1.add("0", "X")}')
    print(f'13: c2.add("ocho", "nueve")     -> {c2.add("ocho", "nueve")}')
    print(f'14: c2.sub("ocho", "nueve")     -> {c2.sub("ocho", "nueve")}')
    print(f'15: c2.mul("ocho", "nueve")     -> {c2.mul("ocho", "nueve")}')
    print(f'16: c2.div("ocho", "dos")       -> {c2.div("ocho", "dos")}')
    print(f'17: c2.factorize("три")         -> {c2.factorize("три")}')
    print(f'18: c2.factorize("X")           -> {c2.factorize("X")}')
    print(f'19: c2.factorize("ocho")        -> {c2.factorize("ocho")}')
    print(f'20: c2.factorize(3+5)           -> {c2.factorize(3+5)}')
    print(f'21: c2.factorize(27)            -> {c2.factorize(27)}')
    print(f'22: c2.factorize(1092)          -> {c2.factorize(1092)}')
    print(f'23: c2.factorize(32768)         -> {c2.factorize(32768)}')
    print(f'24: c2.factorize(10952347)      -> {c2.factorize(10952347)}')
    print(f'25: c2.factorize(100000039)     -> {c2.factorize(100000039)}')

if __name__ == "__main__":
    main()