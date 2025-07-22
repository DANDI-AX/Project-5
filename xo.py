import tkinter.messagebox
from tkinter import *

win = Tk()
win.geometry("1350x750+0+0")
win.title("TIC TAC TOE @DM")

win.resizable(width=False,height=False)

def rgb_hack(rgba):
    return "#%02x%02x%02x" % rgba
win.configure(bg=rgb_hack((14, 18, 37)))
fr1 = Frame(win, bg=rgb_hack((14, 18, 37)), pady=2, width=1350, height=100, relief=RIDGE)
fr1.grid(row=0, column=0)
Lfr1 = Label(fr1, font=("arial", 50, "bold"), text="XO GAME", bd=21, bg=rgb_hack((14, 18, 37)), fg="cornsilk",
             justify=CENTER)
Lfr1.grid(row=0, column=0)

mainfr = Frame(win, bg=rgb_hack((14, 18, 37)), pady=2, width=1350, height=600, relief=RIDGE)
mainfr.grid(row=1, column=0)

leftfr = Frame(mainfr, bd=10, width=750, height=500, pady=2, padx=10, bg=rgb_hack((14, 18, 37)), relief=RIDGE)
leftfr.pack(side=LEFT)
rightfr = Frame(mainfr, bd=10, width=460, height=500, pady=2, padx=10,bg=rgb_hack((14, 18, 37)), relief=RIDGE)
rightfr.pack(side=RIGHT)

rightfr1 = Frame(rightfr, bd=10, width=460, height=200, pady=2, padx=10, bg=rgb_hack((14, 18, 37)), relief=RIDGE)
rightfr1.grid(row=0, column=0)
rightfr2 = Frame(rightfr, bd=10, width=460, height=200, pady=2, padx=10,bg=rgb_hack((14, 18, 37)), relief=RIDGE)
rightfr2.grid(row=1, column=0)

playerX = IntVar()
playerO = IntVar()
buttons = StringVar()

playerX.set(0)
playerO.set(0)
click = True


def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"

        click = False
        scrkpr()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scrkpr()
def reset():
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "

    btn1.configure(bg=rgb_hack((6, 16, 45)))
    btn2.configure(bg=rgb_hack((6, 16, 45)))
    btn3.configure(bg=rgb_hack((6, 16, 45)))
    btn4.configure(bg=rgb_hack((6, 16, 45)))
    btn5.configure(bg=rgb_hack((6, 16, 45)))
    btn6.configure(bg=rgb_hack((6, 16, 45)))
    btn7.configure(bg=rgb_hack((6, 16, 45)))
    btn8.configure(bg=rgb_hack((6, 16, 45)))
    btn9.configure(bg=rgb_hack((6, 16, 45)))
def ex():
    ex= tkinter.messagebox.askyesnocancel("EXIT", " PLEASE, CONFIRM THAT YOU WANT TO EXIT!")
    if ex>0:
        win.destroy()
    else:

        playerX("")
        playerO("")




def newgame():
    reset()
    playerX.set(0)
    playerO.set(0)

