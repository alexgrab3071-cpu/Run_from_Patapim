import random
import time
from end_pictures import *
from general_defs import *


print("Ссылка на GitHub: https://github.com/alexgrab3071-cpu/Run_from_Patapim.git")
print()
print("=" * 60)
print("ПОБЕГ ИЗ БР БР ПАТАПИМА")
print("=" * 60)
print(
    "После тусы вы с вашими друзьями ехали на такси в сторону дома. Из-за пьянки\n"
    "вы не помните, точно ли доехали до дома. У вас ноет тело и сильно хочется спать,\n"
    "вы приоткрываете глаза и вместо привычной кровати видите темный подвал\n"
    "с гнилыми продуктами. Теперь ваша цель — покинуть это загадочное место."
)
time.sleep(5)

inventory = [
    ["Здоровье", 100],
    ["Деньги", 0]
]

life = True
find_key = False
escaped_basement = False


def p(t):
    for i in t:
        time.sleep(0.05)
        print(i, end="", flush=True)
    print()


def line():
    print("-" * 60)


def menu(options):
    line()
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    line()
    return safe_input(f"Введите число от 1 до {len(options)}: ", range(1, len(options) + 1))


def location_basement():
    global life, find_key, escaped_basement, inventory
    if not escaped_basement:
        print()
        print("=" * 60)
        print("ТЁМНЫЙ ПОДВАЛ")
        print("=" * 60)
        options = [
            "Еще поспать, мало-ли это кошмар?",
            "(уже осмотрено)" if find_key else "Осмотреться, может, что-то будет видно?",
            "Позвать на помощь, а то подвал закрыт",
            "Постараться выбраться"
        ]
        thirst_choose = menu(options)

        if thirst_choose == 1:
            print()
            print("Еще поспать.")
            time.sleep(1)
            print("Вы постарались уснуть, но проснулись уже в мясной лавке светофора...")
            time.sleep(1)
            print("Видимо, терять контроль над происходящим было ошибкой...")
            time.sleep(1)
            print(end_pictures["Мясная лавка Светофора"])
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"

        elif thirst_choose == 2:
            if find_key:
                print("Вы уже осмотрелись здесь, больше ничего нет.")
                input("\nНажми Enter, чтобы продолжить...")
                return "basement"
            else:
                r = random.randint(1, 3)
                if r == 1:
                    print("Осмотреться.")
                    time.sleep(1)
                    print("Вы смогли различить под ногами одноразовую отмычку, отлично, может пригодиться.")
                    time.sleep(1)
                    print("А так же рядом с отмычкой лежал странный прибор, который требовал 5-значный код.")
                    time.sleep(1)
                    print("А рядом лежала помятая записка, на которой было написано: 08251")
                    time.sleep(1)
                    code_pashalco = input("Вы решили попробовать ввести код, что вы введете: ")
                    if code_pashalco == "57085":
                        time.sleep(3)
                        print("\nРеальность вокруг меняется")
                        time.sleep(1)
                        print("\nПривычный подвал сменяется странным офисом")
                        time.sleep(1)
                        print("\nВы узнаёте офисы Microsoft")
                        time.sleep(1)
                        print("\nКак только вы отворачиваетесь к своему ноутбуку, понимая, что вы раб системы...")
                        time.sleep(1)
                        print("\nСзади на вас нападает другой работник... вы падаете на пол без сил, полу мертвые")
                        time.sleep(3)
                        die = 0
                        while life and die < 100:
                            die += 1
                            print(f"Вы умерли на {die}%")
                            time.sleep(0.05)
                        life = False
                        return "end"
                    elif code_pashalco == "банан":
                        print("\nРеальность вокруг меняется")
                        time.sleep(1)
                        print("\nПривычный подвал сменяется странным хаммамом")
                        time.sleep(1)
                        print("\nРядом Меллстрой танцует ХАММАМ, вы попали в Хаммам, покинув это страшное поместье")
                        time.sleep(3)
                        hot = 0
                        print(
                            "...........................................................................\n"
                            ".................................@@@@@@@...................................\n"
                            "...............................@@@@@@@@@@@.................................\n"
                            "..............................@@@@@@@@@@@@@................................\n"
                            "..............................############.................................\n"
                            ".............................##############................................\n"
                            ".............................##############................................\n"
                            ".............................##############................................\n"
                            "..............................############.................................\n"
                            "...............................##########..................................\n"
                            "......................//////////########//////////.........................\n"
                            "...................////////////##########////////////......................\n"
                            ".................////////////############////////////......................\n"
                            "...............#############/############/#############....................\n"
                            "..............##############/############/##############...................\n"
                            ".............###############/############/###############..................\n"
                            "............################/############/################.................\n"
                            "............################/############/################.................\n"
                            "............################/############/################.................\n"
                            "............################/############/.................................\n"
                            "............################/############/.................................\n"
                            "............################/############/.................................\n"
                            ".............###############/############/.................................\n"
                            "..............##############/############/.................................\n"
                            "...............#############/############/.................................\n"
                            ".................///////////############/..................................\n"
                            "...........................##############..................................\n"
                            "..........................%%%%%%%%%%%%%%%%.................................\n"
                            ".........................%%%%%%%%%%%%%%%%%%................................\n"
                            "........................%%%%%%%%%%%%%%%%%%%%...............................\n"
                            "........................%%%%%%%%%%%%%%%%%%%%...............................\n"
                            "........................%%%%%%        %%%%%%...............................\n"
                            "........................%%%%%          %%%%%...............................\n"
                            "........................%%%%            %%%%...............................\n"
                            "........................###              ###...............................\n"
                            "........................###              ###...............................\n"
                            "........................###              ###...............................\n"
                            ".......................####              ####..............................\n"
                            ".......................####              ####..............................\n"
                            ".......................####              ####..............................\n"
                            "......................#####              #####.............................\n"
                            "......................#####              #####.............................\n"
                            ".....................######              ######............................\n"
                            "....................#######              #######...........................\n"
                            "...................########              ########..........................\n"
                            "..................#########              #########.........................\n"
                            "..................#########              #########.........................\n"
                            "...................#######                #######..........................\n"
                            ".....................###                    ###............................\n"
                            "..........................................................................."
                        )
                        while life and hot < 100:
                            hot += 1
                            print(f"Вам жарко в хаммаме на {hot}%")
                            time.sleep(0.05)
                        life = False
                        return "end"

                    inventory.append(["Отмычка", 1])
                    find_key = True

                else:
                    print("Осмотреться.")
                    time.sleep(1)
                    print("Увы, глаза еще не привыкли к темноте...")
                input("\nНажми Enter, чтобы продолжить...")
                return "basement"

        elif thirst_choose == 3:
            print("\nВ глубине мрака вы слышите шаги, будто слон топает по металлу.")
            time.sleep(2)
            print("Вскоре появляется силуэт, явно жаждущий вашей крови.")
            time.sleep(2)
            print("Вы узнаете в нем БР-БР ПАТАПИМА...")
            time.sleep(2)
            print("Но это было последнее, о чем вы думаете...")
            time.sleep(1)
            print(end_pictures["Обед Патапима"])
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"

        elif thirst_choose == 4:
            if find_key:
                print("\nЗамок щелкает, по ржавой лестнице вы поднимаетесь на первый этаж здания.")
                time.sleep(1)
                print("ПРОХОД ЗАВАЛИВАЕТ. Пути назад нет.")
                time.sleep(1)
                print("Вы стоите в коридоре старого заброшенного здания. Слышно, как ветер завывает в щелях.")
                time.sleep(1)
                input("\nНажми Enter, чтобы продолжить...")
                inventory.append(["Отмычка использована", 0])
                escaped_basement = True
                return "house_hall"
            else:
                print("\nЧерт, замок закрыт, чем бы открыть?")
                time.sleep(1)
                print("Может, тут что-то есть поблизости?")
                input("\nНажми Enter, чтобы продолжить...")
                return "basement"
    return "house_hall"


