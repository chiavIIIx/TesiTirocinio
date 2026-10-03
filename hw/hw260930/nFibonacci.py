from typing import List
from nagini_contracts.contracts import *

def nFibonacci(n: int) -> List[int]:
    Requires(n >= 0)
    Ensures(list_pred(Result()))
    Ensures(len(Result()) == n)
    f: List[int] = []
    a, b = 0, 1
    i = 0
    while i < n:
        Invariant(list_pred(f))
        Invariant(i <= n)
        Invariant(len(f) == i)
        f.append(a)
        a, b = b, a + b #assegnazione simultanea permessa da nagini
        i += 1
    return f