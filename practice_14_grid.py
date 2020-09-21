import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

# btn1 = Button(root, text = "button1")
# btn2 = Button(root, text = "button1")

# # btn1.pack()
# # btn2.pack()

# # btn1.pack(side = "left")
# # btn2.pack(side = "left")

# btn1.grid(row = 0, column = 0)
# btn2.grid(row = 1, column = 1)


btn1 = Button(root, text = "num", width =  5, height = 2)
btn2 = Button(root, text = "/", width =  5, height = 2)
btn3 = Button(root, text = "*", width =  5, height = 2)
btn4 = Button(root, text = "-", width =  5, height = 2)

#1line
btn1.grid(row = 0, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn2.grid(row = 0, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn3.grid(row = 0, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn4.grid(row = 0, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

#2line
btn5 = Button(root, text = "7", width =  5, height = 2)
btn6 = Button(root, text = "8", width =  5, height = 2)
btn7 = Button(root, text = "9", width =  5, height = 2)
btn8 = Button(root, text = "+", width =  5, height = 2) # 세로 2줄

btn5.grid(row = 1, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn6.grid(row = 1, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn7.grid(row = 1, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn8.grid(row = 1, column = 3, rowspan = 2, sticky = N+E+W+S, padx = 3, pady = 3)

#3line
btn9 = Button(root, text = "4", width =  5, height = 2)
btn10 = Button(root, text = "5", width =  5, height = 2)
btn11 = Button(root, text = "6", width =  5, height = 2)

btn9.grid(row = 2, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn10.grid(row = 2, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn11.grid(row = 2, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)

#4line
btn13 = Button(root, text = "1", width =  5, height = 2)
btn14 = Button(root, text = "2", width =  5, height = 2)
btn15 = Button(root, text = "3", width =  5, height = 2)
btn16 = Button(root, text = "enter", width =  5, height = 2)

btn13.grid(row = 3, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn14.grid(row = 3, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn15.grid(row = 3, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn16.grid(row = 3, column = 3, rowspan = 2, sticky = N+E+W+S, padx = 3, pady = 3)

#5line
btn17 = Button(root, text = "0", width =  5, height = 2)
btn18 = Button(root, text = ".", width =  5, height = 2)

btn17.grid(row = 4, column = 0, columnspan = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn18.grid(row = 4, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)


root.mainloop()