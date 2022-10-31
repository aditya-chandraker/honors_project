# importing Packages from tkinter
from tkinter import *
from tkinter import messagebox
import random

colors = ["red", "orange", "yellow", "green",
          "blue", "purple", "black", "grey"] * 2

# Button
b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
b_true_table = [[False, False, False, False], [False, False, False, False], [
    False, False, False, False], [False, False, False, False]]

random.shuffle(colors)


def clicked(r, c):
    b[r][c].configure(bg=colors[(r*4+c)])

    if not False in b_true_table:
        pass


def play_game():

    # text for buttons
    for i in range(4):
        for j in range(4):
            button = Button(height=4, width=8,
                            command=lambda r=i, c=j: clicked(r, c))
            b[i][j] = button
            b[i][j].grid(row=i, column=j)

    mainloop()


def helloCallBack():
    pass


if __name__ == "__main__":
    # Design window
    # Creating the Canvas
    root = Tk()
    mylabel = Label(text="Score", height=2, width=8,)
    mylabel.grid(row=4, column=0)
    score = Label(text="20", height=2, width=8,)
    score.grid(row=4, column=1)

    cool_button = Button(
        text="reset", command=helloCallBack, height=2, width=8,)
    cool_button.grid(row=4, column=3)

    # Title of the window
    root.title("Memory Game")
    #root.resizable(0, 0)

    play_game()
