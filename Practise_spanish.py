import conjugation
import tkinter as tk
from tkinter import ttk
from tkinter import font

class quiz(tk.Frame):

    def __init__(self, root, quiz_input):
        #tk.Frame.__init__(self)

        self.root_window = root
        self.root_window.title("Practise Spanish")
        # getting screen width and height of display
        width = 1000 # self.root_window.winfo_screenwidth()
        height = 800 # self.root_window.winfo_screenheight()
        self.root_window.geometry("%dx%d" % (width, height))

        self.frame = ttk.Frame(self.root_window, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky='nwes')
        self.frame.option_add('*Font', '20')

        self.input = quiz_input
        self.number = 1
        self.df_sel = self.input.create_sel(1) #Even improviseren

        self.noq = tk.IntVar()
        self.get_user_input()


    def get_user_input(self):
        ttk.Label(self.frame, text="").grid(column=1, row=0, sticky='w')
        ttk.Label(self.frame, text="Hoeveel vervoegingen wil je oefenen?").grid(column=1, row=1, sticky='w')
        ttk.Label(self.frame, text="Geef een aantal:").grid(column=2, row=1, sticky='w')
        self.noq_entry = ttk.Entry(self.frame, width=20, textvariable=self.noq)
        self.noq_entry.grid(column=3, row=1, sticky=('we'))
        self.noq_entry.focus()
        self.noq_entry.bind("<Return>", self.get_noq)


    def get_noq(self, event):
        self.noq = self.noq.get()
        self.df_sel = self.input.create_sel(self.noq)
        self.run_quiz()


    def run_quiz(self):
        #noq_entry vervangen door getal
        #self.noq_entry.delete(0, tk.END)
        ttk.Label(self.frame, text=self.noq).grid(row=1, column=3)

        #Lege regel invoegen
        ttk.Label(self.frame, text="").grid(column=1, row=2, sticky='w')
        self.answers = []
        print(range(self.noq))

        for i in range(self.noq):
            ttk.Label(self.frame, text="Vervoeg in " + self.df_sel['tiempo'][i] + ':').grid(column=1, row=i+3, sticky='w')
            ttk.Label(self.frame, text=self.df_sel['verbo'][i] + ' (' + self.df_sel['persona_text'][i] + ')').grid(column=2, row=i+3, sticky='w')

            #answer = tk.StringVar()
            #self.answers.append(answer)
            entry = tk.Entry(self.frame, width=20) #, textvariable=answer
            entry.grid(column=3, row=i+3, sticky=('we'))
            self.answers.append(entry)

        ttk.Label(self.frame, text="").grid(row=self.noq+4, column=1, sticky='w')
        ttk.Button(self.frame, text='Start over', command=self.start_over).grid(row=self.noq+5, column=1, sticky='w')
        ttk.Button(self.frame, text='Quit', command=self.quit).grid(row=self.noq + 5, column=2, sticky='w')
        self.answers[0].focus()
        self.root_window.bind("<Return>", self.check_answers)


    def check_answers(self, event):
        for i in range(self.noq):
            print(self.df_sel['conjuga'][i])
            if self.answers[i].get() == self.df_sel['conjuga'][i]:
                ttk.Label(self.frame, text='Goed!').grid(column=4, row=i+3, sticky='we')
            else:
                ttk.Label(self.frame, text='Fout').grid(column=4, row=i+3, sticky='we')


    def start_over(self):
        self.__init__(self.root_window, self.input)


    def quit(self):
        self.root_window.quit()


q = conjugation.quiz_input()

root = tk.Tk()
quiz(root, q)
root.mainloop()



#Voor later?
#for child in self.frame.winfo_children():
#    child.grid_configure(padx=5, pady=5)

# For expanding if contents are added, not yet neccesary
# self.root_window.columnconfigure(0, weight=1)
# self.root_window.rowconfigure(0, weight=1)

#highlightFont = font.Font(family='Helvetica', name='appHighlightFont', size=120, weight='bold')
