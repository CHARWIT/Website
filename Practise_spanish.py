import conjugation
import tkinter as tk
from tkinter import ttk
from tkinter import font

#highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=120, weight='bold')
class quiz(tk.Frame):

    def __init__(self, quiz_input):
        print(quiz_input)

"""
    # getting screen width and height of display
    width = 1000 # window.winfo_screenwidth()
    height = 800 # window.winfo_screenheight()
    # setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.title("Practise Spanish")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    window.option_add('*Font', '19')
    opdracht_label = ttk.Label(mainframe, text="Vertaal:").grid(column=1, row=1, sticky=W)

    woord_spaans = StringVar()
    woord_spaans = "hola"
    ttk.Label(mainframe, text=woord_spaans, font=font.Font(size=20)).grid(column=2, row=2, sticky=W)
    ttk.Label(mainframe, text=" -> ", font=font.Font(size=20)).grid(column=3, row=2, sticky=W)

    vertaling = StringVar()
    vertaling_entry = ttk.Entry(mainframe, width=20, font=font.Font(size=20), textvariable=vertaling)
    vertaling_entry.grid(column=4, row=2, sticky=(W, E))
    vertaling_entry.focus()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    show = ttk.Label(mainframe, font=font.Font(size=20))
    show.grid(column=4, row=3, sticky=W)

    def functie(event):
        global show
        if vertaling.get() == "hallo":
            show.config(text="Goed")
        else:
            show.config(text="fout")

    vertaling_entry.bind("<Return>", functie)

"""

q = conjugation.quiz_input()
res=q.create_sel(10)
print(res)

window = tk.Tk()
quiz(window)
window.mainloop()
