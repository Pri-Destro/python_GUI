from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

Label(root, text = "menu").pack()

buger_var = IntVar()
btn_buger1 = Radiobutton(root, text = "hambuger", value = 1, variable = buger_var)
 btn_buger1.select()
btn_buger2 = Radiobutton(root, text = "cheesehambuger", value = 2, variable = buger_var)
btn_buger3 = Radiobutton(root, text = "chickenhambuger", value = 3, variable = buger_var)

btn_buger1.pack()
btn_buger2.pack()
btn_buger3.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "cock", value = "cock", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "sprite", value = "sprite", variable = drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(buger_var.get())
    print(drink_var.get())

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop()