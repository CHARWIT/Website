import conjugation
import tkinter as tk
from tkinter import ttk
from tkinter import font

def functie():
    print("hallo")
    #if vervoeging_entry.get() == "hallo":
    #    answer.set("goed")
    #else:
    #    answer.set("fout")

root = tk.Tk()

root.title("Practise Spanish")
width = 1000 # root.winfo_screenwidth()
height = 800 # root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky='nwes')
frame.option_add('*Font', '20')

vervoeging_entry = tk.StringVar()
entry = ttk.Entry(frame, width=20, font=font.Font(size=20), textvariable=vervoeging_entry)
entry.grid(column=4, row=2, sticky=('we'))
entry.focus()
root.bind("<Return>", functie())

answer = tk.StringVar()
ttk.Label(frame, font=font.Font(size=20), textvariable=answer).grid(column=4, row=3, sticky='w')

root.mainloop()


"""
from tkinter import *

def toggle ():
    global shown
    if shown: l.grid_remove () # Hide the text
    else: l.grid () # Show the text
    shown = not shown # Reverse the 'shown' boolean value

# Create the window with all the widgets contained within a frame
root = Tk ()
f = Frame (root)
f.grid ()
shown = False
Button (f, text = "Toggle text", command = toggle).grid ()
l = Label (f, text = "Your text")
root.mainloop ()


#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("700x250")

# Define a function to return the Input data
def get_data():
   label.config(text= entry.get(), font= ('Helvetica 13'))

#Create an Entry Widget
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="", font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop()
"""
