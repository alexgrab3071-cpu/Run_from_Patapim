import random
import time
from end_pictures import *
from general_defs import *



print(
    "После тусы вы с вашими друзьями ехали на такси в сторону дома. Из-за пьянки\nвы не помните, точно ли доехали до дома. У вас ноет тело и сильно хочется спать, вы приоткрываете глаза\nи вместо привычной кровати видите темный подвал с гнилыми продуктами\nтеперь ваша цель покинуть это загадочное место.")
time.sleep(5)

inventory = [
    ["Здоровье", 100],
    ["Деньги", 0]
]

life = True
find_key = False
escaped_basement = False


def location_basement():
    global life, find_key, escaped_basement, inventory
    if not escaped_basement:
        print_menu([
            "1. Еще поспать, мало-ли это кошмар?",
            "2. Осмотреться, может, что-то будет видно?" if not find_key else "2. (уже осмотрено)",
            "3. Позвать на помощь, а то подвал закрыт",
            "4. Постараться выбраться"
        ])

        thirst_choose = safe_input("Ваш выбор (цифра 1-4): ", range(1, 5))

        if thirst_choose == 1:
            print("\nЕще поспать.")
            time.sleep(1)
            print("Вы постарались уснуть, но проснулись уже в мясной лавке светофора...")
            time.sleep(1)
            print("Видимо, терять контроль над происходящим было ошибкой...")
            time.sleep(1)
            print(end_pictures["Мясная лавка Светофора"])
            print("\nИГРА ОКОНЧЕНА")
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
                            time.sleep(0.5)
                            if die >= 100:
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
                            "...........................................................................\n.................................@@@@@@@...................................\n...............................@@@@@@@@@@@.................................\n..............................@@@@@@@@@@@@@................................\n..............................############.................................\n.............................##############................................\n.............................##############................................\n.............................##############................................\n..............................############.................................\n...............................##########..................................\n......................//////////########//////////.........................\n...................////////////##########////////////......................\n.................////////////############////////////......................\n...............#############/############/#############....................\n..............##############/############/##############...................\n.............###############/############/###############..................\n............################/############/################.................\n............################/############/################.................\n............################/############/################.................\n............################/############/.................................\n............################/############/.................................\n............################/############/.................................\n.............###############/############/.................................\n..............##############/############/.................................\n...............#############/############/.................................\n.................///////////############/..................................\n...........................##############..................................\n..........................%%%%%%%%%%%%%%%%.................................\n.........................%%%%%%%%%%%%%%%%%%................................\n........................%%%%%%%%%%%%%%%%%%%%...............................\n........................%%%%%%%%%%%%%%%%%%%%...............................\n........................%%%%%%        %%%%%%...............................\n........................%%%%%          %%%%%...............................\n........................%%%%            %%%%...............................\n........................###              ###...............................\n........................###              ###...............................\n........................###              ###...............................\n.......................####              ####..............................\n.......................####              ####..............................\n.......................####              ####..............................\n......................#####              #####.............................\n......................#####              #####.............................\n.....................######              ######............................\n....................#######              #######...........................\n...................########              ########..........................\n..................#########              #########.........................\n..................#########              #########.........................\n...................#######                #######..........................\n.....................###                    ###............................\n...........................................................................")
                        while life and hot < 100:
                            hot += 1
                            print(f"Вам жарко в хаммаме на {hot}%")
                            time.sleep(0.5)
                            if hot >= 100:
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
            time.sleep(1)
            print("Но это было последнее, о чем вы думаете...")
            time.sleep(2)
            print(end_pictures["Обед Патапима"])
            print("\nИГРА ОКОНЧЕНА")
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
        print("\n" + "=" * 50)
        print("После выхода в холл поместья ваши глаза ничего не различают")
        time.sleep(1)
        print("Ориентироваться можно только на ощупь...")
        print("=" * 50)
        time.sleep(1)
        print_menu([
            "1. Пойти вперед, постараться найти что-то на ощупь...",
            "2. Искать предметы на ощупь...",
            "3. Посмотреть инвентарь..."
        ])
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
                print_menu([
                    "1. Взять фонарик, забыв про рубильник",
                    "2. Дернуть рычаг рубильника, проверить, что случится"
                ])
                choose_1 = safe_input("Ваш выбор: ", range(1, 3))

                if choose_1 == 1:
                    print("Отлично, теперь хоть что-то видно!")
                    inventory.append(["Рабочий фонарик", 1])
                    found_light = True
                    return "house_hall"

                elif choose_1 == 2:
                    time.sleep(1)
                    print(
                        "Вы включили свет... Яркая вспышка ослепила вас, и вы нашли себя очнувшимся уже в мясной лавке Светофора...")
                    return "mogila"

            else:
                print("Пока что глаза не привыкли...")
                time.sleep(1.5)
                return "house_hall"

        elif choose == 3:
            show_inventory(inventory)
            return "house_hall"

    if found_light:
        print("\n" + "=" * 50)
        print("Вы находитесь в холле, с фонариком. Теперь все пути видно, куда пойдете?")
        print("=" * 50)
        time.sleep(1)
        print_menu([
            "1. Направо, к лестнице",
            "2. Налево, на кухню",
            "3. Вперед, к прихожей",
            "4. Посмотреть инвентарь..."
        ])
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
    print("F " * 100)
    life = False
    return "end"

