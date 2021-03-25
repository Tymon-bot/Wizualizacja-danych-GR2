import random
import os

# zad 1

with open("Zad1.txt", "w") as f:
    for i in range(5):
        f.write(str(random.randint(0, 30) * 2))
        f.write("\n")
# Zad 2
with open("Zad1.txt", "r") as f:
    print(f.read())

os.remove("Zad1.txt")

# Zad 3

with open("Zad2.txt", "w+") as f:
    f.write("Linijka\nLinijka\nOstatnia linijka")
    f.seek(0)
    for line in f:
        print(line)

os.remove("Zad2.txt")

#Zad 4

class NaZakupy:
    def __init__(self , nazwa_produktu , ilosc , jednostka_miary , cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = int(ilosc)
        self.jednostka_miary = jednostka_miary
        self.cena_jed = float(cena_jed)

    def wyswietl_produkt(self):
        print("Nazwa produktu:" , self.nazwa_produktu , sep=" ")
        print("Ilość:" , self.ilosc , sep=" ")
        print("Jednostka miary:", self.jednostka_miary , sep=" ")
        print("Cena:" , self.cena_jed , sep=" ")

    def ile_produktu(self):
        print("Mamy", self.ilosc , self.jednostka_miary , "produktu" , sep=" ")

    def ile_kosztuje(self, wybranaIlosc):
        print(wybranaIlosc, self.jednostka_miary, "kosztuje",self.cena_jed * wybranaIlosc, sep=" ")

Ziemniak=NaZakupy("ziemniak","3","kg",2)

Ziemniak.wyswietl_produkt()
Ziemniak.ile_produktu()
Ziemniak.ile_kosztuje(7)

del Ziemniak

#Zad 5

class CiagiArytmetyczne:
    roznica = 0
    elementy_ciagu = [0]

    def wyswiel_dane(self):
        for i in self.elementy_ciagu:
            print(i)

    def pobierz_elementy(self , * element):
        self.elementy_ciagu =  [x for x in element]

        self.roznica = self.elementy_ciagu[1] - self.elementy_ciagu[0]

    def pobierz_parametry(self, a1 , r , ile):
        self.elementy_ciagu = [a1 + ( r * x) for x in range(ile)]
        self.roznica = r

    def policz_sume(self):
        print(str(((self.elementy_ciagu[0]+self.elementy_ciagu[len(self.elementy_ciagu)-1])/2)*self.roznica))

ciag= CiagiArytmetyczne()
print("Ciag:")
ciag.pobierz_elementy(1,2,3)
ciag.wyswiel_dane()
print("suma:")
ciag.policz_sume()

del ciag


#Zad 6

class Robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += self.krok * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y -= self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.krok * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.krok * ile_krokow

    def pokaz_gdzie_jestes(self):
        print("X:", self.x, "\nY:", self.y, sep=' ')

robak = Robaczek(1, 2, 5)

robak.pokaz_gdzie_jestes()

robak.idz_w_gore(1)

robak.idz_w_dol(1)

robak.idz_w_lewo(4)

robak.idz_w_prawo(20)

robak.pokaz_gdzie_jestes()

del robak