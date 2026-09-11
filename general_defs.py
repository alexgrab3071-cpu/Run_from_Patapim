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

def safe_input(prompt, valid_range=None):
    while True:
        try:
            user_input = input(prompt)
            if valid_range is not None:
                num = int(user_input)
                if num in valid_range:
                    return num
                print(f"Введи число от {min(valid_range)} до {max(valid_range)}!")
            else:
                return user_input
        except ValueError:
            print("Введи число, братан!")