def location_stairs_1_floor():
    time.sleep(1)
    print("Вы слышите, как кто-то храпит на втором этаже...")
    time.sleep(1)
    print("1. Остаться на первом этаже, пойти в холл...")
    print("2. Пойти по лестнице на второй этаж...")
    choose = safe_input("Ваш выбор: ", range(1, 3))
    if choose == 1:
        time.sleep(1)
        print("Вы отходите от лестницы и приходите в холл...")
        return "house_hall"
    if choose == 2:
        print("Вы решаетесь подняться на второй этаж на храп...")
        time.sleep(1)
        return "stairs_2_floor"
    return "stairs_1_floor"

def location_stairs_2_floor():
    global cherdak_key, found_patapim_key, tapochki, inventory
    time.sleep(1)
    print("Вы находитесь на втором этаже, перед вами 2 двери, из левой слышен храп а правая закрыта на замок")
    time.sleep(2)
    print("1. Открыть правую дверь...")
    print("2. Пойти в левую дверь, на храп...")
    print("3. Пойти назад, на первый этаж...")
    print("4. Посмотреть инвентарь...")
    choose = safe_input("Ваш выбор: ", range(1, 5))
    if choose == 1 and cherdak_key == False:
        time.sleep(1)
        print("К сожлению, дверь не поддается, тут нужен специальный ключ...")
        return "stairs_2_floor"
    if choose == 1 and cherdak_key == True:
        time.sleep(1)
        print("Замок удачно щелкает, путь на чердак открыт!")
        return "cherdak"
    if choose == 2:
        time.sleep(1)
        print("Вы продвигаетесь к левой комнате, звуки храпа усиливаются...")
        time.sleep(1)
        return "Patapim_room"
    if choose == 3:
        print("Вы спускаетесь обратно на первый этаж...")
        time.sleep(1)
        return "stairs_1_floor"
    if choose == 4:
        show_inventory(inventory)
        return "stairs_2_floor"
    return "stairs_2_floor"

def location_Patapim_room():
    global found_patapim_key, tapochki, inventory, life
    time.sleep(1)
    print("Перед вами лежит огромное существо из знаменитой группы ИИподобной mozgognil...")
    time.sleep(1)
    print("1. Выйти обратно в холл этажа 2...")
    if not found_patapim_key:
        print("2. Постараться забрать странные ключи на тумбочке Бр-бр Патапима (вы их увидели)...")
    else:
        print("2. (Уже забрано)")
    print("3. Напасть на Бр-бр Патапима...")
    print("4. Посмотреть инвентарь...")
    choose = safe_input("Ваш выбор: ", range(1, 5))
    if choose == 1:
        print("Вы вышли...")
        time.sleep(1)
        return "stairs_2_floor"
    if found_patapim_key == False:
        if choose == 2 and tapochki == False:
            print("Это была хорошая попытка пройти мимо mozgognil, но Mozhognil раздавило вас своей ногой...")
            print(end_pictures["Мясная лавка Светофора"])
            return "mogila"
        if choose == 2 and tapochki == True:
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
    time.sleep(1)
    print("Вы проходите по корридору в сторону кухни.")
    time.sleep(1)
    print("1. Проверить ящики с едой")
    if not found_car_key:
        print("2. Проверить ящики с не едой")
    else:
        print("2. (Уже изрыто)")
    print("3. Подойти к столу")
    print("4. Уйти обратно в холл этажа 1")
    print("5. Посмотреть инвентарь")
    choose = safe_input("Ваш выбор: ", range(1, 6))
    if choose == 1:
        r = random.randint(1, 2)
        if r == 1:
            print("В ящике вы ничего не нашли, там кучу хлама, но может, есть что-то еще?")
            time.sleep(1)
        if r == 2:
            print("Вам удалось найти в ящике что-то.. это были урановые конфетки, они добавились в ваш инвентарь.")
            if ["Урановые конфетки", 1] not in inventory:
                inventory.append(["Урановые конфетки", 1])
                uran_candies = True
            time.sleep(1)
        return "kitchen"
    if choose == 2 and not found_car_key:
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
    if choose == 3:
        time.sleep(1)
        print("Подойдя к столу, вы заметили гараж, который стоял слева от выходной двери. Теперь вы знаете, что есть гараж слева от выхода")
        see_car = True
        return "kitchen"
    if choose == 4:
        time.sleep(1)
        print("Вы ушлив холл")
        return "house_hall"
    if choose == 5:
        time.sleep(1)
        show_inventory(inventory)
        return "kitchen"
    return "kitchen"

