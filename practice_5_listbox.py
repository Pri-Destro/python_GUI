from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "apple")
listbox.insert(1, "banana")
listbox.insert(2, "strowberry")
listbox.insert(END, "watermelon")
listbox.insert(END, "melon")
listbox.pack()

def btncmd():
    #삭제
    #listbox.delete(0) # 맨 처음 항목 삭제

    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인 (시작 idx 끝 idx)
    #print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2))

    #선택된 항목 확인(idx 반환)
    print("선택된 항목 :", listbox.curselection())

btn = Button(root, text = "click", command = btncmd)
btn.pack()

root.mainloop()