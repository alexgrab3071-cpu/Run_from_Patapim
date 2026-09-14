def show_inventory(inv):
    print("\n" + "=" * 40)
    print("          ИНВЕНТАРЬ")
    print("=" * 40)
    for i, item in enumerate(inv, 1):
        print(f"  {i}. {item[0]} - {item[1]}")
    print("=" * 40 + "\n")

def print_menu(options):
    print("\n" + "-" * 30)
    for option in options:
        print(f"  {option}")
    print("-" * 30)

def safe_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Неверный ввод. Введите число от {min(valid_range)} до {max(valid_range)}.")
        except ValueError:
            print("Это не число. Попробуйте снова.")
