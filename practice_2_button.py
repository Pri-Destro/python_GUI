from tkinter import*

root = Tk()
root.title("mine")

btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "버튼2") # 버튼 내부의 글자 위치
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "버튼3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = "버튼4")# 버튼 자체의 크기
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", padx = 10, pady = 5, text = "버튼5")# 글자 색, 배경 색
btn5.pack()

photo = PhotoImage(file = "img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("click")

btn7 = Button(root, text = "동작 하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()