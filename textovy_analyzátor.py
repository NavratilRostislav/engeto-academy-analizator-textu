"""
projekt.py : první projekt do Engeto Online Python Akadenie

autor: Rostislav Navrátil
email: navratil.rostislav@email.cz
discord: Rostislav Navrátil
"""


#importuj TEXTS z task_templace

from task_template import TEXTS 
import re


# databaze uživatelů a hesel

uzivatele = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"        
}

#základní seznámení uživatele
print("vítej uživately v analyzátoru textu")
print("-"*20)

#vstupy od uživatele
uzivatelske_jmeno = input("zadej své uživatelské jmeno: ")
heslo = input("zadej své uživatelské heslo: ")

print("-" * 20)


#ověření uživatele
def overeni_uzivatele(uzivatelske_jmeno, heslo):
    if uzivatelske_jmeno in uzivatele and uzivatele[uzivatelske_jmeno] == heslo:
        print(f"uživatel {uzivatelske_jmeno} nalezen a heslo je správné.") 
        print("Úspěšné přihlášení!")
        print(f"vítám tě zpátky {uzivatelske_jmeno}. sem rád že ses vrátil/a.")
        print("-" * 20)    
        return True
    else:
        print("špatné jméno nebo heslo. Program se ukončí.")
        exit()      
   
#výběr textu
def vyber_text(texty):

    #vu = výběr uživatele
    vu = input("vyber text který chceš analyzovat čísla 1-3 :")
    print("-" * 20)
    if vu in ["1", "2", "3"]:
        vybrany_text = texty[int(vu)-1]  #získání textu podle výběru 
        
        #ověření a převod na řetězec
        if isinstance(vybrany_text, list):
            vybrany_text = " ".join(vybrany_text)
        elif not isinstance(vybrany_text, str):
            raise ValueError("chyba v 'vyber_text' : Očekáván byl řetězec.")
        
        print(f"vybraný text:\n{vybrany_text}\n" + "-" * 20)
        return vybrany_text
    else:
        print("neplatný výběr. Zavírám program")
        exit()


#odstraní všechny nežádoucí znaky kromě písmen a mezer
def odstran_nezadouci_znaky(vybrany_text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", vybrany_text)

#počítají se jen slova z alfabeth 
def is_strictly_regex(words):
    return all(bool(re.fullmatch(r"[A-Z]+", word)) for word in words)


#Analýza vybraného textu
def analyza_textu(vybrany_text):
    if isinstance(vybrany_text, list):#zkontroluje jestly je vybrany_text seznam
        vybrany_text = " ".join(vybrany_text) #pokud ano, převedeme ho na řetezec  

    #vyčistění textu
    cisty_text = odstran_nezadouci_znaky(vybrany_text)
    #print(f"zkušební čisty text: {cisty_text}")#pomocný print
    
    #proměnné statistik
    words = cisty_text.split()#rozdělí text na slova a uloží do seznamu
    total_words = len(words)#spočítá kolik slov je v seznamu
    capitalized_words = 0
    uppercase_words = 0
    lowercase_words = 0
    total_numbers = 0
    sum_numbers = 0   
    
    #print(f"výpis všech slov: {words}")#pomocný print

    #smička projde každe slovo v seznamu words
    for word in words:
        if word[0].isupper():
            capitalized_words += 1 #počet slov začínajcím velkým písmenem
        if is_strictly_regex(word):
            uppercase_words += 1 #počet slov psaných velkým písmenem 
        if word.islower():
            lowercase_words +=1 # počet slov psaných malím písmenem 
        if re.match(r'^\D*\d+\D*$',word): # slovo obsahující čísla 
        #počet čísel se zvyšuje a sčítají se všechny číslice nalezené ve slově
            total_numbers+= 1
        sum_numbers += sum(int(num)for num in re.findall(r'\d+',word))
    
    print("-" * 20)
    print(f"1.Celkový počet slov:{total_words} ")
    print(f"2.počet slov začínajících velkým písmenem:{capitalized_words}")
    print(f"3.počet slov psaných velkými písmeny:{uppercase_words} ")
    print(f"4.počet slov psaných malými písmeny:{lowercase_words} ")
    print(f"5.počet čísel (ne cifer):{ total_numbers}")
    print(f"6.suma všech čísel (ne cifer) v textu:{sum_numbers}")
    print("-" * 20)
    
    
    #vypsání zakladního sloupcoveho grafu četnosti delky slov
    print("základní sloupcový graf délky slov")
    print("-" * 20)
    
    # proměné pro počítání slov různých délek
    pismena = [0] * 10 # pole pro délky slov 1-10
    
    # počítání delky slov
    for word in words:
        delka = len(word)
        if 1 <= delka < len(pismena):
            pismena[delka]+= 1
        
    #výpis výsledků
    print("LEN|     OCCURENCES       |  NR.")
    for i in range(1, len(pismena)):
        print(f"{i}  |{"*" * pismena[i]:<20}  |  {pismena[i]}")
    #print("-"*20)
    
    #funkce do budoucna   
    #povolene_delky = [5] #povolene delky na výpis 
    #for word in words:
        #if len(word) in povolene_delky:
           #print(word)

    #zavolání funkce pro odsranění nežádoucích znaků
    odstran_nezadouci_znaky(vybrany_text)
    
    #zavolání funkce: počítají se jen slova z alfabeth
    is_strictly_regex(words)
           
if overeni_uzivatele(uzivatelske_jmeno, heslo):
    vybrany_text = vyber_text(TEXTS)
    if not isinstance(vybrany_text, str):
        print("vybraný text není správný, očekáván byl řetězec")
        exit()
    
    
    analyza_textu(vybrany_text)
    