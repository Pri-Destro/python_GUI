import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

Label(root, text = "select menu").pack(side = "top")

Button(root, text  ="order").pack(side = "bottom")

#menu
frame_buger = Frame(root, relief = "solid", bd = 1)
frame_buger.pack(side = "left", fill = "both", expand = True)

Button(frame_buger, text = "buger").pack()
Button(frame_buger, text = "cheesebuger").pack()
Button(frame_buger, text = "chickenbuger").pack()

frame_drink = LabelFrame(root, text = "drink")
frame_drink.pack(side = "right", fill = "both", expand = True)

Button(frame_drink, text = "coke").pack()
Button(frame_drink, text = "sprite").pack()

root.mainloop()