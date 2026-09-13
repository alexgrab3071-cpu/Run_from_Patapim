import random
import time
from end_pictures import *
from general_defs import *


print("Ссылка на GitHub: https://github.com/alexgrab3071-cpu/Run_from_Patapim.git")
print()
print("=" * 60)
print("ПОБЕГ ИЗ ПАТАПИМА")
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


# ============================================================
# ПОДВАЛ И ДОМ
# ============================================================

def location_basement():
    global life, find_key, escaped_basement, inventory
    if not escaped_basement:
        print()
        print("=" * 60)
        print("ТЁМНЫЙ ПОДВАЛ")
        print("=" * 60)
        line()
        print("1. Еще поспать, мало-ли это кошмар?")
        print("2. Осмотреться, может, что-то будет видно?" if not find_key else "2. (уже осмотрено)")
        print("3. Позвать на помощь, а то подвал закрыт")
        print("4. Постараться выбраться")
        line()

        thirst_choose = safe_input("Ваш выбор (1-4): ", range(1, 5))

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
        line()
        print("1. Пойти вперед, постараться найти что-то на ощупь...")
        print("2. Искать предметы на ощупь...")
        print("3. Посмотреть инвентарь...")
        line()
        choose = safe_input("Ваш выбор: ", range(1, 4))

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
                line()
                print("1. Взять фонарик, забыв про рубильник")
                print("2. Дернуть рычаг рубильника, проверить, что случится")
                line()
                choose_1 = safe_input("Ваш выбор: ", range(1, 3))
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
        line()
        print("1. Направо, к лестнице")
        print("2. Налево, на кухню")
        print("3. Вперед, к прихожей")
        print("4. Посмотреть инвентарь...")
        line()
        choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Остаться на первом этаже, пойти в холл...")
    print("2. Пойти по лестнице на второй этаж...")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 3))
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
    line()
    print("1. Открыть правую дверь...")
    print("2. Пойти в левую дверь, на храп...")
    print("3. Пойти назад, на первый этаж...")
    print("4. Посмотреть инвентарь...")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Выйти обратно в холл этажа 2...")
    if not found_patapim_key:
        print("2. Постараться забрать странные ключи на тумбочке Бр-бр Патапима (вы их увидели)...")
    else:
        print("2. (Уже забрано)")
    print("3. Напасть на Бр-бр Патапима...")
    print("4. Посмотреть инвентарь...")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Проверить ящики с едой")
    if not found_car_key:
        print("2. Проверить ящики с не едой")
    else:
        print("2. (Уже изрыто)")
    print("3. Подойти к столу")
    print("4. Уйти обратно в холл этажа 1")
    print("5. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 6))
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
    line()
    if not vent:
        print("1. Полезть в вентиляцию")
    else:
        print("1. Вы уже лазали в вентиляцию.")
    print("2. Открыть выходную дверь")
    print("3. Вернуться обратно в холл")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Пойти вперед, к дороге")
    print("2. Уйти обратно в холл")
    if see_car:
        print("3. Повернуть налево, к машине")
    else:
        print("3. (ЗАКРЫТО, МОЖНО ОТКРЫТЬ НА ЛОКАЦИЯХ)")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор : ", range(1, 5))
    if choose == 1:
        print("Перед вами калитка. Вы открываете ее и выходите на дорогу.")
        time.sleep(1)
        print("Как бы долго вы не шли, вы все равно приходите туда же, будучи в депрессии, вы решаете пойти не\n по дороге, а в лес")
        time.sleep(3)
        print("Там все деревья темные, но вскоре вы выходите на поляну, где виднеется что-то странное.")
        time.sleep(2)
        print("Вам кажется, будто в N-ном месте воздух искажается...")
        time.sleep(2)
        line()
        print("1. Уйти обратно, на дорогу")
        print("2. Зайти в разлом реальности")
        line()
        choose = safe_input("Ваш выбор: ", range(1, 3))
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
    line()
    print("1. Попробовать открыть машину...")
    print("2. Уйти обратно к выходу из дома...")
    print("3. Посмотреть инвентарь...")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Уехать по шоссе в город")
    if found_caboom and uran_candies:
        print("2. Исполнить план по изъятию ядерного оружия...")
    else:
        print("2. |ЗАКРЫТО|")
    print("3. Выйти обратно во двор")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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


# ============================================================
# ГОРОД И РАБОТА
# ============================================================

def location_town():
    global life, have_phone, location, inventory, deth_babke
    print()
    print("=" * 60)
    print("ГОРОД")
    print("=" * 60)
    time.sleep(1)
    print("Вы приехали в город, доступные выборы:")
    line()
    print("1. Искать работу")
    print("2. Пойти в ТЦ")
    print("3. Попрошайничать")
    print("4. Пойти на автобусную остановку")
    print("5. Пойти в метро")
    print("6. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 7))

    if choose == 1:
        if not have_phone:
            print("У вас не было телефона, чтобы поискать работу, у вас выбор: Идти дворником / Идти продавцом Moggнита.")
            time.sleep(1)
            line()
            print("1. Устроиться на работу дворником.")
            print("2. Устроиться на работу продавцом")
            print("3. Ничего не делать, вернуться к выбору")
            line()
            sub_choose = safe_input("Ваш выбор: ", range(1, 4))
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
        line()
        if not deth_babke:
            print("1. Избить бабку")
        else:
            print("1. Хз, побейте труп...")
        print("2. Ждать автобус")
        print("3. Уйти в город")
        line()
        sub_choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Работать")
    print("2. Работать")
    print("3. Бросить работу")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Пойти на кассу, принять товары")
    print("2. Уйти.")
    print("3. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
        line()
        print("1. Оплатить")
        line()
        choose = safe_input("Ваш выбор: ", range(1, 2))
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
    line()
    print("1. Прогуляться по селу")
    print("2. Пойти в лес")
    if have_AP_ticket:
        print("3. Пойти в Алабуга Политех")
        print("4. Уехать из села в город")
        print("5. Посмотреть инвентарь")
    else:
        print("3. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 6 if have_AP_ticket else 4))

    if choose == 1:
        print("Вы решили прогуляться, вы заметили паука вдали, он был примерно 35 метров в высоту")
        time.sleep(1)
        line()
        print("1. Напасть на него")
        print("2. Спросить у него, нет ли ничего прикольного")
        print("3. Посмотреть инвентарь")
        line()
        sub_choose = safe_input("Ваш выбор: ", range(1, 4))
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

# ============================================================
# НОВЫЕ ЛОКАЦИИ
# ============================================================

def location_shopping_centre():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ТОРГОВЫЙ ЦЕНТР")
    print("=" * 60)
    time.sleep(1)
    line()
    print("1. Уйти в город")
    print("2. Пойти в Магазин Светофор")
    print("3. Пойти в Магазин Авиасейлс")
    print("4. Пойти в Кинотеатр")
    print("5. Пойти в ПК магазин")
    print("6. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 7))
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
    line()
    print("1. Купить мясо (если денег больше 100)")
    print("2. (двери закрыты)")
    print("3. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Купить билет (если денег больше 10 000)")
    print("2. Уйти в ТЦ")
    print("3. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Угадать слово")
    print("2. Уйти")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 3))
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
    line()
    print("1. Смешарики сквозь вселенные")
    print("2. Человек-паук")
    print("3. Колобок")
    print("4. Уйти")
    print("5. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 6))
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
    line()
    print("1. Купить сборку ПК (если денег больше 50 000)")
    print("2. Арендовать ПК на час (если денег больше 10 000)")
    print("3. Уйти")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Поиграть в Minecraft")
    print("2. Поиграть в Сапера")
    print("3. Поиграть в CS2")
    print("4. Выйти в город")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Новый мир")
    print("2. Выйти из игры")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 3))
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
    line()
    print("1. Играть")
    print("2. Выйти")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 3))
    if choose == 1:
        print("Вы играли в Сапёра. Молодцы!")
        time.sleep(2)
        return "ecran_pk"
    elif choose == 2:
        print("Вы вышли из Сапёра...")
        time.sleep(1)
        return "ecran_pk"
    return "saper"


