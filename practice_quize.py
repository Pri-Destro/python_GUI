#간단한 메모장 따라하기
import os
from tkinter import*

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") # 가로 * 세로

menu = Menu(root)

filename = "mynote.txt"

def open_new_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding = "utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_new_file():
    with open(filename, "w", encoding = "utf8") as file:
        file.write(txt.get("1.0", END))

#file 메뉴
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기", command = open_new_file)
menu_file.add_command(label = "저장", command = save_new_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기", command = root.quit)
menu.add_cascade(label = "파일", menu = menu_file)

#file 편집
menu.add_cascade(label = "편집")
menu.add_cascade(label = "서식")
menu.add_cascade(label = "보기")
menu.add_cascade(label = "도움말")

#스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

#메모
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fil = "both", expand = True)

scrollbar.config(command = txt.yview)
root.config(menu = menu)
root.mainloop()

# add anooter