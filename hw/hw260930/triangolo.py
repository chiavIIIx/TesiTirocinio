from typing import List
from nagini_contracts.contracts import *

def triangolo(n: int) -> List[List[int]]:
    Requires(n >= 0)
    Ensures(list_pred(Result()))
    Ensures(len(Result()) == n)
    l: List[List[int]] = []
    i = 0
    while i < n:
        Invariant(list_pred(l))
        Invariant(Forall(l, lambda r: (list_pred(r), [[len(r)]])))
        Invariant(0 <= i and i <= n)
        Invariant(len(l) == i)
        Invariant(Forall(int, lambda k: Implies(0 <= k and k < i, len(l[k]) == k + 1)))
        riga: List[int] = []
        j = 0
        while j <= i:
            Invariant(list_pred(riga))
            Invariant(0 <= j and j <= i + 1)
            Invariant(len(riga) == j)
            Invariant(list_pred(l))
            Invariant(Forall(l, lambda r: (list_pred(r), [[len(r)]])))
            Invariant(len(l) == i)
            Invariant(Forall(int, lambda k: Implies(0 <= k and k < i, len(l[k]) == k + 1)))
            riga.append(j)
            j += 1
        l.append(riga)
        i += 1
    Assert(Forall(int, lambda k: Implies(0 <= k and k < n, len(l[k]) == k + 1)))
    return l