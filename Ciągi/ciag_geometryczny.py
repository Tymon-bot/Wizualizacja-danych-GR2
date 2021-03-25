def nElementG(a1, q, n):
    return a1 * q ** (n - 1)


#Wzór na sume ciągu
def sumG(a1, n, q = 1):
    if(q == 1):
        return n * a1
    return a1 * ((1 - q ** n) / (1 - q))


# Wyraz Środkowy
def wyrazSrodkowyG(a, b):
    return sqrt(a * b)