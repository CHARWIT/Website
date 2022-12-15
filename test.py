if True:
    print('true')
else:
    print('false')

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

import pandas as pd
import random

class quiz_input():

    def __init__(self):
        #Reading the base documents for the conjugations
        self.tab_verbos = pd.read_excel("C:\\Users\\Admin\\Documents\\Nils\\input_spaanse_vervoegingen.xlsx", sheet_name="verbos")
        self.tab_termina = pd.read_excel("C:\\Users\\Admin\\Documents\\Nils\\input_spaanse_vervoegingen.xlsx", sheet_name="terminación_estándar")
        self.tab_irregula = pd.read_excel("C:\\Users\\Admin\\Documents\\Nils\\input_spaanse_vervoegingen.xlsx", sheet_name="irregularidades")
        #Meaning of the abbreviations: pret = preterito, imp = imperfecto, indef = indefenido, pres = presente, subj = subjuntivo, neg = negativo
        self.tiempos = ['presente', 'gerundio', 'perfecto', 'pret_imp', 'pret_indef', 'pres_subj', 'imp_subj', 'futuro', 'condicional', 'imperativo', 'imperativo_neg']
        self.personas = ['1s', '2s', '3s', '1m', '2m', '3m']
        #First person singular does not exist for imperativo
        self.personas_imperativo = ['2s', '3s', '1m', '2m', '3m']
        #Create list of possible combinations of tenses and pronounces in which exist irregularities
        self.tiempos_personales_irregulares = list(self.tab_irregula['tiempo'] + self.tab_irregula['pers'].fillna(''))


    def selection(self, n):
        #Selection of n verb conjugations
        verbo = random.choices(self.tab_verbos['verbos'].tolist(), k=n)
        tiempo = random.choices(self.tiempos, k=n)
        selection = pd.DataFrame({'verbo': verbo, 'tiempo': tiempo})
        #choose the right pronounce for the tenses (first person singular does not exist for imperativo)
        selection['persona'] = selection['tiempo'].apply(lambda x: random.choice(self.personas_imperativo) if 'imperativo' in x else random.choice(self.personas))
        return selection


    def derive_raiz(self, v, t):
        if (t == 'futuro') | (t == 'condicional'):
            raiz = self.get_irregularity(v, 'raiz_futuro', '') if self.irregularity_check(v, 'raiz_futuro', '') else v
        elif t == "pres_subj":
            raiz = self.get_irregularity(v, 'raiz_pres_subj', '') if self.irregularity_check(v, 'raiz_pres_subj', '') else v[:-2]
        elif t == "imp_subj":
            raiz = self.get_irregularity(v, 'raiz_imp_subj', '') if self.irregularity_check(v, 'raiz_imp_subj', '') else v[:-2]
        else:
            raiz = v[:-2]
        return raiz


    def get_terminacion(self, term_inf, t, p):
        return self.tab_termina.loc[(self.tab_termina['tiempo'] == t) & (self.tab_termina['pers'] == p), term_inf].item()


    def irregularity_check(self, v, t, p):
        if (t + p in self.tiempos_personales_irregulares):
            if pd.notnull(self.get_irregularity(v, t, p)):
                return True
            else:
                return False
        else:
            return False


    def get_irregularity(self, v, t, p):
        return self.tab_irregula.loc[(self.tab_irregula['tiempo'] == t) & (self.tab_irregula['pers'].fillna('') == p), v].item()


    def add_gerundio(self, v):
        if self.irregularity_check(v, 'gerundio', ''):
            return self.get_irregularity(v, 'gerundio', '')
        else:
            if v[-2:] == 'ar':
                return v[:-2] + 'ando'
            else:
                return v[:-2] + 'iendo'


    def add_participio(self,v):
        if self.irregularity_check(v, 'perfecto', ''):
            return self.get_irregularity(v, 'perfecto', '')
        else:
            if v[-2:] == 'ar':
                return v[:-2] + 'ado'
            else:
                return v[:-2] + 'ido'
