# [qui le righe 1-11 dell'originale: header di licenza Apache]
#
# Modificato da Caterina Chiavellati: versione semplificata di _zero_reflection
# per la verifica con Nagini (mcx_mode fissato a "noancilla", niente registri).

from typing import List
from nagini_contracts.contracts import *
from stubGrover import QuantumCircuit

def _state_preparation(num_state_qubits: int, qubits: List[int]) -> QuantumCircuit:
    Requires(num_state_qubits > 0)
    Requires(Acc(list_pred(qubits), 1/2))
    Requires(len(qubits) >= 1)
    Requires(Forall(int, lambda i: Implies(0 <= i and i < len(qubits),
                                           0 <= qubits[i] and qubits[i] < num_state_qubits)))

    Ensures(Acc(list_pred(qubits), 1/2))
    Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
    Ensures(Result().num_qubits == num_state_qubits)
    Ensures(Result().gates == len(qubits))
    Ensures(Result().num_clbits == 0)

    hadamards = QuantumCircuit(num_state_qubits, 0)
    hadamards.h_list(qubits)
    return hadamards
    
def _zero_reflection(num_state_qubits: int, qubits: List[int]) -> QuantumCircuit:
    Requires(num_state_qubits > 0)
    Requires(Acc(list_pred(qubits), 1/2))
    Requires(len(qubits) >= 1)
    Requires(Forall(int, lambda i: Implies(0 <= i and i < len(qubits), 0 <= qubits[i] and qubits[i] < num_state_qubits)))

    Ensures(Acc(list_pred(qubits), 1/2))
    Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
    Ensures(Result().num_qubits == num_state_qubits)
    Ensures(Implies(len(qubits) == 1, Result().gates == 3))
    Ensures(Implies(len(qubits) > 1, Result().gates == 2 * len(qubits) + 3))
    Ensures(Result().num_clbits == 0)

    reflection = QuantumCircuit(num_state_qubits, 0)

    reflection.x_list(qubits)
    if len(qubits) == 1:
        reflection.z(qubits[0])
    else:
        target = qubits[len(qubits) - 1]
        controls = qubits[:len(qubits) - 1]
        reflection.h(target)
        reflection.mcx(controls, target)
        reflection.h(target)
    reflection.x_list(qubits)

    return reflection

def _build(oracle: QuantumCircuit, qubits: List[int]) -> QuantumCircuit:
    Requires(Acc(oracle.num_qubits, 1/2) and Acc(oracle.gates, 1/2))
    Requires(oracle.num_qubits > 0)
    Requires(Acc(list_pred(qubits)))
    Requires(len(qubits) >= 1)
    Requires(Forall(int, lambda i: Implies(0 <= i and i < len(qubits), 0 <= qubits[i] and qubits[i] < oracle.num_qubits)))

    Ensures(Acc(oracle.num_qubits, 1/2) and Acc(oracle.gates, 1/2))
    Ensures(Acc(list_pred(qubits)))
    Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
    Ensures(Result().num_qubits == oracle.num_qubits)
    Ensures(Implies(len(qubits) == 1, Result().gates == oracle.gates + 5))
    Ensures(Implies(len(qubits) > 1, Result().gates == oracle.gates + 4 * len(qubits) + 3))
    Ensures(Result().num_clbits == 0)
    Ensures(len(qubits) == Old(len(qubits)))

    n = oracle.num_qubits
    circuit = QuantumCircuit(n, 0)

    circuit.compose(oracle)

    a = _state_preparation(n, qubits)
    a_inv = a.inverse()
    circuit.compose(a_inv)

    s0 = _zero_reflection(n, qubits)
    circuit.compose(s0)

    a2 = _state_preparation(n, qubits)
    circuit.compose(a2)

    return circuit

def _all_qubits(n: int) -> List[int]:
    Requires(n > 0)
    Ensures(Acc(list_pred(Result())))
    Ensures(len(Result()) == n)
    Ensures(Forall(int, lambda j: Implies(0 <= j and j < n, Result()[j] == j)))

    qubits: List[int] = []
    i = 0
    while i < n:
        Invariant(Acc(list_pred(qubits)))
        Invariant(0 <= i and i <= n)
        Invariant(len(qubits) == i)
        Invariant(Forall(int, lambda j: Implies(0 <= j and j < i, qubits[j] == j)))
        qubits.append(i)
        i = i + 1
    return qubits

def construct_circuit(oracle: QuantumCircuit, k: int) -> QuantumCircuit:
    Requires(Acc(oracle.num_qubits) and Acc(oracle.gates))
    Requires(oracle.num_qubits > 0)
    Requires(k >= 0)

    Ensures(Acc(oracle.num_qubits) and Acc(oracle.gates))
    Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
    Ensures(Result().num_qubits == oracle.num_qubits)
    Ensures(Implies(oracle.num_qubits == 1,
                    Result().gates == 1 + k * (oracle.gates + 5)))
    Ensures(Implies(oracle.num_qubits > 1,
                    Result().gates == oracle.num_qubits + k * (oracle.gates + 4 * oracle.num_qubits + 3)))

    n = oracle.num_qubits
    qubits = _all_qubits(n)

    qc = QuantumCircuit(n, 0)
    prep = _state_preparation(n, qubits)
    qc.compose(prep)

    if k > 0:
        q = _build(oracle, qubits)
        qk = q.power(k)
        qc.compose(qk)

    return qc