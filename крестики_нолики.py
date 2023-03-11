desk=[[""] * 3 for i in range(3)]
def hello():
    print("<><><><><><><><><><><><>")
    print("ИГРА КРЕСТИКИ-НОЛИКИ")
    print("Привет новый игрок!!!")
    print("<><><><><><><><><><><><>")

    print("Правила игры!!!")
    print("<><><><><><><><><><><><>")
    print("Выигрывает тот кто собрал Х или О по столбцу,строке или диагонали")
    print("Ход осуществляется по координатам х и y")
    print("x-строки     y-столбцы")
    print("<><><><><><><><><><><><>")

    print("ПРИЯТНОЙ ИГРЫ!!!")
    print("<><><><><><><><><><><><>")


def koord():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  __________________")
    for i, row in enumerate(desk):
        row_inf = f"  {i} | {'  | '.join(map(str,row))}  | "
        print(row_inf)
        print("  __________________")
    print()



def ask():
    while True:
        cords = input("Ходите!!!: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if desk[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coord:
        symbols = []
        for c in cord:
            symbols.append(desk[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


hello()
desk = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    koord()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        desk[x][y] = "X"
    else:
        desk[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья!")
        break