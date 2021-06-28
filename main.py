def check_win(field, char):
    return any(
        [
            check_rows(field, char),
            check_columns(field, char),
            check_diagonals(field, char),
        ]
    )


def check_rows(field, char):
    return any(all(c == char for c in row) for row in field)


def check_columns(field, char):
    return any(all(c == char for c in row) for row in zip(*field))


def check_diagonals(field, char):
    return any(
        [
            all(field[i][i] == char for i in range(len(field))),
            all(field[i][len(field[0]) - i - 1] == char for i in range(len(field))),
        ]
    )


def print_field(field):
    width = len(field[0])
    print_row(" ", map(str, range(width)))
    print(f"--+{'--' * width}")
    for index, row in enumerate(field):
        print_row(index, row)


def print_row(name, row):
    print(f"{name} | {' '.join(row)}")


def choose_cell(field, width, height):
    while True:
        x, y = map(
            int,
            input("Пожалуйста введите номер строки и номер столбца через пробел: ")
            .strip()
            .split(),
        )
        if not (0 <= x < width and 0 <= y < height):
            print("Эта клетка выходит за пределы поля.")
            continue
        if field[x][y] != ".":
            print("Эта клетка занята.")
            continue
        return x, y


def main():
    players = []
    players.append(input("Введите имя первого игрока (крестики): "))
    players.append(input("Введите имя второго игрока (нолики): "))
    players_chars = ["x", "o"]
    active_player = 0

    field = [["." for j in range(3)] for i in range(3)]
    print_field(field)

    for i in range(3 * 3):
        print(f"Ход игрока {players[active_player]}!")
        x, y = choose_cell(field, 3, 3)
        field[x][y] = players_chars[active_player]
        print_field(field)
        if check_win(field, players_chars[active_player]):
            print(f"Игрок {players[active_player]} победил!")
            break
        active_player ^= 1
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()
