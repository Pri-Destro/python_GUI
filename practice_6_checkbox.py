from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

chkvar = IntVar() # int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text = "dont show", variable = chkvar)
#chkbox.select() #자동 선택 처리
#chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "dont show 7", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()