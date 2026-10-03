from typing import List
from nagini_contracts.contracts import *

def f1(n: int) -> List[int]:
    Requires(n >= 0) #precondizione
    Ensures(list_pred(Result())) #permesso sulla lista
    Ensures(len(Result()) == n) #postcondizione , ciò che vogliamo dimostrare
    l: List[int] = []
    i = 0
    while i < n:
        #invariante vera per ogni iterazione
        Invariant(list_pred(l)) # senza questo append fallirebbe per mancanza di permessi
        Invariant(i <= n)
        Invariant(len(l) == i) #punto fondamentale per la dimostrazione della postcondizione
        l.append(i)
        i += 1
    return l