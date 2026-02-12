# Git Test5 - Sito Web Statico

Questo è un progetto di esempio con pagine HTML statiche.

## Come avviare il server

### Metodo 1: Script Python (Consigliato)

Per avviare il server locale, esegui:

```bash
python3 server.py
```

Il server sarà disponibile su: **http://localhost:8000**

Se vuoi usare una porta diversa:

```bash
python3 server.py 3000
```

### Metodo 2: Python HTTP Server (Comando diretto)

Se preferisci non usare lo script, puoi avviare il server direttamente con:

```bash
python3 -m http.server 8000
```

### Fermare il server

Premi `CTRL+C` per fermare il server.

## Pagine disponibili

- **Home**: http://localhost:8000/
- **Prodotti**: http://localhost:8000/prodotti.html
- **Pagamento Satispay**: http://localhost:8000/payment-satispay.html

## Requisiti

- Python 3.x (già installato sulla maggior parte dei sistemi)

## Risoluzione dei problemi

**Problema: "La porta 8000 è già in uso"**
- Soluzione: Usa una porta diversa con `python3 server.py 9000`

**Problema: "python3 non trovato"**
- Soluzione: Prova con `python server.py` invece di `python3 server.py`
