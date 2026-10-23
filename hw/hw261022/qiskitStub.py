from nagini_contracts.contracts import *

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

    def h(self, qubit: int) -> None:
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

    def measure(self, qubit: int, clbit: int) -> None:
        Requires(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates))
        Requires(0 <= qubit and qubit < self.num_qubits)
        Requires(0 <= clbit and clbit < self.num_clbits)
        
        Ensures(Acc(self.num_qubits, 1/2) and Acc(self.num_clbits, 1/2) and Acc(self.gates))
        Ensures(self.gates == Old(self.gates) + 1)
        
        self.gates = self.gates + 1
