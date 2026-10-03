from typing import List
from nagini_contracts.contracts import *

def prova1(l: List[List[int]], i: int) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]))))
    Requires(len(l) == i)
    Requires(Forall(int, lambda k: Implies(0 <= k and k < i, len(l[k]) == k + 1)))

def prova2(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]))))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))

def prova3(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), Acc(list_pred(l[k])))))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))

def prova4(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]))))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))
    Ensures(list_pred(l))
    Ensures(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]))))
    Ensures(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))

def prova5(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]) and len(l[k]) == k + 1)))
    Ensures(list_pred(l))
    Ensures(Forall(int, lambda k: Implies(0 <= k and k < len(l), list_pred(l[k]) and len(l[k]) == k + 1)))

def prova6(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(int, lambda k: (Implies(0 <= k and k < len(l), list_pred(l[k])), [[l[k]]])))
    Requires(Forall(int, lambda k: (Implies(0 <= k and k < len(l), len(l[k]) == k + 1), [[l[k]]])))

def prova7(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(l, lambda r: list_pred(r)))
    Requires(Forall(int, lambda k: (Implies(0 <= k and k < len(l), len(l[k]) == k + 1), [[l[k]]])))

def prova8(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(l, lambda r: (list_pred(r), [[len(r)]])))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))

def prova9(l: List[List[int]]) -> None:
    Requires(list_pred(l))
    Requires(Forall(l, lambda r: (list_pred(r), [])))
    Requires(Forall(int, lambda k: Implies(0 <= k and k < len(l), len(l[k]) == k + 1)))