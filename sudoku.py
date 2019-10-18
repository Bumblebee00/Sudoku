import datetime

class Sudoku_solver():

    unsolved = True

    def __init__(self, sudoku):
        self.sudoku = sudoku#->[[], [], [], [], [], [], [], [], []]->evry small list is a row
        self.statring_time = self.time_now()

        while self.unsolved:
            self.squares()
            self.rows()
            self.columns()
            nzero = 0
            for x in self.sudoku:
                for y in x:
                    if y == 0:
                        nzero +=1
            print(nzero)
            if nzero == 0:
                self.unsolved = False
                self.stupid = False
                self.t = self.time_now()-self.statring_time
            #if it takes too long:
            if (self.time_now()-self.statring_time)>20:
                self.unsolved = False
                self.stupid = True

    def time_now(self):
        t = datetime.datetime.now().second
        mt = datetime.datetime.now().microsecond
        return round(t + mt/1000000, 9)
    #returns values of the cell given the x, y coordinates
    def val(self, coordinates):
        x = coordinates[1]
        y = coordinates[0]
        return (self.sudoku[x][y])
    #checks if in the given row there is the given value
    def check_row(self, num_row, number):
        for x in self.sudoku[num_row]:
            if x != number:
                continue
            else:
                return True
                break
    #checks if in the given column there is the given value
    def check_column(self, num_column, number):
        column = []
        for y in range(9):
            column.append((num_column, y))
        for x in column:
            if self.val(x) != number:
                continue
            else:
                return True
                break
    #checks if in the square that contains the given coordinates there is the given value
    def check_square(self, coordinates, number):
        square = []
        x_sett = (coordinates[0] // 3) * 3
        y_sett = (coordinates[1] // 3) * 3
        for y in range(3):
            for x in range(3):
                square.append((x + x_sett, y + y_sett))
        for x in square:
            if self.val(x) != number:
                continue
            else:
                return True
                break
    #calls the solve function for evry square
    def squares(self):
        for w in range(0, 9, 3):
            for z in range(0, 9, 3):
                sq = []
                #this code is responsable of creating the square
                for y in range(3):
                    for x in range(3):
                        sq.append((x+z, y+w))
                self.solve(sq)
    #calls the solve function for evry row
    def rows(self):
        for y in range(9):
            row = []
            for x in range(9):
                row.append((x, y))
            self.solve(row)
    #calls the solve function for evry column
    def columns(self):
        for x in range(9):
            column = []
            for y in range(9):
                column.append((x, y))
            self.solve(column)
    #main function that solves the sudoku in the given coordinates
    def solve(self, coordinates):
        global sudoku
        #separing the numbers anth the 0s
        values = []
        no_values = []
        for x in coordinates:
            if self.val(x) == 0:
                no_values.append(x)
            else:
                values.append(x)
        #finding the missing numbers
        missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in values:
            missing.remove(self.val(x))
        #mainprocess
        for n in missing:
            empty = []
            for x in no_values:
                empty.append(x)
            for s in no_values:
                if self.check_row(s[1], n):
                    empty.remove(s)
                elif self.check_column(s[0], n):
                    empty.remove(s)
                elif self.check_square(s, n):
                    empty.remove(s)
            if len(empty) == 1:
                self.sudoku[empty[0][1]][empty[0][0]] = n
