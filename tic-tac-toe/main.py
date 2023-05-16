import keyboard
import os

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

current_pos = [1, 1]
turn = 1
key_pressed = False
signs = [' ', 'o', 'x']
moves = {
    'w': [0, -1],  # up
    's': [0, 1],  # down
    'a': [-1, 0],  # left
    'd': [1, 0],  # right
    'q': [0, 0]  # submit
}


def draw_board():
    os.system('cls')
    print()
    for i, row in enumerate(board):
        line = ' | '.join([f'({signs[cell]})' if current_pos == [j, i] else f' {signs[cell]} ' for j, cell in enumerate(row)])
        print(line)
        if i < len(board) - 1:
            print('----+-' * (len(row) - 1) + '----')


def make_move():
    global current_pos
    global turn

    curr_x, curr_y = current_pos
    key = get_key()
    if key is None:
        return 0
    move_x, move_y = moves[key][0], moves[key][1]
    keys = list(moves.keys())
    if 0 <= curr_x + move_x < len(board[0]) and 0 <= curr_y + move_y < len(board):
        current_pos = [curr_x + move_x, curr_y + move_y]

    if key == keys[4] and board[curr_y][curr_x] == 0:
        board[curr_y][curr_x] = turn
        turn = 1 if turn > 1 else 2
    draw_board()
    return check_winner()


def get_key():
    global key_pressed

    for key in moves.keys():
        if keyboard.is_pressed(key) and not key_pressed:
            key_pressed = True
            return key
        elif keyboard.is_pressed(key) and key_pressed:
            return None

    key_pressed = False
    return None


def check_winner():
    winning_combinations = [
        [[0, 0], [0, 1], [0, 2]],  # 00 01 02
        [[1, 0], [1, 1], [1, 2]],  # 10 11 12
        [[2, 0], [2, 1], [2, 2]],  # 20 21 22

        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],

        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]

    for line in winning_combinations:
        cells = [board[y][x] for x, y in line]
        if all(cell == cells[0] and cell != 0 for cell in cells):
            return cells[0]

    full = True
    for line in board:
        full = False if all(cell for cell in line)==0 else full

    if full:
        return 3
    return 0


def main():
    playing = True
    draw_board()
    win = 0
    while playing:
        win = make_move()
        if win > 0:
            playing = False

    print(f"{signs[win]} won") if win!=3 else print('Draw')


if __name__ == '__main__':
    main()

