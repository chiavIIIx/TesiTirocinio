from qiskitStub import QuantumCircuit
from nagini_contracts.contracts import *

def deutsch_nb(n: int, tipo: int) -> QuantumCircuit:
    Requires(n >= 1 and 0 <= tipo and tipo <= 3) #sostituisce raise ValueError
    
    Ensures(Acc(Result().num_qubits) and Result().num_qubits == n + 1)
    Ensures(Acc(Result().num_clbits) and Result().num_clbits == n)
    Ensures(Acc(Result().gates))
    #ogni riga lega un tipo di oracolo al numero di porte
    Ensures(Implies(tipo == 0, Result().gates == 3 * n + 2))
    Ensures(Implies(tipo == 1, Result().gates == 3 * n + 3))
    Ensures(Implies(tipo == 2, Result().gates == 4 * n + 2))
    Ensures(Implies(tipo == 3, Result().gates == 3 * n + 3))
    
    qc = QuantumCircuit(n+1, n)
    qc.x(n)

    # H su tutti gli n + 1 qubit
    i = 0
    while i < n + 1:
        # permessi vanno ripetuti perchè nagini dimentica tutto ciò che non è nell'invariante
        Invariant(Acc(qc.num_qubits) and qc.num_qubits == n + 1)
        Invariant(Acc(qc.num_clbits) and qc.num_clbits == n)
        Invariant(Acc(qc.gates) and qc.gates == 1 + i) #numero porte è il numero di iterazioni + 1 (la porta x fuori dal ciclo)
        Invariant(0 <= i and i <= n + 1)
        qc.h(i)
        i += 1

    #oracolo
    if tipo == 0:                      # f(x)=0 -> porte sono n+2 (n+1 H dal ciclo e 1X)
        pass
    elif tipo == 1:                    # f(x)=1 -> porte sono n+3
        qc.x(n)
    elif tipo == 2:                    # f(x)=parità dei bit di x -> porte sono 2n+2 (n+2+ n porte cx)
        j = 0
        while j < n:
            Invariant(Acc(qc.num_qubits) and qc.num_qubits == n + 1)
            Invariant(Acc(qc.num_clbits) and qc.num_clbits == n)
            Invariant(Acc(qc.gates) and qc.gates == n + 2 + j)
            Invariant(0 <= j and j <= n)
            qc.cx(j, n)
            j += 1
    elif tipo == 3:                    # f(x)=primo bit di x -> porte sono n+3
        qc.cx(0, n)

    # H sui qubit di dati
    base = qc.gates          # porte presenti PRIMA del ciclo -> serve perché il numero di porte dipende dal tipo di oracolo
    i = 0
    while i < n:
        Invariant(Acc(qc.num_qubits) and qc.num_qubits == n + 1)
        Invariant(Acc(qc.num_clbits) and qc.num_clbits == n)
        Invariant(Acc(qc.gates) and qc.gates == base + i)
        Invariant(0 <= i and i <= n)
        qc.h(i)
        i += 1
    # Misura dei qubit di dati
    base = qc.gates          
    i = 0
    while i < n:
        Invariant(Acc(qc.num_qubits) and qc.num_qubits == n + 1)
        Invariant(Acc(qc.num_clbits) and qc.num_clbits == n)
        Invariant(Acc(qc.gates) and qc.gates == base + i)
        Invariant(0 <= i and i <= n)
        qc.measure(i, i)
        i += 1
    
    return qc