# tesi_tirocinio

Materiale per tesi e tirocinio: verifica formale di codice Python con Nagini e studio del calcolo quantistico con Qiskit.

## Struttura della cartella
* I nomi dei compiti seguono il formato `hwAAMMGG` (anno, mese, giorno della consegna).
```
tesi_tirocinio/
├── README.md
├── .gitignore
├── .vscode/                     impostazioni di VS Code
├── hw/                          compiti assegnati dal relatore
│   ├── hw260924/                consegna del 24/09/2026
│   ├── hw260930/                consegna del 30/09/2026
│   └── hw261008/                consegna dell'08/10/2026
├── libriQuantum/                libri (non su git)
├── qiskit-pocket-guide-main/    codice di esempio del Qiskit Pocket Guide
└── EilersMueller18.pdf          paper di Nagini (non su git)
```

## Compiti

### hw260924: funzioni con output crescente in n

* **Consegna:** scrivere cinque o sei funzioni Python che, dato in input un intero n, restituiscono una lista (o una lista di liste) di dimensione crescente in n, via via più complesse.

### hw260930: verifica con Nagini

* **Consegna:** annotare con Nagini le funzioni di hw260924 per derivare statement sulla lunghezza dell'output in funzione di n.

### hw261008: programmi di prova in Qiskit

* **Consegna:** familiarizzare con la programmazione in Qiskit tramite semplici programmi Python, seguendo il *Qiskit Pocket Guide*; in parallelo capire il concetto di stub per le librerie, che servirà per "insegnare" a Nagini cosa sono i circuiti (il circuito gioca il ruolo della lista). Per ora senza usare Nagini.

## Ambienti

- **`nagini`** (conda, Python 3.9): per Nagini. Va selezionato anche come interprete in VS Code (Cmd+Shift+P, "Python: Select Interpreter"), altrimenti l'editor segnala come non definiti `Requires`, `Ensures`, ecc.
- **`qiskit-book`** (conda, Python 3.10, qiskit-terra 0.46): per Qiskit e i notebook. Va selezionato come kernel del notebook in VS Code.

## Come lanciare Nagini

```bash
conda activate nagini
cd hw/hw260930
nagini f1.py
```

Esito atteso: `Verification successful`, oppure l'elenco degli errori con riga e colonna (`file.py@riga.colonna`).

## Differenze rispetto al Qiskit Pocket Guide

Il libro è scritto per Qiskit 0.20; alcune istruzioni sono deprecate dalla 0.46 e rimosse dalla 1.0. Sostituzioni usate negli esercizi:

- **`BasicAer`** → `BasicProvider().get_backend("basic_simulator")`, dal modulo `qiskit.providers.basic_provider` (solo conteggi).
- **`statevector_simulator` e `unitary_simulator`** → `Statevector(qc)` e `Operator(qc)` di `qiskit.quantum_info`, senza passare per un backend. Il circuito non deve contenere misure.
- **`execute(qc, backend)`** → `transpile(qc, backend)` seguito da `backend.run(...)`.
- **`qiskit.opflow`** (Operator Flow, es. `H^n`) → `QuantumCircuit` con i metodi `h`, `cx`.
- **`qc.draw('mpl')`** → `qc.draw('mpl', style='iqp')`, per evitare il FutureWarning sullo stile predefinito.
- **Fonte:** [Qiskit v1.0 feature changes](https://quantum.cloud.ibm.com/docs/guides/qiskit-1.0-features).

## Problemi noti e soluzioni

### Nagini

- **Warning "relevancy must be enabled to use option CASE_SPLIT"**: viene da Z3, è innocuo e si può ignorare.
- **Crash "'NoneType' object has no attribute 'path'"**: cancellare le cache di Nagini con `rm -rf .mypy_cache_strict .mypy_cache_nonstrict` nella cartella da cui si lancia Nagini.
- **Tempi di verifica di 15-25 secondi anche per funzioni banali**: è il costo fisso di avvio (JVM, Viper, Z3), non dipende dal codice.

### Qiskit

- **FutureWarning "The qiskit package is not installed, only qiskit-terra"** e **DeprecationWarning su BasicAer**: sono avvisi, non errori. 
- **CircuitError "Index 0 out of range for size 0"** su `measure`: il circuito non ha bit classici. Usare `QuantumCircuit(n, n)` oppure `measure_all()`.
- **QiskitError "Cannot apply instruction with classical bits: measure"**: `Statevector` e `Operator` non accettano circuiti con misure. Calcolarli prima di aggiungere le misure.

## Letture

- **Nagini:** Eilers e Müller, *Nagini: A Static Verifier for Python* (2018), `EilersMueller18.pdf`.
- **Qiskit:** Weaver e Harkins, *Qiskit Pocket Guide* (O'Reilly, 2022), in `libriQuantum/`. Il codice di esempio è in `qiskit-pocket-guide-main/`.
- **Mermin:** in `libriQuantum/`.