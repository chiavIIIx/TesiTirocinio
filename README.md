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
│   ├── hw260924/                
│   ├── hw260930/                
│   ├── hw261008/                
│   ├── hw261022/                
│   └── hw261110/                
├── grover/                      file originali di Qiskit per Grover (non modificati)
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

* **Consegna:** familiarizzare con la programmazione in Qiskit tramite semplici programmi Python, seguendo il *Qiskit Pocket Guide*; in parallelo capire il concetto di stub per le librerie, che servirà per "insegnare" a Nagini cosa sono i circuiti (il circuito gioca il ruolo della lista).

### hw261022: verifica di Deutsch-Jozsa con Nagini

* **Consegna:** dimostrare con Nagini i risultati attesi su Deutsch-Jozsa con n bit di input. Gli obiettivi indicati dal relatore sono esempi con un numero di qubit dipendente dall'input, che usino più funzioni di Qiskit e che contengano cicli.

### hw261110: verifica del codice originale di Qiskit (Grover, poi QFT e Shor)

* **Consegna:** prendere il codice con cui Qiskit implementa Grover, QFT e Shor e verificarne con Nagini dei limiti sul numero di porte, come fatto per Deutsch. Si parte da Grover.
* **Codice di partenza** (da qiskit-terra 0.46, ambiente `qiskit-book`), copiato senza modifiche in `grover/`:
    * `grover_operator_originale.py`: da `qiskit/circuit/library/grover_operator.py`, classe `GroverOperator` (una singola iterazione di Grover)
    * `grover_originale.py`: da `qiskit/algorithms/amplitude_amplifiers/grover.py`, classe `Grover` (algoritmo completo; interessa solo `construct_circuit`)

* **Trasformazioni rispetto al codice originale** (regole candidate per il traduttore automatico):
    * `mcx_mode` fissato a `"noancilla"` (il default di `GroverOperator`): il blocco delle ancille e il parametro spariscono
    * registri, nomi e `name=` tolti: `QuantumCircuit(QuantumRegister(n), name=...)` diventa `QuantumCircuit(n, 0)`
    * metodi su liste separati da quelli su qubit singolo: `x(lista)` diventa `x_list(lista)`, `h(lista)` diventa `h_list(lista)`
    * indici negativi e slicing riscritti: `qubits[-1]` diventa `qubits[len(qubits) - 1]`, `qubits[:-1]` diventa `qubits[:len(qubits) - 1]`
    * una property che usa `self` solo in lettura diventa una funzione libera che riceve quei dati come parametri (`state_preparation` diventa `_state_preparation(num_state_qubits, qubits)`)
    * rimosso il ramo con la preparazione di stato fornita dall'utente: si considera il Grover standard con le H
* **Correzione di un errore del codice originale:** in `_zero_reflection`, con un solo qubit di riflessione, Qiskit applica `z(0)` invece di `z(qubits[0])`. Con `reflection_qubits = [3]` la riflessione agirebbe sul qubit sbagliato. Nella versione verificata si usa `z(qubits[0])`; il numero di porte non cambia, quindi il modello attuale non può rilevare l'errore.
* **Metodi aggiunti allo stub di `QuantumCircuit`:** `z`, `x_list`, `h_list`, `mcx`, `inverse`, `compose`.
* **Semplificazioni del modello:**
    * `mcx` conta come una porta e non controlla che il target sia diverso dai controlli
    * `compose` modella solo `inplace=True`, ignora la lista dei qubit e i bit classici, e non permette di comporre un circuito con se stesso
    * `inverse` restituisce un circuito nuovo con gli stessi qubit e le stesse porte
