from tkinter import ttk
from tkinter import *
Questions = ["Which of the following is not an object programming language?",
             "Which looping statement runs the program from the end?",
             "How is a code block indicated in python?"]
Options = [["Java ", "C++", "Python"],
           ["While loop", "Do while loop", "For loop"],
           ["Brackets", "Indentation", "Key","None of the above"]]

Answers = [2, 3, 0]

Score = 0
Total_No_Questions = 3
Question_no = 1

def Last_attempt():
    global Score,Question_no
    
    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no-1])
    option1.config(text=Options[Question_no-1][0])
    option2.config(text=Options[Question_no-1][1])
    option3.config(text=Options[Question_no-1][2])
    next_b.config(text="next")
    play_again.place_forget()
    score.place_forget()
    root.pack()

def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1

    Question_no += 1

    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.5, rely=.5,anchor=CENTER)
        play_again.place(relx=.45, rely=.1)
        
        score.config(text="Score:"+str(Score), font=("Arial", 15))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def Attempt_quiz():
    user_screen.place_forget()
    root.pack()


Win = Tk()
Win.geometry("600x550" )
Win.title("Test 1")

user_screen = Frame( background="yellow") 
user_screen.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_message = Label(user_screen, width=60, font=("Arial", 15), text="Attempt all questions", background="yellow")
intro_message.pack()
play_b = Button (user_screen, text="Start attempt", command=Attempt_quiz, background="violet")
play_b.pack()

root = Frame(Win)
root.pack_forget()

question = Label(root, width=60, font=("Arial", 15), text=Questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text=Options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=Options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=Options[0][2], command=lambda: check(3))
option3.pack()

next_b = Button(root, text="next", command=next, background="green")
next_b.pack()

score = Label(Win)
score.place_forget()

play_again = Button(Win,text= "Continue last attempt",command=Last_attempt,background="red")
play_again.place_forget()

Win.mainloop()