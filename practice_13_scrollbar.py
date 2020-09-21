import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")

# set 이 없으면 스크롤 기동x 
listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack()

scrollbar.config(command = listbox.yview)

root.mainloop()