def location_cs2():
    global life, location
    print()
    print("=" * 60)
    print("CS2")
    print("=" * 60)
    time.sleep(1)
    line()
    print("1. Играть оффлайн")
    print("2. Играть онлайн")
    print("3. Выйти")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    line()
    print("1. Играть за Т")
    print("2. Играть за КТ")
    print("3. Выйти")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 4))
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
    print("CS2 - ЗА Т")
    print("=" * 60)
    time.sleep(1)
    print("Вы играете за Т...")
    time.sleep(1)
    line()
    print("1. Выиграть")
    line()
    safe_input("Ваш выбор: ", range(1, 2))
    print("Вы выиграли! Молодцы.")
    time.sleep(1)
    return "cs2"


def location_off_kt():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ЗА КТ")
    print("=" * 60)
    time.sleep(1)
    print("Вы играете за КТ...")
    time.sleep(1)
    line()
    print("1. Выиграть")
    line()
    safe_input("Ваш выбор: ", range(1, 2))
    print("Вы выиграли! Молодцы.")
    time.sleep(1)
    return "cs2"


def location_online():
    global life, location
    print()
    print("=" * 60)
    print("CS2 - ОНЛАЙН")
    print("=" * 60)
    time.sleep(1)
    print("Мне было лень придумывать геймплей КС2, поэтому вы вернётесь в локацию КС...")
    time.sleep(2)
    return "cs2"


def location_higth_n():
    global life, location, inventory
    print()
    print("=" * 60)
    print("ВЫСШИЙ НОВГОРОД")
    print("=" * 60)
    time.sleep(1)
    line()
    print("1. Призвать Котость")
    print("2. Остаться жить (концовка)")
    print("3. Прыгнуть обратно в город")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Пить чекушки (концовка - ты спился)")
    print("2. Смириться (концовка - смерть)")
    print("3. Искать хаммамную комнату (хорошая концовка, если нашёл)")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))
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
    line()
    print("1. Учиться")
    print("2. Уволиться")
    print("3. Спрыгнуть из окна из Политеха")
    print("4. Посмотреть инвентарь")
    line()
    choose = safe_input("Ваш выбор: ", range(1, 5))

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
        # билет пропадает
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

# ============================================================
# ГЛАВНЫЙ ЦИКЛ
# ============================================================
found_AP = False
have_AP_ticket = False
deth_babke = False
have_phone = False
found_light = False
location = "town"
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
    elif location == "end":
        break
