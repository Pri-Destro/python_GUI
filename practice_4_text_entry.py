from tkinter import*

root = Tk()
root.title("mine")

label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file = "img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "ok")

    global photo2
    photo2 = PhotoImage(file = "img2.png")
    label2.config(image = photo2)
    

btn = Button(root, text = "click", command = change)
btn.pack()

root.mainloop()