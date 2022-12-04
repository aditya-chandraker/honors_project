# imports
from tkinter import *
import random
from tkinter import messagebox

# Reset the Game
def reset():
    """When initializing this will make all of the variables reset"""
    global colors, turn, score, button_list, last_index_clicked, score_label, root

    # Create our matches
    colors = ["red", "orange", "yellow", "green",
          "blue", "purple", "black", "grey"] * 2
    
    random.shuffle(colors) # Shuffle our matches

    root.title('Memory Game')

    score = 20
    last_index_clicked = None
    
    button_list = [Button(height=4, width=8, command=lambda i=i: button_click(i)) for i in range(0,16)]
    
    counter = 0
    for button in button_list:
        button.grid(row=counter//4, column=counter%4)
        counter += 1

    mylabel = Label(text="Score", height=2, width=8)
    mylabel.grid(row=4, column=0)

    score_label = Label(text="20", height=2, width=8)
    score_label.grid(row=4, column=1)

    cool_button = Button(
        text="reset", command=lambda: reset(), height=2, width=8,)
    cool_button.grid(row=4, column=3)


def button_click(index):
    """Every time a button is clicked it will pass it's index in the list for access and we can continue with a message"""
    global score, last_index_clicked

    button_list[index].configure(bg=colors[index])
    button_list[index].config(state="disabled")

    if last_index_clicked != None:

        if score <= 1:
            messagebox.showinfo("You lost", ":( no more turns")
            reset()

        if colors[index] == colors[last_index_clicked]:
            if all("disabled" in item["state"] for item in button_list):
                messagebox.showinfo("You won", "Congrats!")
                reset()
            
        else:
            messagebox.showinfo("Incorrect!", "Incorrect")
            button_list[index].config(state="active", bg="#F0F0F0")
            button_list[last_index_clicked].config(state="active", bg="#F0F0F0")
            score -= 1
            score_label.configure(text=str(score))

        last_index_clicked = None

    else:
        last_index_clicked = index

if __name__ == "__main__":
    # initilizes and starts program
    root = Tk()
    reset()
    root.mainloop()