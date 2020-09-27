import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
from tkinter import* #__all__
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("mine")

#file add
def add_file():
    files = filedialog.askopenfilenames(title = "select img files", filetypes = (("PNG file", "*.png"), ("All file", "*.*")) ,initialdir = "C:/")
    
    #print selected files
    for file_a in files:
        list_file.insert(END, file_a)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# save path(folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":#cancel
        return 
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

#image merge
def merge_image():

    try:
        # width
        img_width = cmb_width.get()
        if img_width == "pure":
            img_width = -1
        else:
            img_width = int(img_width)

        #space
        img_space = cmb_space.get()
        if img_space == "narrow":
            img_space = 30
        elif img_space == "ordinary":
            img_space = 60
        elif img_space == "wide":
            img_space = 90
        else:#None
            img_space = 0

        #format
        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]

        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width *  x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))
        
        #maximun width and total height
        max_width, total_height = max(widths), sum(heights)

        #making 1 flim
        if img_space > 0:
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0

        for idx, img in enumerate(images):
            #width is not pure
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100 # progress persent
            p_var.set(progress)
            progress_bar.update()

        #format option process
        file_name = "my_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("infor","saving complete")
    except Exception as err:
        msgbox.showerror("error", err)

#start
def start():
    #checking options 
    # print(cmb_width.get())
    # print(cmb_space.get())
    # print(cmb_format.get())

    #check file list
    if list_file.size() == 0:
        msgbox.showwarning("Warring", "NO IMG")

    #check save path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warring", "NO Path")
    
    #image merge
    merge_image()

#file frame (file add, select delete)
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 5, pady = 5)

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "file add", command = add_file)
btn_add_file.pack(side = "left")

btn_del_file = Button(file_frame, padx = 5, pady = 5, width = 12, text = "select delete", command = del_file)
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

btn_dest_path = Button(path_frame, text = "find", width = 10, command = browse_dest_path)
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

btn_start = Button(frame_run, padx = 5, pady = 5, text = "start", width = 12, command = start)
btn_start.pack(side = "right", padx = 5, pady = 5)

root.resizable(False, False) # 너비 높이 변경 불가
root.mainloop()