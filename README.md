# engeto-academy-analizator-textu
muj první školní  projekt. Analizator textu. 

--možnost přídání rozšíření grafu pro počet písmen ve slově. V tom případě nutné 
  předělání sloupcového grafu protože přidané sloupce budou špatně odsazeny.
 

duplicitní funkce      :řádek 56-60, 154 popsané printy a errory aby se vědělo 
                        kde hledat.

nechané a zakomentované pomocné printy: řádek 88 zkušební čistý text
                                        řádek 99 výpis všech slov
                                        řádek 143-147 výpis slov o určité delce



musím opravyt:

        !!hotovo!!
1. Ošetření pro stav (špatné přihlášení): V tuto chvíli se při špatném přihlášení program ukončí, ale díky NameError a ne pomocí exit(). - Požadavek zadání

    analyza chybi: duplicitní funkce na ověření uživatele a jedna meměla exit.

    jak sem to opravyl: vymazání a přepracování funkce na ověřování uživatele

        !!hotovo!!
2. Statistika pro uppercase: vyhodnocuje špatně (testováno na textu 1), má být 1 slovo ty máš 2 slova. - Požadavek zadání
    
    nalezení chybi: v anglickem textu je spojení US 30N --> jako název cesty (silnice) . Problém je ve slově 30N. Číslovka není 
                    psaná velkým ani malím písmem. 

    analyza chybi: Python v příkazu uppercase nejdřív "odstraní" z výrazu vše co není písmeno a pak analyzuje uppercase 
                   a jelikož z vyrazu 30N po odstranění číslovky zbyde velke "N" tak ho Python vyhodnotí jako True. 

    možnosti řešení :
                     regularní výraz knihovna regex "re":
                                                        
                                            def is_strictly_regex(word):
                                                return bool(re.fullmatch(r"[A-Z]+",word))

                                                vyhody:velmy výkoné a flexibilní.dokáží popsat specifické řetézce
                                                       nebo kombinace znaků

                                                nevýhody:složitější pro začatečníky a pomalejší u krátkých řetezců

                     
                     vlastní implementace:
                                             def is_strictly_upper_custom(word):
                                                for char in word:
                                                    if not char.isupper():
                                                        return False

                                            vyhody:nepoužívá žádné knihony snadno pochopitelná flexibilní při ladění 

                                            nevíhody:při spracování velkych slov může být pomalejší protože každé písmeno 
                                            kontroluje zvlášť.

                    metoda str.isupper():
                                         vyhody:stručná 
                                         nevyhody:občas muže vratit True při speciálních znacich
                                         nebo číslech proto se přidává kontrola.                  
                                         """all(char.isalpha())"""                            
                     

    vyřešono:   def is_strictly_regex(word):
                    return bool(re.fullmatch(r"[A-Z]+",word))

        
        !!hotovo!!
3. Počty pro četnost výskytu (graf). Nikde neodstarňuješ nežádoucí znaky (. , ! ? atd..) , to ovlivňuje celý graf - Požadavek zadání
               
analyza chybi: po funkci split text na slova jsem si nechal vyprintovat všechny slova a ve slovech se nachází "tečky", " čárky" atd.

řešení: vytvoření definice a funkce implementovaná před funkci split z důvodu  
        čistějšího kodu 
                        def odstran_nezadouci_znaky_regex(text):
                            return re.sub(r"[^a-zA-Z0-9\s]", "",vybrany_text)

        !!hotovo!!
4. Struktura kódu není dobrá, odsazení apod. 

celkové přepracování kodu a zkracení zápisu 


