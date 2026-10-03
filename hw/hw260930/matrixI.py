from typing import List
from nagini_contracts.contracts import *

def matrixI(n: int) -> List[List[int]]:
    Requires(n >= 0)
    Ensures(list_pred(Result()))
    Ensures(len(Result()) == n)
    M: List[List[int]] = []
    i = 0
    while i < n:
        Invariant(list_pred(M))
        Invariant(Forall(M, lambda r: (list_pred(r), [[len(r)]])))
        Invariant(0 <= i and i <= n)
        Invariant(len(M) == i)
        Invariant(Forall(int, lambda k: Implies(0 <= k and k < i, len(M[k]) == n)))
        riga: List[int] = []
        j = 0
        while j < n:
            Invariant(list_pred(riga))
            Invariant(0 <= j and j <= n)
            Invariant(len(riga) == j)
            Invariant(list_pred(M))
            Invariant(Forall(M, lambda r: (list_pred(r), [[len(r)]])))
            Invariant(len(M) == i)
            Invariant(Forall(int, lambda k: Implies(0 <= k and k < i, len(M[k]) == n)))
            riga.append(1 if i == j else 0)
            j += 1
        M.append(riga)
        i += 1
    Assert(Forall(int, lambda k: Implies(0 <= k and k < n, len(M[k]) == n)))
    return M