# First I imported the tkinter library so that I can use it create GUI for my code
from tkinter import *
#I also imported the random module so that I can use it to randomly select an option from the given list
import random

# Here I have created the tkinter window
root = Tk()
# Set the tile of the window
root.title('Fun Game')
#set the dimensions of the window width & height
root.geometry("350x300")
#disable the ability for the user to resize the window
root.resizable(0,0)

# define the function
def isrock():
    #create a list of possible action for computer to choose from
    possible_action = ['Rock', 'Paper', 'Scissors']
    # computer randomly selects one option from the list
    computer_action = random.choice(possible_action)
    if computer_action == "Scissors":
    # Following the rule of rock paper scissors game, determine game result based on user and computer choice
         game_result = "You Win!"
    elif computer_action == 'Rock':
         game_result = "Tie"
    else:
        game_result = "You Lose"
    # Link the Rock Button with the def function
    label.configure(text="Rock")
    # Update the Label to show computer choice
    label2.configure(text=computer_action)
    # Update the Label to display game result
    label3.configure(text=game_result)

# Similar to the above if function, but this time user chooses paper
def ispaper():
    possible_action = ['Rock', 'Paper', 'Scissors']
    computer_action = random.choice(possible_action)
    if computer_action == "Rock":
         game_result = "You Win!"
    elif computer_action == 'Paper':
         game_result = "Tie"
    else:
        game_result = "You Lose"
    label.configure(text="Paper")
    label2.configure(text=computer_action)
    label3.configure(text=game_result)

# Similar to the above two if statements, but this time user chooses scissors

def isscissors():
    possible_action = ['Rock', 'Paper', 'Scissors']
    computer_action = random.choice(possible_action)
    if computer_action == "Paper":
         game_result = "You Win!"
    elif computer_action == 'Scissors':
         game_result = "Tie"
    else:
        game_result = "You Lose"
    label.configure(text="Scissors")
    label2.configure(text=computer_action)
    label3.configure(text=game_result)

# Here I made three seprate buttons for rock, paper, and scissors for the user to click on
# the first button has text "Rock", a red foreground color, commans to recall the def isrock() function I linked with this button
# the place with X & y value provide the position of the button, I also choce the font size 12 and made it bold
button1=Button(root, text="ROCK", fg='Red', command=isrock, font=('Helvetica', 12, "bold"))
button1.place(x=50,y=40)

# Paper button using the same idea as above and different button position
button2=Button(root, text="PAPER", fg='Red', command=ispaper, font=('Helvetica', 12, "bold"))
button2.place(x=125,y=75)

# Scissors button using the same idea as above and different button position
button3=Button(root, text="SCISSORS", fg='Red', command=isscissors, font=('Helvetica', 12, "bold"))
button3.place(x=210,y=115)

# Here I create three labels to show user choice, computer choice, and game result
# similar to the button code, except different foreground color and lablel position with differnt X(horozontal) & y(vertical) position
# the anchor spacify side of the win
label=Label(root, text='YOU CHOSE', fg='green', font=('Helvetica', 12, "bold"))
label.place(relx=0,rely=0,anchor='nw')

label2=Label(root, text= 'COMPUTER CHOSE', fg='green', font=('Helvetica', 12, "bold"))
label2.place(relx=1,rely=0,anchor='ne')

label3=Label(root,text="GAME RESULT", font=('Helvetica', 14, "bold"))
label3.place(relx=0.5, rely=0.65, anchor='center')


root.mainloop()


