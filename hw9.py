# Напишите класс TicTacToeBoard для игры в
# крестики-нолики, который должен иметь следующие методы:
#
# new_game() – для создания новой игры;
# get_field() – для получения поля (список списков);
# check_field() – для проверки, есть ли победитель,
# который возвращает X, если победил первый игрок, 0,
# если второй, D, если ничья и None, если можно продолжать игру;
# make_move(row, col) – который устанавливает значение
# текущего хода в ячейку поля с координатами row, col,
# если это возможно, «переключает» ход игрока, а также
# возвращает сообщение «Победил игрок X» при победе
# крестиков, «Победил игрок 0» при победе ноликов, «Ничья»
# в случае ничьей и «Продолжаем играть», если победитель
# после данного хода неопределён.
# Кроме того, метод make_move должен возвращать
# сообщение «Клетка <row>, <col> уже занята»,
# если в клетке уже стоит крестик или нолик, и
# «Игра уже завершена», если в текущей игре уже выявлен
# победитель или закончились ячейки для ходов.
#
# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col метода make_move могут принимать значения от 1 до 3.
#
# Пример:
# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")

class TicTacToeBoard:

    def __init__(self ):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.player = 'X'
        self.end_g = False
        self.move = True
        self.f_move = True
        self.winner = None

    def new_game(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.player = 'X'
        self.end_g = False
        self.move = True
        self.f_move = True
        self.winner = True

    def get_field(self):
        return self.field

    def check_field(self):
        if self.player == 'no winner':
            return 'Draw'
        elif (self.field[0][0] and self.field[0][1] and self.field[0][2]) == 'X'\
            or (self.field[1][0] and self.field[1][1] and self.field[1][2]) == 'X'\
            or (self.field[2][0] and self.field[2][1] and self.field[2][2]) == 'X'\
            or (self.field[0][0] and self.field[1][1] and self.field[2][2]) == 'X'\
            or (self.field[0][2] and self.field[1][1] and self.field[2][0]) == 'X':
            return 'Win X'
        elif (self.field[0][0] and self.field[0][1] and self.field[0][2]) == '0'\
            or (self.field[1][0] and self.field[1][1] and self.field[1][2]) == '0'\
            or (self.field[2][0] and self.field[2][1] and self.field[2][2]) == '0'\
            or (self.field[0][0] and self.field[1][1] and self.field[2][2]) == '0'\
            or (self.field[0][2] and self.field[1][1] and self.field[2][0]) == '0':
            return 'Win 0'
        else:
            return None

    def make_move(self, row, col):
        if self.end_g and not self.f_move:
            return 'Игра уже завершена'
        else:
            if self.field[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            else:
                if self.move:
                    self.field[row - 1][col - 1] = 'X'
                    self.move = False
                    self.f_move = False
                else:
                    self.field[row - 1][col - 1] = 'O'
                    self.move = True
                    self.f_move = False
        return self.check_field()

board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")