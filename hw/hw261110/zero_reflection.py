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