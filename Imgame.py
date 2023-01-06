from logc import *

class Imgame():

    def restart(self):
        self.field = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.counter = 1
        self.flag = 0
        self.closed = False

    def __init__(self):
        self.field = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.counter = 1
        self.flag = 0
        self.closed = False

    def cell_is_occupied(self, i):
        if self.field[i] == "_":
            return False
        return True

    def rotate(self):  # clockwise
        tempfield = self.field.copy()
        self.field[2] = tempfield[0]
        self.field[5] = tempfield[1]
        self.field[8] = tempfield[2]
        self.field[1] = tempfield[3]
        self.field[7] = tempfield[5]
        self.field[0] = tempfield[6]
        self.field[3] = tempfield[7]
        self.field[6] = tempfield[8]
        return self.field

    def fill_the_cell(self, i):
        if self.field[i] == "_":
            if self.counter % 2 == 1:
                self.field[i] = "X"
            else:
                self.field[i] = "O"
            self.counter += 1
        elif self.counter < 10:
            print("This cell is occupied! Choose another one!")
        else:
            print("Draw")
            self.flag = 1

    def streakx(self):  # checks the winner X
        strict = self.field.copy()
        a = (strict[0] == strict[1] == strict[2] == 'X')
        b = (strict[1] == strict[4] == strict[7] == 'X')
        c = (strict[0] == strict[4] == strict[8] == 'X')
        for i in range(4):
            if xor3(a, b, c):
                return 1
            else:
                simplerotate(strict)
                a = (strict[0] == strict[1] == strict[2] == 'X')
                b = (strict[1] == strict[4] == strict[7] == 'X')
                c = (strict[0] == strict[4] == strict[8] == 'X')
        return 0

    def streako(self):  # checks the winner O
        strict = self.field.copy()
        a = (strict[0] == strict[1] == strict[2] == 'O')
        b = (strict[1] == strict[4] == strict[7] == 'O')
        c = (strict[0] == strict[4] == strict[8] == 'O')
        for j in range(4):
            if xor3(a, b, c):
                return 1
            else:
                simplerotate(strict)
                a = (strict[0] == strict[1] == strict[2] == 'O')
                b = (strict[1] == strict[4] == strict[7] == 'O')
                c = (strict[0] == strict[4] == strict[8] == 'O')
        return 0


    def check_the_game_stats(self):
        if self.field.count(u'_') == 0:
            if (self.streako() == 0) and (self.streakx() == 0):
                self.closed = True
                return "Draw"
            if self.streako() == 1 and self.streakx() == 0:
                self.closed = True
                return "O wins"
            if self.streakx() == 1 and self.streako() == 0:
                self.closed = True
                return "X wins"
            self.flag = 1
        else:
            if self.streako() == self.streakx() == 0:
                pass
            if self.streako() == 1 and self.streakx() == 0:
                self.flag = 1
                self.closed = True
                return "O wins"
            if self.streakx() == 1 and self.streako() == 0:
                self.flag = 1
                self.closed = True
                return "X wins"
