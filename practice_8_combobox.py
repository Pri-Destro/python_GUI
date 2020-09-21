import tkinter.ttk as ttk
from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("sale")

read_only_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
read_only_combobox.current(0)
read_only_combobox.pack()
read_only_combobox.set("sale")


def btncmd():
    print(combobox.get())
    print(read_only_combobox.get())

btn = Button(root, text = "order", command = btncmd)
btn.pack()

root.mainloop()