def location_house_hall():
    global life, found_light, inventory, location, tapochki, cherdak_key, found_patapim_key, found_car_key, vent, see_car, found_caboom, uran_candies
    if not found_light:
        print()
        print("=" * 60)
        print("ХОЛЛ ПОМЕСТЬЯ (ТЕМНОТА)")
        print("=" * 60)
        print("После выхода в холл поместья ваши глаза ничего не различают")
        time.sleep(1)
        print("Ориентироваться можно только на ощупь...")
        time.sleep(1)
        choose = menu([
            "Пойти вперед, постараться найти что-то на ощупь...",
            "Искать предметы на ощупь...",
            "Посмотреть инвентарь..."
        ])

        if choose == 1:
            time.sleep(1)
            print("Вы пошли наобум, это была плохая идея, вы вышли в тот же холл...")
            return "house_hall"

        elif choose == 2:
            time.sleep(1)
            r = random.randint(1, 3)
            if r == 1:
                print("Вы смогли найти фонарик, который мог бы помочь, и рубильник.")
                time.sleep(1)
                choose_1 = menu([
                    "Взять фонарик, забыв про рубильник",
                    "Дернуть рычаг рубильника, проверить, что случится"
                ])
                if choose_1 == 1:
                    print("Отлично, теперь хоть что-то видно!")
                    inventory.append(["Рабочий фонарик", 1])
                    found_light = True
                    return "house_hall"
                else:
                    time.sleep(1)
                    print("Вы включили свет... Яркая вспышка ослепила вас, и вы нашли себя очнувшимся уже в мясной лавке Светофора...")
                    return "mogila"
            else:
                print("Пока что глаза не привыкли...")
                time.sleep(1.5)
                return "house_hall"

        elif choose == 3:
            show_inventory(inventory)
            return "house_hall"

    if found_light:
        print()
        print("=" * 60)
        print("ХОЛЛ ПОМЕСТЬЯ")
        print("=" * 60)
        print("Вы находитесь в холле, с фонариком. Теперь все пути видно, куда пойдете?")
        time.sleep(1)
        choose = menu([
            "Направо, к лестнице",
            "Налево, на кухню",
            "Вперед, к прихожей",
            "Посмотреть инвентарь..."
        ])
        if choose == 1:
            time.sleep(1)
            print("Вы идете направо к лестнице...")
            return "stairs_1_floor"
        elif choose == 2:
            time.sleep(1)
            print("Вы идете налево на кухню...")
            return "kitchen"
        elif choose == 3:
            time.sleep(1)
            print("Вы идете вперед к прихожей...")
            return "prihozhaya"
        elif choose == 4:
            time.sleep(1)
            show_inventory(inventory)
            return "house_hall"
    return "house_hall"


def location_mogila():
    global life
    print("F " * 30)
    print()
    print("=" * 60)
    print("ИГРА ОКОНЧЕНА")
    print("=" * 60)
    life = False
    return "end"


def location_stairs_1_floor():
    print()
    print("=" * 60)
    print("ЛЕСТНИЦА (1 ЭТАЖ)")
    print("=" * 60)
    time.sleep(1)
    print("Вы слышите, как кто-то храпит на втором этаже...")
    time.sleep(1)
    choose = menu([
        "Остаться на первом этаже, пойти в холл...",
        "Пойти по лестнице на второй этаж..."
    ])
    if choose == 1:
        time.sleep(1)
        print("Вы отходите от лестницы и приходите в холл...")
        return "house_hall"
    else:
        print("Вы решаетесь подняться на второй этаж на храп...")
        time.sleep(1)
        return "stairs_2_floor"


def location_stairs_2_floor():
    global cherdak_key, found_patapim_key, tapochki, inventory
    print()
    print("=" * 60)
    print("ЛЕСТНИЦА (2 ЭТАЖ)")
    print("=" * 60)
    time.sleep(1)
    print("Вы находитесь на втором этаже, перед вами 2 двери, из левой слышен храп а правая закрыта на замок")
    time.sleep(2)
    choose = menu([
        "Открыть правую дверь...",
        "Пойти в левую дверь, на храп...",
        "Пойти назад, на первый этаж...",
        "Посмотреть инвентарь..."
    ])
    if choose == 1:
        if cherdak_key:
            time.sleep(1)
            print("Замок удачно щелкает, путь на чердак открыт!")
            return "cherdak"
        else:
            time.sleep(1)
            print("К сожлению, дверь не поддается, тут нужен специальный ключ...")
            return "stairs_2_floor"
    elif choose == 2:
        time.sleep(1)
        print("Вы продвигаетесь к левой комнате, звуки храпа усиливаются...")
        time.sleep(1)
        return "Patapim_room"
    elif choose == 3:
        print("Вы спускаетесь обратно на первый этаж...")
        time.sleep(1)
        return "stairs_1_floor"
    elif choose == 4:
        show_inventory(inventory)
        return "stairs_2_floor"
    return "stairs_2_floor"


def location_Patapim_room():
    global found_patapim_key, tapochki, inventory, life
    print()
    print("=" * 60)
    print("КОМНАТА ПАТАПИМА")
    print("=" * 60)
    time.sleep(1)
    print("Перед вами лежит огромное существо из знаменитой группы ИИподобной mozgognil...")
    time.sleep(1)
    options = ["Выйти обратно в холл этажа 2..."]
    if not found_patapim_key:
        options.append("Постараться забрать странные ключи на тумбочке Бр-бр Патапима (вы их увидели)...")
    else:
        options.append("(Уже забрано)")
    options.append("Напасть на Бр-бр Патапима...")
    options.append("Посмотреть инвентарь...")
    choose = menu(options)

    if choose == 1:
        print("Вы вышли...")
        time.sleep(1)
        return "stairs_2_floor"
    if not found_patapim_key:
        if choose == 2 and not tapochki:
            print("Это была хорошая попытка пройти мимо mozgognil, но Mozhognil раздавило вас своей ногой...")
            print(end_pictures["Мясная лавка Светофора"])
            return "mogila"
        if choose == 2 and tapochki:
            print("У вас получается незаметно пройти к тумбочке и забрать ключи... Что они открывают?")
            found_patapim_key = True
            return "Patapim_room"
    if choose == 3:
        print("Mozgognil Вас легко раздавил...")
        print(end_pictures["Мясная лавка Светофора"])
        return "mogila"
    if choose == 4:
        show_inventory(inventory)
        return "Patapim_room"
    return "Patapim_room"


def location_kitchen():
    global found_car_key, see_car, inventory, uran_candies
    print()
    print("=" * 60)
    print("КУХНЯ")
    print("=" * 60)
    time.sleep(1)
    print("Вы проходите по корридору в сторону кухни.")
    time.sleep(1)
    options = ["Проверить ящики с едой"]
    if not found_car_key:
        options.append("Проверить ящики с не едой")
    else:
        options.append("(Уже изрыто)")
    options += [
        "Подойти к столу",
        "Уйти обратно в холл этажа 1",
        "Посмотреть инвентарь"
    ]
    choose = menu(options)
    if choose == 1:
        r = random.randint(1, 2)
        if r == 1:
            print("В ящике вы ничего не нашли, там кучу хлама, но может, есть что-то еще?")
            time.sleep(1)
        else:
            print("Вам удалось найти в ящике что-то.. это были урановые конфетки, они добавились в ваш инвентарь.")
            if ["Урановые конфетки", 1] not in inventory:
                inventory.append(["Урановые конфетки", 1])
                uran_candies = True
            time.sleep(1)
        return "kitchen"
    elif choose == 2 and not found_car_key:
        print("Вы начали рыться в мусорке...")
        time.sleep(1.5)
        r = random.randint(1, 3)
        if r == 1:
            print("В мусорке вы нашли ключи от машины.")
            inventory.append(["Ключи от машины", 1])
            found_car_key = True
        else:
            print("В мусорке ничего не нашлось")
        return "kitchen"
    elif choose == 3:
        time.sleep(1)
        print("Подойдя к столу, вы заметили гараж, который стоял слева от выходной двери. Теперь вы знаете, что есть гараж слева от выхода")
        see_car = True
        return "kitchen"
    elif choose == 4:
        time.sleep(1)
        print("Вы ушли в холл")
        return "house_hall"
    elif choose == 5:
        time.sleep(1)
        show_inventory(inventory)
        return "kitchen"
    return "kitchen"


def location_prihozhaya():
    global vent, cherdak_key, tapochki, inventory, found_patapim_key
    print()
    print("=" * 60)
    print("ПРИХОЖАЯ")
    print("=" * 60)
    print("Вы идете в сторону прихожей...")
    time.sleep(1)
    print("Вы замечаете маленькую вентиляцию около двери...")
    time.sleep(1)
    options = []
    if not vent:
        options.append("Полезть в вентиляцию")
    else:
        options.append("Вы уже лазали в вентиляцию.")
    options += [
        "Открыть выходную дверь",
        "Вернуться обратно в холл",
        "Посмотреть инвентарь"
    ]
    choose = menu(options)
    if choose == 1 and not vent:
        time.sleep(1)
        print("Вы пролезаете в вентиляцию, там вы находите две вещи: Мягкие тапочки и ключи от какой-то двери...")
        inventory.append(["Мягкие тапочки", 1])
        inventory.append(["Ключ от чердака", 1])
        cherdak_key = True
        tapochki = True
        vent = True
        time.sleep(1)
        print("Вы вылезли обратно.")
        return "prihozhaya"
    elif choose == 2:
        if not found_patapim_key:
            print("Дверь не поддается, наверняка есть какой-то ключ...")
            time.sleep(1)
            return "prihozhaya"
        else:
            print("Дверь успешно открылась, вы вышли на улицу.")
            return "street_next_to_house"
    elif choose == 3:
        print("Вы идете в холл")
        time.sleep(1)
        return "house_hall"
    elif choose == 4:
        show_inventory(inventory)
        return "prihozhaya"
    return "prihozhaya"


def location_cherdak():
    global found_caboom
    print()
    print("=" * 60)
    print("ЧЕРДАК")
    print("=" * 60)
    print("Вы поднимаетесь на чердак...")
    time.sleep(2)
    print("Вы чувствуете, как что-то меняется в воздухе...")
    time.sleep(2)
    print("Поднимаясь, вы видите ядерное оружие, которое лежит на гнилых досках Mozgognil(-и).")
    found_caboom = True
    time.sleep(2)
    print("Может, можно как-то отвезти оружие, после чего взорвать?")
    time.sleep(2)
    print("На полу вы находите записку:")
    s = ("Как уничтожить Mozgognil: сначала нужно получить доступ к секретному орудию, потом собрать урановые вещества...\n"
         " Дальше нужно увезти орудие на машине и запустить в Mozgognil.")
    for i in s:
        print(i, end="")
    print()
    time.sleep(2)
    print("\nВы спускаетесь на второй этаж...")
    return "stairs_2_floor"


def location_street_next_to_house():
    global see_car, life
    print()
    print("=" * 60)
    print("УЛИЦА РЯДОМ С ДОМОМ")
    print("=" * 60)
    print("Вы выбираетесь на улицу, вместо привычной деревни/города вы видите темный лес и только лишь дорога выделяется на фоне мрака.")
    time.sleep(3)
    options = [
        "Пойти вперед, к дороге",
        "Уйти обратно в холл"
    ]
    if see_car:
        options.append("Повернуть налево, к машине")
    else:
        options.append("(ЗАКРЫТО, МОЖНО ОТКРЫТЬ НА ЛОКАЦИЯХ)")
    options.append("Посмотреть инвентарь")
    choose = menu(options)
    if choose == 1:
        print("Перед вами калитка. Вы открываете ее и выходите на дорогу.")
        time.sleep(1)
        print("Как бы долго вы не шли, вы все равно приходите туда же, будучи в депрессии, вы решаете пойти не\n по дороге, а в лес")
        time.sleep(3)
        print("Там все деревья темные, но вскоре вы выходите на поляну, где виднеется что-то странное.")
        time.sleep(2)
        print("Вам кажется, будто в N-ном месте воздух искажается...")
        time.sleep(2)
        choose = menu([
            "Уйти обратно, на дорогу",
            "Зайти в разлом реальности"
        ])
        if choose == 1:
            print("Вы пытаетесь найти дорогу назад, но умираете от голода и жажды в вечных поисках")
            return "mogila"
        else:
            print("Вы попадаете в... вы попадаете в сон спящего Mozgognil.")
            time.sleep(1)
            print("Он вас съедает")
            print(end_pictures["Тролол"])
            return "mogila"
    elif choose == 2:
        print("Вы идете в прихожую...")
        time.sleep(1)
        return "prihozhaya"
    elif choose == 3 and see_car:
        print("Вы идете к машине, подходите к ней...")
        time.sleep(1)
        return "next_to_car"
    elif choose == 3 and not see_car:
        print("Так нечестно!")
        time.sleep(1)
        return "street_next_to_house"
    elif choose == 4:
        show_inventory(inventory)
        return "street_next_to_house"
    return "street_next_to_house"


def location_next_to_car():
    global found_car_key
    print()
    print("=" * 60)
    print("РЯДОМ С МАШИНОЙ")
    print("=" * 60)
    print("Вы подходите к машине, на машине есть огромный кузов, может, попробовать уехать?")
    time.sleep(2)
    choose = menu([
        "Попробовать открыть машину...",
        "Уйти обратно к выходу из дома...",
        "Посмотреть инвентарь..."
    ])
    if choose == 1 and found_car_key:
        print("С помощью ключа вы открываете дверь машины и садитесь за руль")
        return "car_seat"
    elif choose == 1 and not found_car_key:
        print("Вы попытались открыть дверь, но она не поддалась - нужны ключи.")
        return "next_to_car"
    elif choose == 2:
        print("Вы возвращаетесь к выходу из дома...")
        time.sleep(1)
        return "street_next_to_house"
    elif choose == 3:
        show_inventory(inventory)
        return "next_to_car"
    return "next_to_car"


def location_car_seat():
    global found_caboom, uran_candies, life
    print()
    print("=" * 60)
    print("В МАШИНЕ")
    print("=" * 60)
    print("Вам знакома эта машина, это популярная марка Baobabys, теперь вы в машине")
    time.sleep(2)
    options = ["Уехать по шоссе в город"]
    if found_caboom and uran_candies:
        options.append("Исполнить план по изъятию ядерного оружия...")
    else:
        options.append("|ЗАКРЫТО|")
    options += [
        "Выйти обратно во двор",
        "Посмотреть инвентарь"
    ]
    choose = menu(options)
    if choose == 1:
        print("Вы уехали в город, начало расцветать, вы узнавали Москву все лучше, часть 1 закончилась...")
        print()
        print("=" * 60)
        print("Конец части 1 (хорошая концовка)")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 2 and found_caboom and uran_candies:
        print("Итак, началось...")
        time.sleep(1)
        print("Вы пробрались на чердак, вынесли ядерное оружие на прицеп...")
        time.sleep(1)
        print("Вы измельчили уран из конфет и засыпали его в орудие")
        time.sleep(1)
        print("После чего вы поехали по шоссе")
        time.sleep(1)
        print("Вы выехали на достаточное расстояние (676.7 км) и запустили Ядерное орудие на координаты поместья Патапимовичей")
        time.sleep(3)
        print("Вы уехали в город, начало расцветать, вы узнавали Москву все лучше, часть 1 закончилась...")
        print()
        print("=" * 60)
        print("Конец игры (хорошая концовка)")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 3:
        print("Вы вышли в гараж")
        time.sleep(1)
        return "street_next_to_house"
    elif choose == 4:
        show_inventory(inventory)
        return "car_seat"
    return "car_seat"


def location_town():
    global life, have_phone, location, inventory, deth_babke
    print()
    print("=" * 60)
    print("ГОРОД")
    print("=" * 60)
    time.sleep(1)
    print("Вы приехали в город, доступные выборы:")
    choose = menu([
        "Искать работу",
        "Пойти в ТЦ",
        "Попрошайничать",
        "Пойти на автобусную остановку",
        "Пойти в метро",
        "Посмотреть инвентарь"
    ])

    if choose == 1:
        if not have_phone:
            print("У вас не было телефона, чтобы поискать работу, у вас выбор: Идти дворником / Идти продавцом Moggнита.")
            time.sleep(1)
            sub_choose = menu([
                "Устроиться на работу дворником.",
                "Устроиться на работу продавцом",
                "Ничего не делать, вернуться к выбору"
            ])
            if sub_choose == 1:
                print("Вы устроились дворником...")
                time.sleep(1)
                return "work_dvornik"
            elif sub_choose == 2:
                print("Вы устроились продавцом...")
                time.sleep(1)
                return "work_prodavec"
            else:
                print("Вы забили на работу")
                return "town"
        else:
            print("Вы уже нашли работу с телефоном (заглушка).")
            return "town"

    elif choose == 2:
        print("Вы пошли в ТЦ..")
        time.sleep(1)
        return "shopping_centre"

    elif choose == 3:
        r = random.randint(1, 20)
        print(f"Вы напопрошайничали {r} рублей")
        inventory[1][1] += r
        return "town"

    elif choose == 4:
        print("Вы пошли на остановку..")
        time.sleep(1)
        print("На остановке сидела бабушка, автобус будет через минуту.")
        time.sleep(1)
        options = []
        if not deth_babke:
            options.append("Избить бабку")
        else:
            options.append("Хз, побейте труп...")
        options += [
            "Ждать автобус",
            "Уйти в город"
        ]
        sub_choose = menu(options)
        if sub_choose == 1 and not deth_babke:
            r = random.randint(10, 50)
            print(f"Вы подошли к бабке, избили ее, с нее вы получили + {r*10} рублей.")
            inventory[1][1] += r * 10
            deth_babke = True
            return "town"
        elif sub_choose == 1 and deth_babke:
            print("Вы уже убили бабку")
            return "town"
        elif sub_choose == 2:
            print("Автобус приехал, вы сели в него, проехали зайцем, поехали...")
            time.sleep(1)
            r = random.randint(1, 3)
            if r == 1:
                print("Автобус приехал в Село Молочное")
                return "selo_molochnoe"
            elif r == 2:
                print("Автобус приехал в Высший Новгород")
                return "higth_n"
            else:
                print("Автобус приехал в Зачекушье")
                return "back_chekyshie"
        else:
            return "town"

    elif choose == 5:
        print("Вы спустились в метро, тут только 1 станция, вы вышли.")
        return "town"

    elif choose == 6:
        show_inventory(inventory)
        return "town"

    return "town"


def location_work_dvornik():
    global life, inventory, location
    print()
    print("=" * 60)
    print("РАБОТА ДВОРНИКОМ")
    print("=" * 60)
    print("Вы устроились работать дворником...")
    time.sleep(2)
    choose = menu([
        "Работать",
        "Работать",
        "Бросить работу",
        "Посмотреть инвентарь"
    ])
    if choose == 1 or choose == 2:
        for i in range(10):
            print(f"Вы поработали на {i}%")
        r = random.randint(1, 5)
        print(f"Вы заработали {r*1000} рублей.")
        inventory[1][1] += r * 1000
        return "work_dvornik"
    elif choose == 3:
        print("Вы бросили работать, так и быть...")
        return "town"
    elif choose == 4:
        show_inventory(inventory)
        return "work_dvornik"
    return "work_dvornik"


