import Tkinter

from tkinter import *

from IPython.terminal.pt_inputhooks import tk


class Buffer:
    def __init__(self):
        pass

    def put(self):
        pass

    def get(self):
        pass

    def occupied_size_of_buffer(self):
        pass

    def left_size_buffer(self):
        pass

    def free_the_buffer(self):
        pass


root = Tk()
root.geometry('500x500')
root.title('Buffer Class Design')
root.configure(bg='black')

# 1st Display
w0 = Tkinter.Canvas(root, width=400, height=30, bg='Blue')
w0.pack()
w0.place(x=40, y=40)

# 2nd Display
w = Tkinter.Canvas(root, width=400, height=300, bg='Blue')
w.pack()
w.place(x=40, y=100)

# Put Element
label0 = Tkinter.Label(root, text='Put Element:')
label0.config(font=('helvetica', 10))
w.create_window(100, 40, window=label0)
entry1 = Tkinter.Entry(root)
w.create_window(240, 40, window=entry1)

# Get Element
label1 = Tkinter.Label(root, text='Get Element:')
label1.config(font=('helvetica', 10))
w.create_window(100, 80, window=label1)
entry2 = Tkinter.Entry(root)
w.create_window(240, 80, window=entry2)
# Occupied Size of Buffer
label2 = Tkinter.Label(root, text='Occ Size Buff:')
label2.config(font=('helvetica', 10))
w.create_window(100, 120, window=label2)
entry3 = Tkinter.Entry(root)
w.create_window(240, 120, window=entry3)

# Left Size of Buffer
label3 = Tkinter.Label(root, text='Left Size Buffer:')
label3.config(font=('helvetica', 10))
w.create_window(100, 160, window=label3)
entry4 = Tkinter.Entry(root)
w.create_window(240, 160, window=entry4)

# Free the Buffer
label4 = Tkinter.Label(root, text='Free Buffer:')
label4.config(font=('helvetica', 10))
w.create_window(100, 200, window=label4)
entry5 = Tkinter.Entry(root)
B = Tkinter.Button(text="Hello", command=None)
w.create_window(240, 200, window=entry5)

button = Button(root, text='Execute')
button.pack()
button.place(x=320, y=350)
root.mainloop()
