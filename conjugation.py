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


    def conjugacion(self, v, t, p):
        #Create shadow v, t and p for conjugation of the imperativo (which is equal to conjugations in other tenses), gerundio and perfecto
        v2 = v
        t2 = t
        p2 = p

        #Imperativo in 2s will be conjugated as if it was presente 3s
        if t == 'imperativo' and p == '2s':
            t2 = 'presente'
            p2 = '3s'
        #Imperativo in 3s, 1m and 3m will be conjugated as if it was presente de subjuntivo, the same applies to the imperativo negativo
        elif t == 'imperativo' and p in ['3s', '1m', '3m'] or t == 'imperativo_neg':
            t2 = 'pres_subj'
        #Set verbo to (presente of) estar in gerundio ...
        elif t == 'gerundio':
            v2 = 'estar'
            t2 = 'presente'
        #... or to (presente of) haber in perfecto
        elif t == 'perfecto':
            v2 = 'haber'
            t2 = 'presente'

        #Imperativo 2m is a special case without irregularities (inifintivo with last character replaced by 'd')
        if t == 'imperativo' and p == '2m':
            res = v2[:-1] + 'd'
        #In other cases check for irregularity first
        #For gerundio and perfecto in estar and haber (v2 and t2)
        elif (t == 'gerundio' or t == 'perfecto') and self.irregularity_check(v2, t2, p):
            res = self.get_irregularity(v2, t2, p)
        #For the rest, based on (v2,) t and p because of tense and pronounce change in imperativo
        elif self.irregularity_check(v2, t, p):
            res = self.get_irregularity(v2, t, p)
        #And if no irregularity exists, conjugation is: raiz + terminación (depending on term_inf)
        else:
            # The 'terminación' depends on the last two characters of the infinitivo (term_inf)
            term_inf = v2[-2:]
            raiz = self.derive_raiz(v2, t2)
            res = raiz + self.get_terminacion(term_inf, t2, p2)

        #In case of gerundio or perfecto: add gerundio or perfecto to conjugacion of either estar and haber
        if t == 'gerundio':
            res = res + ' ' + self.add_gerundio(v)

        if t == 'perfecto':
            res = res + ' ' + self.add_participio(v)

        return res


    def create_sel(self, n):
        df = self.selection(n)
        df['conjuga'] = df.apply(lambda x: self.conjugacion(x.verbo, x.tiempo, x.persona), axis=1)
        return df


def test():
    q = quiz_input()
    # c=q.conjugacion('ir', 'gerundio', '2m')
    # print(c)

    res = q.create_sel(10)
    print(res)

if __name__ == '__main__':
    test()
