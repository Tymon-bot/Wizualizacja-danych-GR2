def nElemement(a1, n, r):
    return a1 + (n - 1) * r


#wzór na n-ty element ciągu
def nElement(ak, k, n, r):
    return ak + (n - k) * r


#dla sumy
def sumaArytma(a1, an, n):
    return ((a1 + an) / 2) * n


# wzór na wyraz środkowy
def wyrazSrodkowyArytma(x, z):
    return (x + z) / 2