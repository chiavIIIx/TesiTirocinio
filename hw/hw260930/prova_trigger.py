from typing import List
from nagini_contracts.contracts import *

def prova8(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(l, lambda r: (list_pred(r), [[len(r)]])))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))

def prova9(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(l, lambda r: (list_pred(r), [])))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))
    