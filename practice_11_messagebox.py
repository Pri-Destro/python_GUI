import tkinter.messagebox as msgbox
from tkinter import*

root = Tk()
root.title("mine")
root.geometry("640x480")


#turain ticket
def info():
    msgbox.showinfo("info", "ok")

def warn():
    msgbox.showwarning("waring", "no ticket")

def error():
    msgbox.showerror("error", "error")

def okcancel():
    msgbox.askokcancel("ok / cancel", "really")

def retrycancel():
    response = msgbox.askretrycancel("retry / cancel", "missing error")
    if response == 1:
        print("retry")
    elif response == 0:
        print("cancel")
    
def yesno():
    msgbox.askyesno("yes / no", "really")

def yesnocancel():
    respose = msgbox.askyesnocancel(title = None, message = "missing ticket \n want save?")
    #yes = save True
    #no = stop False
    #cancel = stop cancel None
    print("response : ", respose)
    if respose == 1:
        print("ok")
    elif respose == 0:
        print("no")
    else:
        print("cancel")

Button(root, command = info, text = "infor").pack()
Button(root, command = warn, text = "warning").pack()
Button(root, command = error, text = "error").pack()
Button(root, command = okcancel, text = "ok / cancel").pack()
Button(root, command = retrycancel, text = "retry / cancel").pack()
Button(root, command = yesno, text = "yes / no").pack()
Button(root, command = yesnocancel, text = "yes / no / cancel").pack()

root.mainloop()