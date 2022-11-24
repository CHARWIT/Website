#Make a canvas

from tkinter import *
from tkinter import ttk
from tkinter import font

# highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=120, weight='bold')

window = Tk()

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
woord_spaans = "Hola"
ttk.Label(mainframe, text=woord_spaans, font=font.Font(size=20)).grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text=" -> ", font=font.Font(size=20)).grid(column=3, row=2, sticky=W)

vertaling = StringVar()
vertaling_entry = ttk.Entry(mainframe, width=20, font=font.Font(size=20), textvariable=vertaling)
vertaling_entry.grid(column=4, row=2, sticky=(W, E))
vertaling_entry.focus()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

def functie():
    print("goed!")

window.bind("<Return>", functie)


window.mainloop()
