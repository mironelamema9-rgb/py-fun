from src.expressions.expressions import Expressions  # correct absolute import

def main():
    # First instance with default numbers (ODD_LIST)
    e1 = Expressions()
    e1.print_results()

    print("\n--- Second instance with custom numbers ---\n")

    # Second instance with custom numbers (EVEN_LIST)
    custom_numbers = [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
    e2 = Expressions(custom_numbers)
    e2.print_results()

if __name__ == "__main__":
    main()