def location_work_prodavec():
    global life, location, inventory
    print()
    print("=" * 60)
    print("РАБОТА ПРОДАВЦОМ")
    print("=" * 60)
    print("Вы устроились работать продавцом")
    things = ["Яблоко", "Банан", "Котось", "Бумага А4", "Бумага RGB", "Бумага A67", "Ананас", "RTX6090", "Соль", "Мозгогниль", "Польша"]
    time.sleep(1)
    choose = menu([
        "Пойти на кассу, принять товары",
        "Уйти.",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        show = []
        for i in range(random.randint(1, 5)):
            r = random.choice(things)
            show.append(r)
        time.sleep(1)
        print("Пользователь а покупает:")
        for item in show:
            print(item)
        time.sleep(3)
        choose = menu(["Оплатить"])
        if choose == 1:
            r = random.randint(1, 10)
            print(f"Вы заработали с покупки {r*1000} Рублей")
            inventory[1][1] += r * 1000
        return "work_prodavec"
    elif choose == 2:
        print("Вы покинули рабство")
        time.sleep(1)
        return "town"
    elif choose == 3:
        show_inventory(inventory)
        return "work_prodavec"
    return "work_prodavec"


def location_selo_molochnoe():
    global life, location, inventory, found_AP, have_AP_ticket
    print()
    print("=" * 60)
    print("СЕЛО МОЛОЧНОЕ")
    print("=" * 60)
    time.sleep(1)
    print("Вы вышли из автобуса в село молочное...")
    time.sleep(1)
    options = [
        "Прогуляться по селу",
        "Пойти в лес"
    ]
    if have_AP_ticket:
        options += [
            "Пойти в Алабуга Политех",
            "Уехать из села в город",
            "Посмотреть инвентарь"
        ]
    else:
        options.append("Посмотреть инвентарь")
    choose = menu(options)

    if choose == 1:
        print("Вы решили прогуляться, вы заметили паука вдали, он был примерно 35 метров в высоту")
        time.sleep(1)
        sub_choose = menu([
            "Напасть на него",
            "Спросить у него, нет ли ничего прикольного",
            "Посмотреть инвентарь"
        ])
        if sub_choose == 1:
            print("Он вас убил.")
            return "mogila"
        elif sub_choose == 2:
            print("Вы подошли к нему, спросили.")
            time.sleep(1)
            text = ("-Эй, есть-ли что-то интересное?."
                    "-AAABBBCCCuwrfjw00245"
                    "-Что это значит?"
                    "-***___***"
                    "-SOS???"
                    "-Yes"
                    "-Ладно, есть что-то?"
                    "-Found My UltraGiperGrandGrandPa."
                    "-Окей, тогда отдашь что-то?"
                    "-Yes, of course!")
            p(text)
            print("Вы пошли искать Grandpa...")
            time.sleep(1)
            print("Ищете...")
            time.sleep(5)
            print("Нашли!")
            time.sleep(1)
            print("Obkect отдал вам кое что...")
            print("Билет в Алабуга Политех")
            if not have_AP_ticket:
                inventory.append(["Билет в Алабуга Политех", 1])
                have_AP_ticket = True
                found_AP = True
            return "selo_molochnoe"
        else:
            show_inventory(inventory)
            return "selo_molochnoe"

    elif choose == 2:
        print("В лесу вы потеряли левую ногу и умерли.")
        return "mogila"

    elif choose == 3 and have_AP_ticket:
        print("Вы идёте в Алабуга Политех...")
        time.sleep(1)
        return "Alab_P"

    elif choose == 4 and have_AP_ticket:
        print("Вы уехали из села обратно в город...")
        time.sleep(1)
        return "town"

    elif (choose == 3 and not have_AP_ticket) or (choose == 5 and have_AP_ticket):
        show_inventory(inventory)
        return "selo_molochnoe"

    return "selo_molochnoe"


def location_shopping_centre():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ТОРГОВЫЙ ЦЕНТР")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Уйти в город",
        "Пойти в Магазин Светофор",
        "Пойти в Магазин Авиасейлс",
        "Пойти в Кинотеатр",
        "Пойти в ПК магазин",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        print("Вы вышли из ТЦ в город...")
        time.sleep(1)
        return "town"
    elif choose == 2:
        print("Вы идёте в магазин Светофор...")
        time.sleep(1)
        return "svetofor"
    elif choose == 3:
        print("Вы идёте в магазин Авиасейлс...")
        time.sleep(1)
        return "aviasales"
    elif choose == 4:
        print("Вы идёте в кинотеатр...")
        time.sleep(1)
        return "cinema"
    elif choose == 5:
        print("Вы идёте в ПК магазин...")
        time.sleep(1)
        return "pk_shop"
    elif choose == 6:
        show_inventory(inventory)
        return "shopping_centre"
    return "shopping_centre"


def location_svetofor():
    global life, location, inventory
    print()
    print("=" * 60)
    print("МАГАЗИН СВЕТОФОР")
    print("=" * 60)
    time.sleep(1)
    print("Вы в магазине Светофор. Тут пахнет... странно.")
    choose = menu([
        "Купить мясо (если денег больше 100)",
        "(двери закрыты)",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        if inventory[1][1] > 100:
            inventory[1][1] -= 100
            print("Вы купили мясо. Оно выглядит... подозрительно.")
            time.sleep(2)
            print("Вы съели мясо. Оно оказалось человечиной.")
            time.sleep(2)
            print("Вы стали канибалом. Концовка: Канибализм.")
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"
        else:
            print("У вас недостаточно денег (нужно больше 100).")
            return "svetofor"
    elif choose == 2:
        print("Двери закрыты. Вы не можете выйти отсюда... но и не можете войти куда-то ещё.")
        return "svetofor"
    elif choose == 3:
        show_inventory(inventory)
        return "svetofor"
    return "svetofor"


def location_aviasales():
    global life, location, inventory
    print()
    print("=" * 60)
    print("МАГАЗИН АВИАСЕЙЛС")
    print("=" * 60)
    time.sleep(1)
    print("Вы в магазине Авиасейлс. Тут продают билеты.")
    choose = menu([
        "Купить билет (если денег больше 10 000)",
        "Уйти в ТЦ",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        if inventory[1][1] > 10000:
            inventory[1][1] -= 10000
            print("Вы купили билет на самолёт!")
            time.sleep(1)
            print("Вы садитесь в самолёт...")
            time.sleep(2)
            return "airplane"
        else:
            print("У вас недостаточно денег (нужно больше 10 000).")
            return "aviasales"
    elif choose == 2:
        print("Вы уходите в ТЦ...")
        time.sleep(1)
        return "shopping_centre"
    elif choose == 3:
        show_inventory(inventory)
        return "aviasales"
    return "aviasales"


def location_airplane():
    global life, location
    print()
    print("=" * 60)
    print("САМОЛЁТ")
    print("=" * 60)
    time.sleep(2)
    print("Самолёт взлетает...")
    time.sleep(2)
    r = random.randint(1, 3)
    if r == 1:
        print("Вы прилетели в Страну Mogg.")
        time.sleep(2)
        print("Концовка: Страна Mogg.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif r == 2:
        print("Вы прилетели в доисторическую эру.")
        time.sleep(2)
        print("Вас съел динозавр. Концовка: Доисторическая эра.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    else:
        print("Вы прилетели на шоу Поле Чудес.")
        time.sleep(2)
        return "pole_chudes"


def location_pole_chudes():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ПОЛЕ ЧУДЕС")
    print("=" * 60)
    time.sleep(1)
    print("Вы на шоу Поле Чудес! Якубович смотрит на вас.")
    choose = menu([
        "Угадать слово",
        "Уйти"
    ])
    if choose == 1:
        words = ["арбузы", "хаммам", "изоляция"]
        secret = random.choice(words)
        print(f"Ведущий загадал слово из {len(secret)} букв.")
        guess = input("Введите слово: ").strip().lower()
        if guess == secret:
            print("Вы угадали слово! Вы выиграли миллион!")
            inventory[1][1] += 1000000
            time.sleep(2)
            print("Концовка: Победитель Поля Чудес.")
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"
        else:
            print(f"Вы не угадали. Было загадано слово: {secret}")
            time.sleep(2)
            print("Вы ушли в пустоту. Концовка: Пустота.")
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"
    elif choose == 2:
        print("Вы ушли в пустоту. Концовка: Пустота.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    return "pole_chudes"


def location_cinema():
    global life, location, inventory
    print()
    print("=" * 60)
    print("КИНОТЕАТР")
    print("=" * 60)
    time.sleep(1)
    print("Вы в кинотеатре. Что будете смотреть?")
    choose = menu([
        "Смешарики сквозь вселенные",
        "Человек-паук",
        "Колобок",
        "Уйти",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        print("Вы посмотрели Смешарики сквозь вселенные...")
        time.sleep(2)
        print("После фильма вас избили. Концовка: Избиение после фильма.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 2:
        print("Вы посмотрели Человека-паука. Ваша аура +100!")
        inventory.append(["Аура", 100])
        time.sleep(1)
        return "shopping_centre"
    elif choose == 3:
        print("Вы посмотрели Колобка...")
        time.sleep(2)
        print("Вас запинали до смерти. Концовка: Запинали до смерти.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 4:
        print("Вы уходите из кинотеатра...")
        time.sleep(1)
        return "shopping_centre"
    elif choose == 5:
        show_inventory(inventory)
        return "cinema"
    return "cinema"


def location_pk_shop():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ПК МАГАЗИН")
    print("=" * 60)
    time.sleep(1)
    print("Вы в ПК магазине. Тут продают компьютеры и арендуют места.")
    choose = menu([
        "Купить сборку ПК (если денег больше 50 000)",
        "Арендовать ПК на час (если денег больше 10 000)",
        "Уйти",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        if inventory[1][1] > 50000:
            inventory[1][1] -= 50000
            print("Вы купили сборку ПК! Теперь вы можете играть дома.")
            time.sleep(1)
            print("Вы идёте в город...")
            return "town"
        else:
            print("У вас недостаточно денег (нужно больше 50 000).")
            return "pk_shop"
    elif choose == 2:
        if inventory[1][1] > 10000:
            inventory[1][1] -= 10000
            print("Вы арендовали ПК на час!")
            time.sleep(1)
            return "ecran_pk"
        else:
            print("У вас недостаточно денег (нужно больше 10 000).")
            return "pk_shop"
    elif choose == 3:
        print("Вы уходите из ПК магазина...")
        time.sleep(1)
        return "shopping_centre"
    elif choose == 4:
        show_inventory(inventory)
        return "pk_shop"
    return "pk_shop"


def location_ecran_pk():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ЭКРАН ПК")
    print("=" * 60)
    time.sleep(1)
    print("Вы за ПК. Что будете делать?")
    choose = menu([
        "Поиграть в Minecraft",
        "Поиграть в Сапера",
        "Поиграть в CS2",
        "Выйти в город"
    ])
    if choose == 1:
        return "minecraft"
    elif choose == 2:
        return "saper"
    elif choose == 3:
        return "cs2"
    elif choose == 4:
        print("Вы вышли в город...")
        time.sleep(1)
        return "town"
    return "ecran_pk"


def location_minecraft():
    global life, location
    print()
    print("=" * 60)
    print("MINECRAFT")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Новый мир",
        "Выйти из игры"
    ])
    if choose == 1:
        hours = random.randint(1, 24)
        print(f"Вы играли {hours} часов и прошли Minecraft. Молодцы!")
        time.sleep(2)
        return "ecran_pk"
    elif choose == 2:
        print("Вы вышли из Minecraft...")
        time.sleep(1)
        return "ecran_pk"
    return "minecraft"


def location_saper():
    global life, location
    print()
    print("=" * 60)
    print("САПЁР")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Играть",
        "Выйти"
    ])
    if choose == 1:
        print("Вы играли в Сапёра. Молодцы!")
        time.sleep(2)
        return "ecran_pk"
    elif choose == 2:
        print("Вы вышли из Сапёра...")
        time.sleep(1)
        return "ecran_pk"
    return "saper"


cs2_weapons = {
    "Пистолет": 1,
    "SMG": 2,
    "Винтовка": 4,
    "AWP": 5,
    "Нож": 1,
}


def cs2_show_hud(map_name, team, hp, money, weapon, armor, kills, pos, total):
    line()
    print(f"  Карта: {map_name}  |  Сторона: {team}")
    print(f"  HP: {hp}  |  Деньги: ${money}  |  Убийств: {kills}")
    print(f"  Оружие: {weapon}  |  Броня: {'да' if armor else 'нет'}")
    print(f"  Позиция: {pos}/{total}")
    line()


def cs2_buy_menu(money, weapon, armor):
    print()
    print("МАГАЗИН:")
    choice = menu([
        "Пистолет      — $0     (сила 1)",
        "SMG           — $1200  (сила 2)",
        "Винтовка      — $2700  (сила 4)",
        "AWP           — $4750  (сила 5)",
        "Броня         — $650   (+1 защита)",
        "Пропустить"
    ])
    if choice == 1:
        weapon = "Пистолет"
        print("Вы взяли пистолет.")
    elif choice == 2:
        if money >= 1200:
            money -= 1200
            weapon = "SMG"
            print("Вы купили SMG.")
        else:
            print("Не хватает денег.")
    elif choice == 3:
        if money >= 2700:
            money -= 2700
            weapon = "Винтовка"
            print("Вы купили винтовку.")
        else:
            print("Не хватает денег.")
    elif choice == 4:
        if money >= 4750:
            money -= 4750
            weapon = "AWP"
            print("Вы купили AWP.")
        else:
            print("Не хватает денег.")
    elif choice == 5:
        if money >= 650:
            money -= 650
            armor = True
            print("Вы купили броню.")
        else:
            print("Не хватает денег.")
    else:
        print("Вы пропустили покупку.")
    return money, weapon, armor


def cs2_end_match(reason):
    print()
    print("=" * 60)
    print("МАТЧ ОКОНЧЕН")
    print("=" * 60)
    print(reason)
    print("Вы возвращаетесь в меню CS2...")
    time.sleep(2)
    return "cs2"


def cs2_explore_map(map_name, team):
    positions = [
        "Спавн",
        "Центр карты",
        "Длинный коридор",
        "Узкий проход",
        "Плац",
        "Точка А",
        "Точка Б",
        "Крыша",
        "Подвал",
        "Выход"
    ]
    total = len(positions)
    pos = 0
    hp = 100
    money = 800
    weapon = "Пистолет"
    armor = False
    kills = 0

    smoke = 0
    flash = 0
    defuse_kit = False

    has_bomb = (team == "Т")
    bomb_planted = False
    bomb_site = None
    bomb_timer = 0
    bomb_defused = False

    print()
    print("=" * 60)
    print(f"ВЫ НА КАРТЕ {map_name} ЗА {team}")
    print("=" * 60)
    if team == "Т":
        print("У вас есть бомба. Заложите её на точке А или Б.")
    else:
        print("Ваша задача — не дать Т заложить бомбу или разминировать её.")
    time.sleep(2)

    while pos < total and hp > 0:
        print()
        print(f"ТОЧКА: {positions[pos]}")
        cs2_show_hud(map_name, team, hp, money, weapon, armor, kills, pos + 1, total)
        print(f"  Гранаты: дымовая x{smoke}  |  флешка x{flash}  |  дефуз-кит: {'да' if defuse_kit else 'нет'}")

        if bomb_planted and not bomb_defused:
            print(f"  !!! БОМБА ЗАЛОЖЕНА НА ТОЧКЕ {bomb_site}. ДО ВЗРЫВА: {bomb_timer} ходов !!!")

        options = [
            "Идти дальше",
            "Осмотреться (найти лут)",
            "Купить оружие",
            "Перевязаться (+10 HP)"
        ]
        if team == "Т" and has_bomb and positions[pos] in ("Точка А", "Точка Б") and not bomb_planted:
            options.append("Заложить бомбу")
        if team == "КТ" and bomb_planted and not bomb_defused and positions[pos] == f"Точка {bomb_site}":
            options.append("Разминировать бомбу")
        choose = menu(options)

        if choose == 3:
            money, weapon, armor = cs2_buy_menu(money, weapon, armor)
            continue

        if choose == 4:
            hp += 10
            if hp > 100:
                hp = 100
            print("Вы перевязались и восстановили 10 HP.")
            if bomb_planted and not bomb_defused:
                bomb_timer -= 1
                if bomb_timer <= 0:
                    return cs2_end_match("БОМБА ВЗОРВАЛАСЬ! Т побеждают.")
            continue

        if choose == 2:
            r = random.randint(1, 5)
            if r == 1:
                print("Вы нашли $300.")
                money += 300
            elif r == 2:
                print("Вы нашли дымовую гранату!")
                smoke += 1
            elif r == 3:
                print("Вы нашли флешку!")
                flash += 1
            elif r == 4:
                print("Вы нашли броню!")
                armor = True
            elif r == 5 and team == "КТ":
                print("Вы нашли дефуз-кит!")
                defuse_kit = True
            else:
                print("Ничего не нашли.")
            if bomb_planted and not bomb_defused:
                bomb_timer -= 1
                if bomb_timer <= 0:
                    return cs2_end_match("БОМБА ВЗОРВАЛАСЬ! Т побеждают.")
            continue

        if choose == 5 and team == "Т" and has_bomb and positions[pos] in ("Точка А", "Точка Б") and not bomb_planted:
            bomb_planted = True
            bomb_site = "А" if positions[pos] == "Точка А" else "Б"
            bomb_timer = 5
            print(f"Вы заложили бомбу на точке {bomb_site}! У КТ есть 5 ходов, чтобы её разминировать.")
            continue

        if choose == 5 and team == "КТ" and bomb_planted and not bomb_defused and positions[pos] == f"Точка {bomb_site}":
            chance = 75 if defuse_kit else 50
            if random.randint(1, 100) <= chance:
                bomb_defused = True
                return cs2_end_match("Вы успешно разминировали бомбу! КТ побеждают.")
            else:
                print("Вы пытались разминировать, но не успели. Попробуйте ещё раз.")
                bomb_timer -= 1
                if bomb_timer <= 0:
                    return cs2_end_match("БОМБА ВЗОРВАЛАСЬ! Т побеждают.")
                continue

        event = random.randint(1, 6)
        if event == 1:
            print("Вы встретили врага!")
            enemy_hp = random.randint(30, 80)
            enemy_power = random.randint(1, 5)
            your_power = cs2_weapons[weapon] + (1 if armor else 0)
            print(f"Враг: HP {enemy_hp}, сила {enemy_power}  |  Ваша сила: {your_power}")
            if flash > 0:
                use_flash = menu([
                    "Использовать флешку",
                    "Не использовать"
                ])
                if use_flash == 1:
                    flash -= 1
                    enemy_power = max(1, enemy_power - 2)
                    print("Вы кинули флешку! Враг оглушён, его сила снижена.")
            if smoke > 0:
                use_smoke = menu([
                    "Кинуть дым и уйти от боя",
                    "Остаться в бою"
                ])
                if use_smoke == 1:
                    smoke -= 1
                    print("Вы кинули дым и ушли от боя.")
                    pos += 1
                    continue
            while enemy_hp > 0 and hp > 0:
                time.sleep(1)
                if random.randint(1, 10) <= your_power * 2:
                    dmg = random.randint(15, 35)
                    enemy_hp -= dmg
                    print(f"Вы попали во врага на {dmg}. HP врага: {max(enemy_hp, 0)}")
                else:
                    print("Вы промахнулись.")
                if enemy_hp <= 0:
                    break
                if random.randint(1, 10) <= enemy_power * 2:
                    dmg = random.randint(10, 30)
                    if armor and random.randint(1, 2) == 1:
                        print("Броня поглотила часть урона.")
                        dmg //= 2
                    hp -= dmg
                    print(f"Враг попал в вас на {dmg}. Ваше HP: {max(hp, 0)}")
                else:
                    print("Враг промахнулся.")
            if hp <= 0:
                return cs2_end_match("Вы погибли в бою.")
            else:
                kills += 1
                money += 300
                print(f"Вы убили врага! Всего убийств: {kills}")
        elif event == 2:
            print("Вы встретили союзника. Он дал вам $200.")
            money += 200
        elif event == 3:
            print("Вы нашли лут: дымовую гранату.")
            smoke += 1
        elif event == 4:
            print("Вы нашли патроны. Оружие стало немного сильнее (мысленно).")
        elif event == 5:
            print("Пусто. Тишина.")
        else:
            print("Вы услышали шаги вдали, но никого не увидели.")

        if bomb_planted and not bomb_defused:
            bomb_timer -= 1
            if bomb_timer <= 0:
                return cs2_end_match("БОМБА ВЗОРВАЛАСЬ! Т побеждают.")

        pos += 1
        time.sleep(1)

    if hp <= 0:
        return cs2_end_match("Вы погибли.")

    result = f"Убийств: {kills}  |  Осталось HP: {hp}  |  Денег: ${money}\n"
    if bomb_planted and not bomb_defused:
        result += "Бомба была заложена, но не взорвалась и не была разминирована. Концовка: Ничья."
    elif team == "Т" and bomb_defused:
        result += "Бомбу разминировали. Концовка: Поражение Т."
    elif team == "КТ" and bomb_planted and not bomb_defused:
        result += "Бомба не была разминирована. Концовка: Победа Т."
    elif kills >= 3:
        result += "Концовка: Вы зачистили карту и стали MVP."
    elif kills >= 1:
        result += "Концовка: Вы выжили на карте."
    else:
        result += "Концовка: Вы прошли карту, не встретив врагов. Скучно."
    return cs2_end_match(result)


def location_cs2():
    global life, location
    print()
    print("=" * 60)
    print("CS2")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Играть оффлайн",
        "Играть онлайн",
        "Выйти"
    ])
    if choose == 1:
        return "offline"
    elif choose == 2:
        return "online"
    elif choose == 3:
        print("Вы вышли из CS2...")
        time.sleep(1)
        return "ecran_pk"
    return "cs2"


def location_offline():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ОФФЛАЙН")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Играть за Т",
        "Играть за КТ",
        "Выйти"
    ])
    if choose == 1:
        return "off_t"
    elif choose == 2:
        return "off_kt"
    elif choose == 3:
        print("Вы вышли в CS2...")
        time.sleep(1)
        return "cs2"
    return "offline"


def location_off_t():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ОФФЛАЙН ЗА Т")
    print("=" * 60)
    time.sleep(1)
    print("Вы играете за Т...")
    time.sleep(1)
    map_choice = menu([
        "Mirage",
        "Dust2",
        "Inferno"
    ])
    maps = {1: "Mirage", 2: "Dust2", 3: "Inferno"}
    return cs2_explore_map(maps[map_choice], "Т")


def location_off_kt():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ОФФЛАЙН ЗА КТ")
    print("=" * 60)
    time.sleep(1)
    print("Вы играете за КТ...")
    time.sleep(1)
    map_choice = menu([
        "Mirage",
        "Dust2",
        "Inferno"
    ])
    maps = {1: "Mirage", 2: "Dust2", 3: "Inferno"}
    return cs2_explore_map(maps[map_choice], "КТ")


def location_online():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ОНЛАЙН")
    print("=" * 60)
    time.sleep(1)
    print("Поиск матча...")
    time.sleep(2)
    print("Матч найден!")
    time.sleep(1)
    map_choice = menu([
        "Mirage",
        "Dust2",
        "Inferno"
    ])
    maps = {1: "Mirage", 2: "Dust2", 3: "Inferno"}
    team = random.choice(["Т", "КТ"])
    print(f"Вы играете за {team}.")
    time.sleep(1)
    return cs2_explore_map(maps[map_choice], team)


def location_higth_n():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ВЫСШИЙ НОВГОРОД")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Призвать Котость",
        "Остаться жить (концовка)",
        "Прыгнуть обратно в город",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        print("Вы призвали Котость!")
        time.sleep(2)
        print("Котость смотрит на вас и говорит: 'Мяу'.")
        time.sleep(2)
        print("Вы стали котом. Концовка: Котость.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 2:
        print("Вы остались жить в Высшем Новгороде. Концовка: Жизнь в Высшем Новгороде.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 3:
        print("Вы прыгнули обратно в город...")
        time.sleep(1)
        return "town"
    elif choose == 4:
        show_inventory(inventory)
        return "higth_n"
    return "higth_n"


def location_back_chekyshie():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ЗАЧЕКУШЬЕ")
    print("=" * 60)
    time.sleep(1)
    choose = menu([
        "Пить чекушки (концовка - ты спился)",
        "Смириться (концовка - смерть)",
        "Искать хаммамную комнату (хорошая концовка, если нашёл)",
        "Посмотреть инвентарь"
    ])
    if choose == 1:
        print("Вы начали пить чекушки...")
        time.sleep(2)
        print("Вы спились. Концовка: Спился.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 2:
        print("Вы смирились со своей участью...")
        time.sleep(2)
        print("Вы умерли. Концовка: Смерть.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"
    elif choose == 3:
        r = random.randint(1, 2)
        if r == 1:
            print("Вы нашли хаммамную комнату!")
            time.sleep(2)
            print("Вы отдохнули в хаммаме. Концовка: Хаммам.")
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"
        else:
            print("Вы не нашли хаммамную комнату...")
            time.sleep(2)
            print("Вы продолжили скитаться. Концовка: Скитания.")
            print()
            print("=" * 60)
            print("ИГРА ОКОНЧЕНА")
            print("=" * 60)
            life = False
            return "end"
    elif choose == 4:
        show_inventory(inventory)
        return "back_chekyshie"
    return "back_chekyshie"


def location_Alab_P():
    global life, location, inventory, found_AP, have_AP_ticket
    print()
    print("=" * 60)
    print("АЛАБУГА ПОЛИТЕХ")
    print("=" * 60)
    time.sleep(1)
    print("Вы в Алабуга Политехе. Воздух здесь... странный. Знания витают в воздухе.")
    choose = menu([
        "Учиться",
        "Уволиться",
        "Спрыгнуть из окна из Политеха",
        "Посмотреть инвентарь"
    ])

    if choose == 1:
        print("Вы начали учиться...")
        time.sleep(2)
        print("Вы получаете знания, которые не поддаются описанию.")
        time.sleep(2)
        print("Ваш разум расширяется. Вы понимаете то, что не должен понимать человек.")
        time.sleep(3)
        print("Концовка: Знания Алабуга Политеха.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"

    elif choose == 2:
        print("Вы уволились из Алабуга Политеха...")
        time.sleep(1)
        for item in inventory:
            if item[0] == "Билет в Алабуга Политех":
                inventory.remove(item)
                break
        have_AP_ticket = False
        found_AP = False
        print("Вы вернулись в город.")
        return "town"

    elif choose == 3:
        print("Вы подошли к окну и прыгнули...")
        time.sleep(2)
        print("Полёт был недолгим. Концовка: Прыжок из Алабуга Политеха.")
        print()
        print("=" * 60)
        print("ИГРА ОКОНЧЕНА")
        print("=" * 60)
        life = False
        return "end"

    elif choose == 4:
        show_inventory(inventory)
        return "Alab_P"

    return "Alab_P"



found_AP = False
have_AP_ticket = False
deth_babke = False
have_phone = False
found_light = False
location = "basement"
tapochki = False
cherdak_key = False
found_patapim_key = False
found_car_key = False
vent = False
see_car = False
found_caboom = False
uran_candies = False


while life:
    if location == "basement":
        location = location_basement()
    elif location == "house_hall":
        location = location_house_hall()
    elif location == "mogila":
        location = location_mogila()
    elif location == "stairs_1_floor":
        location = location_stairs_1_floor()
    elif location == "stairs_2_floor":
        location = location_stairs_2_floor()
    elif location == "Patapim_room":
        location = location_Patapim_room()
    elif location == "kitchen":
        location = location_kitchen()
    elif location == "prihozhaya":
        location = location_prihozhaya()
    elif location == "cherdak":
        location = location_cherdak()
    elif location == "street_next_to_house":
        location = location_street_next_to_house()
    elif location == "next_to_car":
        location = location_next_to_car()
    elif location == "car_seat":
        location = location_car_seat()
    elif location == "town":
        location = location_town()
    elif location == "work_dvornik":
        location = location_work_dvornik()
    elif location == "work_prodavec":
        location = location_work_prodavec()
    elif location == "selo_molochnoe":
        location = location_selo_molochnoe()
    elif location == "shopping_centre":
        location = location_shopping_centre()
    elif location == "svetofor":
        location = location_svetofor()
    elif location == "aviasales":
        location = location_aviasales()
    elif location == "airplane":
        location = location_airplane()
    elif location == "pole_chudes":
        location = location_pole_chudes()
    elif location == "cinema":
        location = location_cinema()
    elif location == "pk_shop":
        location = location_pk_shop()
    elif location == "ecran_pk":
        location = location_ecran_pk()
    elif location == "minecraft":
        location = location_minecraft()
    elif location == "saper":
        location = location_saper()
    elif location == "cs2":
        location = location_cs2()
    elif location == "offline":
        location = location_offline()
    elif location == "off_t":
        location = location_off_t()
    elif location == "off_kt":
        location = location_off_kt()
    elif location == "online":
        location = location_online()
    elif location == "higth_n":
        location = location_higth_n()
    elif location == "back_chekyshie":
        location = location_back_chekyshie()
    elif location == "Alab_P":
        location = location_Alab_P()
    elif location == "end":
        break
