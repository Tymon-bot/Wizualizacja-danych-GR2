
#Zad 1
A=[1-x for x in range(10)]
B=[4**x for x in range(7)]
C=[x for x in B if x%2==0]

#Zad 2
lista1=[a in range(10)]
lista2=[a for a in lista1 if a%2==0]
print(lista2)

#Zad 3
produkty={"czosnek":"sztuki","pomidory":"kg","cebula":"kg","woda":"sztuki"}
produktyNasztuki=[key for key, value in produkty if value =="sztuki"]

del produktyNasztuki
del produkty

#Zad 4
def trojkat_Prostokatny(a,b,c):
    przyprostokątne=a**2 + b**2
    przeciwprostokątna=c**2
    if przyprostokątne==przeciwprostokątna:
        print("Trójkąt jest prostokątny")
    else:
        print("Trojkąt nie jest prostokątny")
    trojkat_Prostokatny(3,5,7)

#Zad 5
def pole_trapezu(a=3,b=5,h=8):
    return ((a+b)*h)/2

#Zad 6

def ciag(a=1, b=4, ile=10):
    lista=[]
    i=0
    if ile<=0:
        print("wartosc ile nie moze byc mniejsza od 0")
        return 0
    elif ile==1:
        return a*b
    else:
        while i!=ile:
            a*=b
            lista.append(a)
            z+=1
print(ciag())


#Zad 7
def ciagzad7(* liczby):
    if len(liczby)==0:
        return 0
    else:
        wynik=liczby[]
        for i in liczby:
            wynik*=i
            return wynik
print(ciagzad7())


#Zad 8
produkty={"Czekolada"=3,"Piwo"=2.5,"Żurek"=5}

def listazakupow(** produkty):
    return len(produkty), sum(produkty.values())
