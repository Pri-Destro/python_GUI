import tkinter.ttk as ttk
from tkinter import*

root = Tk()
root.title("mine")

#file frame (file add, select delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "file add")
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "select delete")
btn_del_file.pack(side = "right")

#list frame
list_frame = Frame(root)
list_frame.pack(fill = "both", padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = list_file.yview)

#save path frame
path_frame = LabelFrame(root, text = "save path")
path_frame.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 4)

btn_dest_path = Button(path_frame, text = "find", width = 10)
btn_dest_path.pack(side = "right", padx = 5, pady = 5)

#option frame
frame_option = LabelFrame(root, text = "option")
frame_option.pack(padx = 5, pady = 5, ipady = 5)

#1. x width option
#x width label
lbl_width = Label(frame_option, text = "width", width = 8)
lbl_width.pack(side = "left", padx = 5, pady = 5)

#x width combo
opt_width = ["pure", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = "left", padx = 5, pady = 5)

#2. space option label
#space option label
lbl_space = Label(frame_option, text = "interval", width = 8)
lbl_space.pack(side = "left", padx = 5, pady = 5)

#space option combo
opt_space = ["None", "narrow", "ordinary", "wide"]
cmb_space = ttk.Combobox(frame_option, state = "readonly", values = opt_space, width = 10)
cmb_space.current(0)
cmb_space.pack(side = "left", padx = 5, pady = 5)

#3. file fomat option combo
#sfile fomatpace option label
lbl_format = Label(frame_option, text = "format", width = 8)
lbl_format.pack(side = "left", padx = 5, pady = 5)

#spfile fomatace option combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values = opt_format, width = 10)
cmb_format.current(0)
cmb_format.pack(side = "left", padx = 5, pady = 5)

#progressbar
frame_progress = LabelFrame(root, text = "progress")
frame_progress.pack(fill = "x", ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum  = 100, variable = p_var)
progress_bar.pack(fill = "x", padx = 5, pady = 5)

#run frame
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

btn_close = Button(frame_run,  padx = 5, pady = 5, text = "close", width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5)

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12)
btn_start.pack(side = "right", padx = 5, pady = 5)


root.resizable(False, False) # 너비 높이 변경 불가
root.mainloop()