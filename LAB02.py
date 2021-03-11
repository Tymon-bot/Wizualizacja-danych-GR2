#zadanie 1

lista=["Skazani na shawshank", "Zielona mila", "film3","film4","film5"]
print (lista)
print ("Odwrócona lista")
for a in reversed(lista):
    print (a)

i = 1
while i < 6:
    e=input("Dodaj film")
    lista.append(e)
    i += 1

#zadanie 2

slownik={"Skazani na shawshank", "Zielona mila", "film3","film4","film5"}
print(slownik)

#zadanie 3

przedmioty={
    "MD":"Matematyka dyskretna",
    "PS":"Programowanie strukturalne",
    "WD":"Wizualizacja danych",
    "AN":"Analiza",
    "Ang":"Angielski"
}

print (len(przedmioty))

#zadanie 4
i=int(input("Podaj liczbe"))
wynik=i**i
print (wynik)

#zadanie 5

napis="dowolny ciag znakow"
print (napis.count("a"))

#zadanie 6

a=int(input("Podaj 1 liczbe"))
b=int(input("Podaj 2 liczbe"))
c=int(input("Podaj 3 liczbe"))

if a%2==0 and b>c:
    print("Oba warunki są zachowane")

#zadanie 7

zad=[1,2.5,3,4.5,5.6,6,7,8,9,10]

for i in range(1, len(zad)):
    print("suma elementow", i, "suma druga", i-1, "=", zad[i]+zad[i-1])

#zadanie 8

i=0
zadanie8=[]
while i<10:
    i+=1
    a=int(input("podaj liczbe"))
    if(a%2==0):
        zadanie8.append(a)

for i in zadanie8:
    print(i)

#zadanie 9 nie byłem w stanie go zrobić

#zadanie 10

a=input("podaj liczbę")

try:
    a=float(a)
except ValueError:
    print("Bledna wartosc")