* **Decisioni aperte da discutere con il relatore:**
    * contare le porte "impacchettate" (`_build` chiude l'operatore in un unico gate con `to_gate()`) o "srotolate"
    * se barrier e misure contano come porte
    * se MCX conta come una porta o come la sua decomposizione (che dipende da `mcx_mode`)

## Ambienti

- **`nagini`** (conda, Python 3.9, Nagini 1.2.0): prima versione usata.
- **`nagini13`** (conda, Python 3.12, Nagini 1.3.1, openjdk nell'ambiente): versione usata da hw261022. Va selezionato anche come interprete in VS Code (Cmd+Shift+P, "Python: Select Interpreter"), altrimenti l'editor segnala come non definiti `Requires`, `Ensures`, ecc.
- **`qiskit-book`** (conda, Python 3.10, qiskit-terra 0.46): per Qiskit e i notebook. Va selezionato come kernel del notebook in VS Code.

## Come lanciare Nagini

```bash
conda activate nagini13
cd hw/hw261022
nagini Deutsch.py
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
- **Type error "Cannot determine type of ..."** nello stub: i campi compaiono nei contratti del costruttore prima di essere assegnati. Dichiararne il tipo all'assegnazione, ad esempio `self.num_qubits: int = num_qubits`.
- **Type error "Module ... has no attribute ..."**: il file importato non contiene la classe cercata. Controllare che il file stub sia nella cartella da cui si lancia Nagini, che il nome nell'import coincida con il nome del file e che la classe non sia commentata; poi cancellare le cache.
- **"Loop invariant might not be preserved"**: l'invariante non resta vero dopo un giro del ciclo. Per il numero di porte salvare il valore iniziale prima del ciclo (`base = qc.gates`) e scrivere `qc.gates == base + i`, non `qc.gates == qc.gates + i`.
- **"The precondition of method ... might not hold" alla seconda chiamata su una lista**: il chiamante ha ceduto tutto il suo permesso sulla lista, quindi al ritorno Nagini non sa più nulla del suo contenuto né della sua lunghezza. Negli stub chiedere una frazione più piccola di quella del chiamante (ad esempio 1/4 negli stub e 1/2 nelle funzioni che li chiamano): il chiamante tiene una parte del permesso e la lista resta "congelata".
- **"There might be insufficient permission to access list_pred(...)"**: il chiamante possiede una frazione minore di quella richiesta dal metodo chiamato. Controllare che le frazioni siano coerenti tra stub e funzioni.
- **Metodo dello stub senza corpo**: un metodo che contiene solo contratti viene trattato come astratto, cioè i contratti sono assunti veri senza verifica. Scrivere sempre anche il corpo (ad esempio `self.gates = self.gates + len(qubits)`).

### Qiskit

- **FutureWarning "The qiskit package is not installed, only qiskit-terra"**, **DeprecationWarning su BasicAer** e **DeprecationWarning su `qiskit.algorithms`** (migrato nel pacchetto `qiskit_algorithms`): sono avvisi, non errori.
- **Trovare il sorgente di una funzione di Qiskit**: `python -c "import qiskit.circuit.library.grover_operator as m; print(m.__file__)"` (con l'ambiente `qiskit-book` attivo).
- **CircuitError "Index 0 out of range for size 0"** su `measure`: il circuito non ha bit classici. Usare `QuantumCircuit(n, n)` oppure `measure_all()`.
- **QiskitError "Cannot apply instruction with classical bits: measure"**: `Statevector` e `Operator` non accettano circuiti con misure. Calcolarli prima di aggiungere le misure.

## Letture

- **Nagini:** Eilers e Müller, *Nagini: A Static Verifier for Python* (2018), `EilersMueller18.pdf`.
- **Nagini Wiki:** [github.com/marcoeilers/nagini/wiki](https://github.com/marcoeilers/nagini/wiki), linguaggio di specifica (`Requires`, `Ensures`, `Invariant`, `Acc`, funzioni pure).
- **Qiskit:** Weaver e Harkins, *Qiskit Pocket Guide* (O'Reilly, 2022), in `libriQuantum/`. Il codice di esempio è in `qiskit-pocket-guide-main/`.
- **Mermin:** in `libriQuantum/`.