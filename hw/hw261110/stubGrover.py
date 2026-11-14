from nagini_contracts.contracts import *

from typing import List

class QuantumCircuit:
    def __init__(self, num_qubits: int, num_clbits: int) -> None:
        Requires(num_qubits > 0 and num_clbits >= 0)
        
        Ensures(Acc(self.num_qubits) and self.num_qubits == num_qubits)
        Ensures(Acc(self.num_clbits) and self.num_clbits == num_clbits)
        Ensures(Acc(self.gates) and self.gates == 0)    
        
        self.num_qubits: int = num_qubits
        self.num_clbits: int = num_clbits
        self.gates: int = 0

    def x(self, qubit: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Requires(0 <= qubit and qubit < self.num_qubits)
        
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1

    def x_list(self, qubits: List[int]) -> None:
        Requires(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Requires(Acc(list_pred(qubits), 1/4))
        Requires(Forall(int, lambda i: Implies(0 <= i and i < len(qubits), 0 <= qubits[i] and qubits[i] < self.num_qubits)))

        Ensures(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Ensures(Acc(list_pred(qubits), 1/4))
        Ensures(self.gates == Old(self.gates) + len(qubits))

        self.gates = self.gates + len(qubits)

    def h(self, qubit: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Requires(0 <= qubit and qubit < self.num_qubits)
        
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1

    def h_list(self, qubits: List[int]) -> None:
            Requires(Acc(self.num_qubits, 1/4) and Acc(self.gates))
            Requires(Acc(list_pred(qubits), 1/4))
            Requires(Forall(int, lambda i: Implies(0 <= i and i < len(qubits), 0 <= qubits[i] and qubits[i] < self.num_qubits)))
    
            Ensures(Acc(self.num_qubits, 1/4) and Acc(self.gates))
            Ensures(Acc(list_pred(qubits), 1/4))
            Ensures(self.gates == Old(self.gates) + len(qubits))
    
            self.gates = self.gates + len(qubits)

    def z(self, qubit: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Requires(0 <= qubit and qubit < self.num_qubits)
            
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1

    def cx(self, control: int, target: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Requires(0 <= control and control < self.num_qubits)
        Requires(0 <= target and target < self.num_qubits)
        Requires(control != target)
        
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1

    def mcx(self, controls: List[int], target: int) -> None:
        Requires(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Requires(Acc(list_pred(controls), 1/4))
        Requires(len(controls) >= 1)
        Requires(Forall(int, lambda i: Implies(0 <= i and i < len(controls), 0 <= controls[i] and controls[i] < self.num_qubits)))
        Requires(0 <= target and target < self.num_qubits)

        Ensures(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Ensures(Acc(list_pred(controls), 1/4))
        Ensures(self.gates == Old(self.gates) + 1)

        self.gates = self.gates + 1

    def measure(self, qubit: int, clbit: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates))
        Requires(0 <= qubit and qubit < self.num_qubits)
        Requires(0 <= clbit and clbit < self.num_clbits)
        
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1

    def inverse(self) -> 'QuantumCircuit':
        Requires(Acc(self.num_qubits, 1/4) and Acc(self.num_clbits, 1/4) and Acc(self.gates, 1/4))
        Requires(self.num_qubits > 0 and self.num_clbits >= 0)

        Ensures(Acc(self.num_qubits, 1/4) and Acc(self.num_clbits, 1/4) and Acc(self.gates, 1/4))
        Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
        Ensures(Result().num_qubits == self.num_qubits)
        Ensures(Result().num_clbits == self.num_clbits)
        Ensures(Result().gates == self.gates)

        inv = QuantumCircuit(self.num_qubits, self.num_clbits)
        inv.gates = self.gates
        return inv
    
    def compose(self, other: 'QuantumCircuit') -> None:
        Requires(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Requires(Acc(other.num_qubits, 1/4) and Acc(other.gates, 1/4))
        Requires(other.num_qubits <= self.num_qubits)

        Ensures(Acc(self.num_qubits, 1/4) and Acc(self.gates))
        Ensures(Acc(other.num_qubits, 1/4) and Acc(other.gates, 1/4))
        Ensures(self.gates == Old(self.gates) + other.gates)

        self.gates = self.gates + other.gates

    def power(self, k: int) -> 'QuantumCircuit':
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates, 1/2))
        Requires(self.num_qubits > 0 and self.num_clbits >= 0)
        Requires(k >= 0)

        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates, 1/2))
        Ensures(Acc(Result().num_qubits) and Acc(Result().num_clbits) and Acc(Result().gates))
        Ensures(Result().num_qubits == self.num_qubits)
        Ensures(Result().num_clbits == self.num_clbits)
        Ensures(Result().gates == k * self.gates)

        rep = QuantumCircuit(self.num_qubits, self.num_clbits)
        i = 0
        while i < k:
            Invariant(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates, 1/2))
            Invariant(Acc(rep.num_qubits) and Acc(rep.num_clbits) and Acc(rep.gates))
            Invariant(rep.num_qubits == self.num_qubits and rep.num_clbits == self.num_clbits)
            Invariant(0 <= i and i <= k)
            Invariant(rep.gates == i * self.gates)
            rep.compose(self)
            i = i + 1
        return rep    