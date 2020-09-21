from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, "imput")

e = Entry(root, width = 30)
e.pack()
e.insert(0, "one line")

def btncmd():
    print(txt.get("1.0", END))# 1번 라인에서 0번 위치부터 받아온다 
    print(e.get())

    # 내용 제거
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()