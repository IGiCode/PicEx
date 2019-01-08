# We_call_on_the_Ancestors
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk


root = Tk()
root.geometry('+300+150')#location on screen
root.title('PicEX')# App_title
root.resizable(False,False)

messagebox.showinfo(title = 'Welcome To PicEX', message = 'Click OK to select your Picture(s) Folder')

path = filedialog.askdirectory()# Choose Images folder
list_ = os.listdir(path)# Get list of all sub-directories or files
list_size = len(list_)- 1
pos = IntVar()
pos.set(0)
width = 550 #Image Width and height
height = 370

rawimage = Image.open(path + '/' + list_[pos.get()])#Imports raw image
[size_x, size_y] = rawimage.size
if size_x > width or size_y > height:#These codes will resize image
    if size_x > width:
        n_raw = rawimage.resize((width,size_y), Image.ANTIALIAS)
        if size_y > height:
            n_raw = rawimage.resize((width,height), Image.ANTIALIAS)
    else:
        n_raw = rawimage.resize((size_x, height), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(n_raw)
else:
    logo = ImageTk.PhotoImage(rawimage)

def next_():
    global logo
    if pos.get() == list_size:
        messagebox.showinfo(title ='PicEX', message ='This is the last image in the folder')
    else:
        pos.set(pos.get() + 1)
        nrawimage = Image.open(path + '/' + list_[pos.get()])# imports new image
        [nsize_x, nsize_y] = nrawimage.size
        if nsize_x > width or nsize_y > height:
            if nsize_x > width:
                n_raw = nrawimage.resize((width,nsize_y), Image.ANTIALIAS)
                if nsize_y > height:
                    n_raw = nrawimage.resize((width,height), Image.ANTIALIAS)
            else:
                n_raw = nrawimage.resize((nsize_x, height), Image.ANTIALIAS)
            logo = ImageTk.PhotoImage(n_raw)
        else:
            logo = ImageTk.PhotoImage(nrawimage)
        label2.config(image = logo)
        label1.config(text=list_[pos.get()])
def prev():
    global logo
    if pos.get() == 0:
        messagebox.showinfo(title ='PicEX', message = 'This is the first image in the folder')
    else:
        pos.set(pos.get() - 1)
        nrawimage = Image.open(path + '/' + list_[pos.get()])# imports new image
        [nsize_x, nsize_y] = nrawimage.size
        if nsize_x > width or nsize_y > height:
            if nsize_x > width:
                n_raw = nrawimage.resize((width,nsize_y), Image.ANTIALIAS)
                if nsize_y > height:
                    n_raw = nrawimage.resize((width,height), Image.ANTIALIAS)
            else:
                n_raw = nrawimage.resize((nsize_x, height), Image.ANTIALIAS)
            logo = ImageTk.PhotoImage(n_raw)
        else:
            logo = ImageTk.PhotoImage(nrawimage)
        label2.config(image = logo)
        label1.config(text=list_[pos.get()])
def quit_():
    if messagebox.askyesnocancel(title ='PicEX', message = 'Do you want to Quit?') == True:
        root.destroy()
def CallNext(event):
    next_()
def CallPrev(event):
    prev()
def CallQuit(event):
    quit_()
    
# Widgets
label1 = ttk.Label(root, text = list_[pos.get()], anchor = CENTER)#displays image name
label1.pack(fill = X)
label2 = Label(root, background = 'gray95', image = logo, width = width, height = height)#displays image
label2.pack()
frame1 = Frame(root, relief=FLAT, background = 'blue')
frame1.pack()
button1 = ttk.Button(frame1, text = 'Next', command = next_)
button1.grid(row=0,column=1)
button2 = ttk.Button(frame1, text = 'Previous', command = prev)
button2.grid(row=0,column=0)
button3 = ttk.Button(frame1, text = 'Quit', command = quit_)
button3.grid(row=0,column=2)

#Binds to Keyboard events
root.bind("<Right>", CallNext)
root.bind_all("<Left>", CallPrev)
root.bind_all("<Escape>", CallQuit)
root.withdraw()
root.deiconify()

root.mainloop()

print('Thank you for using my program.')
print('''
PicEX Photo Viewer
...Signed...
Isaac O
3:15pm
Friday, 30 Nov '18''')
