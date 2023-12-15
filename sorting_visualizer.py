from tkinter import *
from tkinter import ttk
import random
from bubblesort_code import bubble_sort

root = Tk()
root.title('DSA PROJECT Sorting Algorithm Visualiser')
root.geometry("750x600")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []



# GUI CODING PART
options_frame = Frame(root, width=700, height=200, bg='orange')
options_frame.pack(pady=20)

canvas = Canvas(root, width=700, height=350, bg='lightgray')
canvas.pack(pady=10)

Label(options_frame, text="Choose Algorithm: ", bg='orange').grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=['Bubble Sort'], width=15)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                     label="Sorting Speed ", bg='orange')
sortingspeed.grid(row=0, column=2, padx=10, pady=10)

Button(options_frame, text="Start Sorting", command=sorting, bg='red', fg='white', height=2).grid(row=0, column=3, padx=5,
                                                                                                  pady=5)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Lower Limit", bg='orange')
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
