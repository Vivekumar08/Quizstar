import tkinter
from tkinter import *
import random
import time


questions=[
      'Which star is at centre of our solar system?',
      'Name the outermost layer of the sun?',
      'Who was the first person to step foot on the Moon?',
      'Name the intermost layer in the sun?', 
      'How many Natural Satellites of Earth?',
      'Name the spots between the crona and photosphere in sun?',
      'Name the first Indian to go into space?',
      'Name the largest planet in our solar sysytem?',
      'Nmae the largest Satellite in our solar system?',
      'Name the third planet of our Solar system?',
      'Which planet is called Ice Giant?',
      'Name the last planet in our solar system?',
      'How many planet present in our solar system?',
      'Name the Hottest planet in our solar system?',
      'Which planet is Remove from our solar system?',
]

answers_choice=[
      ['1.Mercury','2.Sun','3.Earth','4.Ganymede',],
      ['1.Crona','2.Photosphere','3.Chromosphere','4.Crust',],
      ['1.Neil Armstrong','2.Rakesh Sharma','3.Kalpana Cahwla','4.Aryabhatta',],
      ['1.Inner Core','Chronasphere','3.Photosphere','4.Crona',],
      ['1. 3','2.0','3. 1','4. 2',],
      ['1.Chord','2.Lunar','3.Galileo','4.Chromosphere',],
      ['1.Kalpana Cahwla','2.Neil Armstrong','3.Aryabhatta','4.Rakesh Sharma',],
      ['1.Uranus','2.Neptune','3.Saturn','4.Jupiter',],
      ['1.Moon','2.Ganymede','3.Titan','4.Callisto',],
      ['1.Venus','2.Mars','3.Earth','4.Neptune',],
      ['1.Saturn','2.Pluto','3.Neptune','4.Uranus',],
      ['1.Uranus','2.Charon','3.UB313','4.Ceres',],
      ['1. 8','2. 11','3. 7','4. 12',],
      ['1.Mercury','2.Venus','3.Mars','4.Jupiter',],
      ['1.UB313','2.Pluto','3.Ceres','4.Neptune',],
]
         
answers=[1,0,0,2,2,3,3,3,1,2,1,0,0,1,1,]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,13)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score,correct_answers):
    
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresultanswers = Label(
        root,
        text="Correct answers: "+str(correct_answers)+"/5",
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresultscore = Label(
        root,
        text="Score: "+str(score)+"/25",
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresultscore.pack(pady=(5,5))
    labelimage.pack(pady=(10,10))
    labelresultanswers.pack(pady=(5,5))
    labelresulttext.pack(pady=(0,5))
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    
    global indexes,user_answer,answers,correct_questions
    x = 0
    score = 0
    correct_questions=0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
            correct_questions+=1
        x += 1
    showresult(score,correct_questions)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
       

    




def startquiz():
    
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)
    

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()
    



root = tkinter.Tk()
root.title("Quizstar")
root.geometry("700x550")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="sparrow1.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"italic"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,10))

lblRules = Label(
    root,
    text = "When you click on the start Button\nYou will see a image of SOLAR SYSTEM\nThen you will click on next button\nYours quiz will be start\nand every question has 10 points",
    width = 100,
    font = ("Times",14),
    background = "#534b4f",
    foreground = "#fdee00",
)
lblRules.pack(pady=(10,0))

root.mainloop()
