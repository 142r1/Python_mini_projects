from collections import namedtuple, defaultdict
import time

Cell = namedtuple('Cell', ['x_cord', 'y_cord'])

def check_neighbor(cell):
    for x in range(cell.x_cord -1, cell.x_cord + 2):
        for y in range(cell.y_cord -1, cell.y_cord +2):
            if (x, y) != (cell.x_cord, cell.y_cord):
                yield Cell(x, y)

def count_neighbor(board):
    neighbor_count = defaultdict(int)
    for cell in board:
        for neighbor in check_neighbor(cell):
            neighbor_count[neighbor] += 1
    return neighbor_count

def make_board(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == 'X':
                board.add(Cell(int(col), int(row)))
    return board

def adv_board(board):
    new_board = set()
    for cell, count in count_neighbor(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board

def convert(board, pad=0):
    if not board:
        return "empty"
    str_board = ""
    xs = [x for (x, y) in board]
    ys = [y for (x, y) in board]
    for y in range(min(ys) -  pad, max(ys) + 1 + pad):
        for x in range(min(xs) - pad, max(xs) + 1 + pad):
            str_board += "X" if Cell(x, y) in board else "."
        str_board += "\n"
    return str_board.strip()

if __name__ == '__main__':
    f = make_board("...X..X.\nXX...X..\n....X..XX")
    for _ in range(3):
        f = adv_board(f)
        print("\033[2J\033[1;1H" + convert(f, 2))
        time.sleep(0.1)