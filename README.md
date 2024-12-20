
# Comuni Italiani

Una libreria Python per ottenere informazioni sui comuni italiani, basata sui dati ufficiali dell'ISTAT.

## **Funzionalità**
- Cerca un comune per nome e ottieni informazioni dettagliate (es. codice catastale, sigla provincia, ecc.).
- Ottieni una lista di comuni per provincia.
- Cerca un comune per codice catastale.
- Aggiornamento automatico dei dati con l'ultima versione disponibile sul sito dell'ISTAT.

---

## **Installazione**
Puoi installare la libreria direttamente da PyPI:

```bash
pip install comuniitaliani
```

---

## **Utilizzo**
Ecco come utilizzare la libreria per le operazioni principali:

### **Cercare un comune per nome**
```python
from comuniitaliani import Comuni

comuni = Comuni()

# Cerca un comune
info = comuni.cerca_comune("Agliè")
print(info)
```

**Output Esempio:**
```json
{
    "nome": "Agliè",
    "sigla_provincia": "TO",
    "codice_catastale": "A074",
    "provincia": "Torino",
    "regione": "Piemonte"
}
```

---

### **Elencare i comuni di una provincia**
```python
from comuniitaliani import Comuni

comuni = Comuni()

# Ottieni tutti i comuni della provincia di Torino
provincia_comuni = comuni.comuni_per_provincia("TO")
print(provincia_comuni[:5])  # Mostra i primi 5 comuni
```

**Output Esempio:**
```json
[
    {"nome": "Agliè", "sigla_provincia": "TO", "codice_catastale": "A074"},
    {"nome": "Airasca", "sigla_provincia": "TO", "codice_catastale": "A109"},
    {"nome": "Ala di Stura", "sigla_provincia": "TO", "codice_catastale": "A117"},
    ...
]
```

---

### **Cercare un comune per codice catastale**
```python
from comuniitaliani import Comuni

comuni = Comuni()

# Cerca un comune per codice catastale
info = comuni.cerca_per_codice_catastale("A074")
print(info)
```

**Output Esempio:**
```json
{
    "nome": "Agliè",
    "sigla_provincia": "TO",
    "codice_catastale": "A074",
    "provincia": "Torino",
    "regione": "Piemonte"
}
```

---

## **Aggiornamento Automatico**
La libreria verifica automaticamente se il dataset ISTAT è aggiornato e lo scarica se necessario.

---

## **Dipendenze**
Questa libreria utilizza:
- **pandas**: per la gestione e manipolazione dei dati.
- **requests**: per scaricare il dataset ISTAT.

---

## **Contribuire**
Se vuoi contribuire alla libreria:
1. Fai un fork del repository.
2. Crea un branch per le tue modifiche:
   ```bash
   git checkout -b nome-branch
   ```
3. Fai un commit delle modifiche:
   ```bash
   git commit -m "Descrizione delle modifiche"
   ```
4. Fai un push del branch:
   ```bash
   git push origin nome-branch
   ```
5. Apri una Pull Request.

---

## **Licenza**
Questa libreria è distribuita sotto la licenza MIT. Consulta il file [LICENSE](./LICENSE) per maggiori dettagli.

---

## **Link Utili**
- [Repository GitHub](https://github.com/cvrboni/comuniitaliani)
- [PyPI Package](https://pypi.org/project/comuniitaliani)
- [Dataset ISTAT](https://www.istat.it/it/archivio/6789)