def location_prihozhaya():
    global vent, cherdak_key, tapochki, inventory, found_patapim_key
    print("Вы идете в сторону прихожей...")
    time.sleep(1)
    print("Вы замечате маленькую вентиляцию около двери...")
    time.sleep(1)
    if not vent:
        print("1. Полезть в вентиляцию")
    else:
        print("1. Вы уже лазали в вентиляцию.")
    print("2. Открыть выходную дверь")
    print("3. Вернуться обратно в холл")
    print("4. Посмотреть инвентарь")
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
    if choose == 2:
        if not found_patapim_key:
            print("Дверь не поддается, наверняка есть какой-то ключ...")
            time.sleep(1)
            return "prihozhaya"
        else:
            print("Дверь успешно открылась, вы вышли на улицу.")
            return "street_next_to_house"
    if choose == 3:
        print("Вы идете в холл")
        time.sleep(1)
        return "house_hall"
    if choose == 4:
        show_inventory(inventory)
        return "prihozhaya"
    return "prihozhaya"

def location_cherdak():
    global found_caboom
    print("Вы поднимаетесь на чердак...")
    time.sleep(2)
    print("Вы чувствуете, как что-то меняется в воздухе...")
    time.sleep(2)
    print("Поднимаясь, ви видите ядерное оружие, которое лежит на гнилых досках Mozgognil(-и).")
    found_caboom = True
    time.sleep(2)
    print("Может, можно как-то отвезти оружие, после чего взорвать?")
    time.sleep(2)
    print("На полу вы находите записку:")
    s = "Как уничтожить Mozgognil: сначала нужно получить доступ к секретному орудию, потом собрать урановые вещества...\n Дальше нужно увезти орудие на машине и запустить в Mozgognil."
    for i in s:
        print(i, end="")
    time.sleep(2)
    print("\nВы спускаетесь на второй этаж...")
    return "stairs_2_floor"

def location_street_next_to_house():
    global see_car, life
    print("Вы выбираетесь на улицу, вместо привычной деревни/города вы выдите темный лес и только лишь дорога выделяется на фоне мрака.")
    time.sleep(3)
    print("1. Пойти вперед, к дороге")
    print("2. Уйти обратно в холл")
    if see_car:
        print("3. Повернуть налево, к машине")
    else:
        print("3. (ЗАКРЫТО, МОЖНО ОТКРЫТЬ НА ЛОКАЦИЯХ)")
    print("4. Посмотреть инвентарь")
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
        print("1. Уйти обратно, на дорогу")
        print("2. Зайти в разлом реальности")
        choose = safe_input("Ваш выбор: ", range(1, 3))
        if choose == 1:
            print("Вы пытаетесь найти дорогу назад, но умираете от голода и жажды в вечных поисках")
            return "mogila"
        if choose == 2:
            print("Вы попадаете в... вы попадаете в сон спящего Mozgognil.")
            time.sleep(1)
            print("Он вас съедает")
            print(end_pictures["Тролол"])
            return "mogila"
    if choose == 2:
        print("Вы идете в прихожую...")
        time.sleep(1)
        return "prihozhaya"
    if choose == 3 and see_car:
        print("Вы идете к машине, подходите к ней...")
        time.sleep(1)
        return "next_to_car"
    if choose == 3 and not see_car:
        print("Так нечестно!")
        time.sleep(1)
        return "street_next_to_house"
    if choose == 4:
        show_inventory(inventory)
        return "street_next_to_house"
    return "street_next_to_house"

def location_next_to_car():
    global found_car_key
    print("Вы подходите к машине, на машине есть огромный кузов, может, попробовать уехать?")
    time.sleep(2)
    print("1. Попробовать открыть машину...")
    print("2. Уйти обратно в выходу из дома...")
    print("3. Посмотреть инвентарь...")
    choose = safe_input("Ваш выбор: ", range(1, 4))
    if choose == 1 and found_car_key:
        print("С помощью ключа вы открываете дверь машины и садитесь за руль")
        return "car_seat"
    if choose == 1 and not found_car_key:
        print("Вы попытались открыть дверь, но она не поддалась - нужны ключи.")
        return "next_to_car"
    if choose == 2:
        print("Вы возвращаетесь к выходу из дома...")
        time.sleep(1)
        return "street_next_to_house"
    if choose == 3:
        show_inventory(inventory)
        return "next_to_car"
    return "next_to_car"

def location_car_seat():
    global found_caboom, uran_candies, life
    print("Вам знакома эта машина, это популярная марка Baobabys, теперь вы в машине")
    time.sleep(2)
    print("1. Уехать по шоссе в город")
    if found_caboom and uran_candies:
        print("2. Исполнить план по изъятию ядерного оружия...")
    else:
        print("2. |ЗАКРЫТО|")
    print("3. Выйти обратно во двор")
    print("4. Посмотреть инвентарь")
    choose = safe_input("Ваш выбор: ", range(1, 5))
    if choose == 1:
        print("Вы уехали в город, начало расцветать, вы узнавали Москву все лучше, часть 1 закончилась...")
        print("\nКонец части 1 (хорошая концовка)")
        life = False
        return "end"
    if choose == 2 and found_caboom and uran_candies:
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
        print("\nКонец игры (хорошая концовка)")
        life = False
        return "end"
    if choose == 3:
        print("Вы вышли в гараж")
        time.sleep(1)
        return "street_next_to_house"
    if choose == 4:
        show_inventory(inventory)
        return "car_seat"
    return "car_seat"

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
    elif location == "end":
        break

