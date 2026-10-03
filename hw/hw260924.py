from typing import List

# inserisce in una lista i numeri da 0 a n-1
# output di dimensione n
def f1(n: int) -> List[int]:
    l: List[int] = []
    for i in range(n):
        l.append(i)
    return l


# primi n numeri della sequenza di Fibonacci
# output di dimensione n
def nFibonacci(n: int) -> List[int]:
    f: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        f.append(a)
        a, b = b, a + b
    return f


# triangolo -> [[0], [0, 1], [0, 1, 2], ...]
# output di dimensione n(n+1)/2
def triangolo(n: int) -> List[List[int]]:
    l: List[List[int]] = []
    for i in range(n):
        riga: List[int] = []
        j = 0
        while j <= i:
            riga.append(j)
            j += 1
        l.append(riga)
    return l


# crea matrice identità nxn
# output di dimensione n^2
def matrixI(n: int) -> List[List[int]]:
    M: List[List[int]] = []
    for i in range(n):
        riga: List[int] = []
        for j in range(n):
            riga.append(1 if i == j else 0)
        M.append(riga)
    return M


# insieme delle parti di {0, ..., n-1}
# output di dimensione 2^n
def sottoinsiemi(n: int) -> List[List[int]]:
    s: List[List[int]] = [[]]
    for k in range(n):
        new: List[List[int]] = []
        for j in s:
            new.append(j + [k])
        s = s + new
    return s