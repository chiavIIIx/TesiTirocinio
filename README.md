# tesi_tirocinio

Materiale per tesi e tirocinio: verifica formale di codice Python con Nagini e studio del calcolo quantistico con Qiskit.

## Struttura della cartella
* I nomi dei compiti seguono il formato `hwAAMMGG` (anno, mese, giorno della consegna).
```
tesi_tirocinio/
├── README.md
├── .gitignore
├── hw/                          compiti assegnati dal relatore
│   ├── hw260924.py              consegna del 24/09/2026
│   └── hw260930/                consegna del 30/09/2026
├── libriQuantum/                libri (non su git)
├── qiskit-pocket-guide-main/    codice di esempio del Qiskit Pocket Guide
└── EilersMueller18.pdf          paper di Nagini (non su git)
```

## Compiti

### hw260924: funzioni con output crescente in n

* **Consegna:** scrivere cinque o sei funzioni Python che, dato in input un intero n, restituiscono una lista (o una lista di liste) di dimensione crescente in n, via via più complesse.

### hw260930: verifica con Nagini

* **Consegna:** annotare con Nagini le funzioni di hw260924 per derivare statement sulla lunghezza dell'output in funzione di n.


## Ambienti

- **`nagini`** (conda, Python 3.9): per Nagini. Va selezionato anche come interprete in VS Code (Cmd+Shift+P, "Python: Select Interpreter"), altrimenti l'editor segnala come non definiti `Requires`, `Ensures`, ecc.
- **`qiskit-book`** (conda, Python 3.10): per Qiskit e il notebook del libro.

## Come lanciare Nagini

```bash
conda activate nagini
cd hw/hw260930
nagini f1.py
```

Esito atteso: `Verification successful`, oppure l'elenco degli errori con riga e colonna (`file.py@riga.colonna`).

## Problemi noti e soluzioni

- **Warning "relevancy must be enabled to use option CASE_SPLIT"**: viene da Z3, è innocuo e si può ignorare.
- **Crash "'NoneType' object has no attribute 'path'"**: cancellare le cache di Nagini con `rm -rf .mypy_cache_strict .mypy_cache_nonstrict` nella cartella da cui si lancia Nagini.
- **Tempi di verifica di 15-25 secondi anche per funzioni banali**: è il costo fisso di avvio (JVM, Viper, Z3), non dipende dal codice.

## Letture

- **Nagini:** Eilers e Müller, *Nagini: A Static Verifier for Python* (2018), `EilersMueller18.pdf`.
- **Qiskit:** Weaver e Harkins, *Qiskit Pocket Guide* (O'Reilly, 2022), in `libriQuantum/`. Il codice di esempio è in `qiskit-pocket-guide-main/`.
- **Mermin:** in `libriQuantum/`.