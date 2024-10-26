""""
projekt.py : první projekt do Engeto Online Python Akadenie

autor: Rostislav Navrátil
email: navratil.rostislav@email.cz
discord: Rostislav Navrátil
"""

  #importuj TEXTS z task_templace

from task_template import TEXTS 
import re
# databaze uživatelu a hesel

uzivatele = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"        
}



#vstupy od uživatele
uzivatelske_jmeno = input("zadej své uživatelské jmeno: ")
heslo = input("zadej své uživatelské heslo: ")

print("-"*20)

# Ověření uživatele
def overeni_uzivatele(uzivatelske_jmeno, heslo):
    print(f"Kontrola uživatelského jména: {uzivatelske_jmeno}")
    print(f"Kontrola hesla: {heslo}")

    print("-"*20)

#ověření uživatele
#def overeni_uzivatele(uzivatelske_jmeno, heslo):
    if uzivatelske_jmeno in uzivatele:
        print(f"uzivatel {uzivatelske_jmeno} nalezen") 

        if uzivatele[uzivatelske_jmeno] == heslo:
            #print("heslo je spravne")
            return True
        else:
            print("spatne helso")
            return False
    else:
        print("špatné jméno nebo heslo. Program se ukončí.")
        exit()      
        
# Volání funkce pro ověření uživatele
if overeni_uzivatele(uzivatelske_jmeno, heslo):
    print("Úspěšné přihlášení!")
    print("-"*20)

#výběr textu
    def vyber_text(texty):

    #vu = výběr uživatele

        vu = input("vyber text který chceš analyzovat čísla 1-3 :")
        print("-"*20)

        if vu in ["1","2","3"]:
            analyzovany_text = texty[int(vu)-1]  #získání textu podle výběru 
            return analyzovany_text
    
        else:
            print("neplatný výběr. Zavírám program")
            exit()

analyzovany_text = vyber_text(TEXTS)
print(f"vybraný text:\n{analyzovany_text}")

#def analyzy_textu
def analýza_textu(text):
    #proměnné statistik

    total_words = 0
    capitalized_words = 0
    uppercase_words = 0
    lowercase_words = 0
    total_numbers = 0
    sum_numbers = 0   
    
    #rozdělí text na slova a uloží do seznamu
    words = analyzovany_text.split()
    #spočítá kolik slov je v seznamu 
    total_words = len(words)
    #smička projde každe slovo v seznamu words
    for word in words:
        if word[0].isupper():
            capitalized_words += 1 #počet slov začínajcím velkým písmenem
        
        if word.isupper():
            uppercase_words += 1 #počet slov psaných velkým písmenem 
        
        if word.islower():
            lowercase_words +=1 # počet slov psaných malím písmenem 

        if re.match(r'^\D*\d+\D*$',word): # slovo obsahující čísla 
        #počet čísel se zvyšuje a sčítají se všechny číslice nalezené ve slově
            total_numbers+= 1
        sum_numbers += sum(int(num)for num in re.findall(r'\d+',word))
    
    print("-"*20)
    print(f"1.Celkový počet slov:{total_words} ")
    print(f"2.počet slov začínajících velkým písmenem:{capitalized_words}")
    print(f"3.počet slov psaných velkými písmeny:{uppercase_words} ")
    print(f"4.počet slov psaných malými písmeny:{lowercase_words} ")
    print(f"5.počet čísel (ne cifer):{ total_numbers}")
    print(f"6.suma všech čísel (ne cifer) v textu:{sum_numbers}")
    print("-"*20)
    
    

#zavolejte funkci pro analýzu textu
analýza_textu(vyber_text)  

#funkce na vypsání zakladního sloupcoveho grafu četnosti delky slov
print("základní sloupcový graf délky slov")
print("-"*20)

# proměná pro slova ve slovníku 
words = []
#proměné pro počítání slov různých délek

pismena_1 = 0
pismena_2 = 0
pismena_3 = 0
pismena_4 = 0
pismena_5 = 0
pismena_6 = 0
pismena_7 = 0
pismena_8 = 0
pismena_9 = 0

words = analyzovany_text.split()

for word in words:
    delka = len(word)
    if delka == 1:
        pismena_1 += 1
    elif delka == 2:
        pismena_2 += 1
    elif delka == 3:
        pismena_3 += 1
    elif delka == 4:
        pismena_4 += 1
    elif delka == 5:
        pismena_5 += 1
    elif delka == 6:
        pismena_6 += 1
    elif delka == 7:
        pismena_7 += 1
    elif delka == 8:
        pismena_8 += 1
    elif delka == 9:
        pismena_9 +=1

#výpis výsledků
print("LEN|     OCCURENCES      | NR.")
print(f"1  |{"*" * pismena_1:<20} | {pismena_1}")
print(f"2  |{"*" * pismena_2:<20} | {pismena_2}")
print(f"3  |{"*" * pismena_3:<20} | {pismena_3}")
print(f"4  |{"*" * pismena_4:<20} | {pismena_4}")
print(f"5  |{"*" * pismena_5:<20} | {pismena_5}")
print(f"6  |{"*" * pismena_6:<20} | {pismena_6}")
print(f"7  |{"*" * pismena_7:<20} | {pismena_7}")
print(f"8  |{"*" * pismena_8:<20} | {pismena_8}")
print(f"9  |{"*" * pismena_9:<20} | {pismena_9}")