def scrkpr():
    if  (btn1["text"] == "X" and btn2["text"]=="X" and btn3["text"]=="X"):
        btn1.configure(bg=rgb_hack((140,36,255)))
        btn2.configure(bg=rgb_hack((140,36,255)))
        btn3.configure(bg=rgb_hack((140,36,255)))
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn4["text"] == "X" and btn5["text"]=="X" and btn6["text"]=="X"):
        btn4.configure(bg=rgb_hack((226,25,255)))
        btn5.configure(bg=rgb_hack((226,25,255)))
        btn6.configure(bg=rgb_hack((226,25,255)))
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn7["text"] == "X" and btn8["text"]=="X" and btn9["text"]=="X"):
        btn7.configure(bg=rgb_hack((226,255,25)))
        btn8.configure(bg=rgb_hack((226,255,25)))
        btn9.configure(bg=rgb_hack((226,255,25)))
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn3["text"] == "X" and btn5["text"]=="X" and btn7["text"]=="X"):
        btn3.configure(background="gold")
        btn5.configure(background="gold")
        btn7.configure(background="gold")
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn1["text"] == "X" and btn5["text"]=="X" and btn9["text"]=="X"):
        btn1.configure(background="teal")
        btn5.configure(background="teal")
        btn9.configure(background="teal")
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn1["text"] == "X" and btn4["text"]=="X" and btn7["text"]=="X"):
        btn1.configure(bg=rgb_hack((178,255,102)))
        btn4.configure(bg=rgb_hack((178,255,102)))
        btn7.configure(bg=rgb_hack((178,255,102)))
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn2["text"] == "X" and btn5["text"]=="X" and btn8["text"]=="X"):
        btn2.configure(background="lime")
        btn5.configure(background="lime")
        btn8.configure(background="lime")
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")
    if  (btn3["text"] == "X" and btn6["text"]=="X" and btn9["text"]=="X"):
        btn3.configure(background="khaki")
        btn6.configure(background="khaki")
        btn9.configure(background="khaki")
        n= float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER X HAS WON THE GAME!!")

    if (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O"):
        btn1.configure(background="green")
        btn2.configure(background="green")
        btn3.configure(background="green")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn4["text"] == "O" and btn5["text"]=="O" and btn6["text"]=="O"):
        btn4.configure(bg=rgb_hack((255,178,207)))
        btn5.configure(bg=rgb_hack((255,178,207)))
        btn6.configure(bg=rgb_hack((255,178,207)))
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn7["text"] == "O" and btn8["text"]=="O" and btn9["text"]=="O"):
        btn7.configure(bg=rgb_hack((255,191,153)))
        btn8.configure(bg=rgb_hack((255,191,153)))
        btn9.configure(bg=rgb_hack((255,191,153)))
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn3["text"] == "O" and btn5["text"]=="O" and btn7["text"]=="O"):
        btn3.configure(background="purple")
        btn5.configure(background="purple")
        btn7.configure(background="purple")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn1["text"] == "O" and btn5["text"]=="O" and btn9["text"]=="O"):
        btn1.configure(background="pink")
        btn5.configure(background="pink")
        btn9.configure(background="pink")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn1["text"] == "O" and btn4["text"]=="O" and btn7["text"]=="O"):
        btn1.configure(background="orange")
        btn4.configure(background="orange")
        btn7.configure(background="orange")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn2["text"] == "O" and btn5["text"]=="O" and btn8["text"]=="O"):
        btn2.configure(background="maroon")
        btn5.configure(background="maroon")
        btn8.configure(background="maroon")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER O HAS WON THE GAME!!")
    if  (btn3["text"] == "O" and btn6["text"]=="O" and btn9["text"]=="O"):
        btn3.configure(background="magenta")
        btn6.configure(background="magenta")
        btn9.configure(background="magenta")
        n= float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("WINNER TELLER","PLAYER 0 HAS WON THE GAME!!")
















LBX = Label(rightfr1, font=("arial", 40, "bold"), text="PLAYER X:", pady=2, padx=2, bg=rgb_hack((14, 18, 37)),foreground=rgb_hack((179, 240, 255)))
LBX.grid(row=0, column=0, sticky=W)

ENX = Entry(rightfr1, font=("arial", 40, "bold"), textvariable=playerX, bd=5, width=10, justify=LEFT,fg=rgb_hack((128, 255, 255)),bg=rgb_hack((4, 14, 43))).grid(row=0,
                                                                                                           column=1)

ENO = Entry(rightfr1, font=("arial", 40, "bold"), textvariable=playerO, bd=5, width=10, justify=LEFT,fg=rgb_hack((128, 255, 255)),bg=rgb_hack((4, 14, 43))).grid(row=1,
                                                                                                           column=1)

btnre = Button(rightfr2, text="RESET", font=("arial", 26, "bold"), bg=rgb_hack((28, 24, 52)), height=2, width=30, command=reset,fg="cyan")
btnre.grid(row=0, column=0)

btnnew = Button(rightfr2, text="NEW GAME", font=("arial", 26, "bold"), bg=rgb_hack((34,0,51)), height=2, width=30, command=newgame,fg="cyan")
btnnew.grid(row=1, column=0)

btnEX = Button(rightfr2, text="EXIT", font=("arial", 26, "bold"), bg=rgb_hack((56, 5, 5)), height=2, width=30, command=ex,fg=rgb_hack((128, 191, 255)))
btnEX.grid(row=3, column=0)

LBO = Label(rightfr1, font=("arial", 40, "bold"), text="PLAYER O:", pady=2, padx=2, bg=rgb_hack((14, 18, 37)),foreground=rgb_hack((179, 240, 255)))
LBO.grid(row=1, column=0, sticky=S)

btn1 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn1))
btn1.grid(row=1, column=0, sticky=S + N + E + W)

btn2 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn2))
btn2.grid(row=1, column=1, sticky=S + N + E + W)

btn3 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn3))
btn3.grid(row=1, column=2, sticky=S + N + E + W)

btn4 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn4))
btn4.grid(row=2, column=0, sticky=S + N + E + W)

btn5 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn5))
btn5.grid(row=2, column=1, sticky=S + N + E + W)

btn6 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn6))
btn6.grid(row=2, column=2, sticky=S + N + E + W)

btn7 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn7))
btn7.grid(row=3, column=0, sticky=S + N + E + W)

btn8 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn8))
btn8.grid(row=3, column=1, sticky=S + N + E + W)

btn9 = Button(leftfr, text=" ", font=("arial", 26, "bold"), bg=rgb_hack((6, 16, 45)), height=3, width=8,fg=rgb_hack((52,244,235)),
              command=lambda: checker(btn9))
btn9.grid(row=3, column=2, sticky=S + N + E + W)

win.mainloop()
