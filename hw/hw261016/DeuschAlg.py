from nagini_contracts.contracts import *
from qiskit_stub import QuantumCircuit

def deutsch(caso: int) -> QuantumCircuit:
    Requires(0 <= caso and caso <= 3)
    
    Ensures(Acc(Result().num_qubits) and Result().num_qubits == 2)
    Ensures(Acc(Result().num_clbits) and Result().num_clbits == 1)
    Ensures(Acc(Result().gates))
    # numero di porte per ciascuna funzione f
    Ensures(Implies(caso == 0, Result().gates == 5))   # f(x) = 0
    Ensures(Implies(caso == 1, Result().gates == 6))   # f(x) = x
    Ensures(Implies(caso == 2, Result().gates == 7))   # f(x) = NOT x
    Ensures(Implies(caso == 3, Result().gates == 6))   # f(x) = 1
    
    qc = QuantumCircuit(2, 1)
    qc.x(1)
    qc.h(0)
    qc.h(1)
    
    if caso == 0:
        pass
    elif caso == 1:
        qc.cx(0, 1)
    elif caso == 2:
        qc.cx(0, 1)
        qc.x(1)
    elif caso == 3:
        qc.x(1)
    qc.h(0)
    qc.measure(0, 0)
    return qc