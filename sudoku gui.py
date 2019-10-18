import tkinter as tk
from PIL import ImageTk, Image
import sudoku as sk
#starting variables
font = ('Roboto', 15)
b_font = ('Roboto', 19)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class Widgets():

    def __init__(self, master):
        self.master = w
        self.master.geometry('640x400')
        self.master.title('Cripter')
        self.master.resizable(False, False)
        #all the widgets
        self.s_frame = tk.Frame(master=self.master, bd=0)
        self.s_frame.place(relx=0, rely=0, relwidt=0.625, relheight=1)

        self.img = ImageTk.PhotoImage(Image.open('sudoku image.png'))
        self.s_image = tk.Label(master=self.s_frame, image=self.img)
        self.s_image.place(relx=0, rely=0, relwidt=1, relheight=1)

        self.solve = tk.Button()
        self.solve.config(text='solve', font=font, bg='white', activebackground='white', relief='groove', command=self.control_solve)
        self.solve.place(relx=0.626, rely=0, relwidt=0.375, relheight=0.25)

        self.stupid_l = tk.Label(bg='white')
        self.stupid_l.place(relx=0.625, rely=0.25, relheight=0.75, relwidt=0.375)

        self.clear_button = tk.Button(text='clear', font=font, bg='white', activebackground='white', relief='groove', command=self.clear)
        self.clear_button.place(relx=0.91, rely=0.9)
        #function that add all the entry widget
        self.entry_add(self.s_frame)

    def clear(self):
        for x in self.entry_list:
            for y in x:
                y.delete(first=0)

    #validate function to insert only numbers
    def only_digit(self, x, y, n):
        vcmd2 = w.register(self.only_backspace)

        if n.isdigit():
            self.entry_list[int(y)][int(x)].config(validatecommand=(vcmd2, x, y, '%d', '%P'))#changing to the other validate function
            return True
        else:
            return False
    #validate function to delete only
    def only_backspace(self, x, y, action, n):
        vcmd = w.register(self.only_digit)
        if action=='0':
            self.entry_list[int(y)][int(x)].config(validatecommand=(vcmd, x, y, '%P'))#changing to the other validate function
            return True
        else:
            return False

    def entry_add(self, master):
        self.entry_list = [[], [], [], [], [], [], [], [], []]
        vcmd = w.register(self.only_digit)
        #creating all the 91 entry widgets and placing over the sudoku image
        for y in range(9):
            for x in range(9):
                self.entry = tk.Entry(master, font=b_font, bd=0, justify='center', validate='key', validatecommand=(vcmd, x, y, '%P'))
                self.entry.place(x=((x*400)/9 + 3.2), y=((y*400)/9 + 3.2), width=38.4, height=38.4)#it took me an huge effort to write down all these values!
                self.entry_list[y].append(self.entry)

    def control_solve(self):
        sudoku_tosolve = [[], [], [], [], [], [], [], [], []]
        #creating the sudoku list
        for y in range(9):
            for x in range(9):
                n = self.entry_list[y][x].get()
                if n == '':
                    sudoku_tosolve[y].append(0)
                else:
                    sudoku_tosolve[y].append(int(n))
        #mainprocess
        this_sudoku = sk.Sudoku_solver(sudoku_tosolve)
        if (not this_sudoku.stupid):
            #displaying the sudoku
            for y in range(9):
                for x in range(9):
                    self.entry_list[y][x].delete(first=0)
                    self.entry_list[y][x].insert(0, this_sudoku.sudoku[y][x])
            self.stupid_l.config(text=f'Sono passati:\n{this_sudoku.t}\nsecondi', font=b_font)
        else:
            self.stupid_l.config(text='Spiacente, non\nsono riuscito\na risolverlo',
                                 font=b_font)


w = tk.Tk()
gui = Widgets(master=w)

w.mainloop()
