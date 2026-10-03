from typing import List
from nagini_contracts.contracts import *

def sottoinsiemi(n: int) -> List[List[int]]:
    Requires(n >= 0)
    Ensures(list_pred(Result()))
    Ensures(len(Result()) == 2 ** n)
    vuoto: List[int] = []
    s: List[List[int]] = [vuoto]
    k = 0
    while k < n:
        Invariant(list_pred(s))
        Invariant(Forall(s, lambda x: (list_pred(x), [[len(x)]])))
        Invariant(0 <= k and k <= n)
        Invariant(len(s) == 2 ** k)
        new: List[List[int]] = []
        j = 0
        while j < len(s):
            Invariant(list_pred(s))
            Invariant(Forall(s, lambda x: (list_pred(x), [[len(x)]])))
            Invariant(len(s) == 2 ** k)
            Invariant(list_pred(new))
            Invariant(Forall(new, lambda x: (list_pred(x), [[len(x)]])))
            Invariant(0 <= j and j <= len(s))
            Invariant(len(new) == j)
            new.append(s[j] + [k])
            j += 1
        s = s + new
        k += 1
    return s