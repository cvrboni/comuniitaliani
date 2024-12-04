# Comuni Italiani

Una libreria Python per ottenere informazioni sui comuni italiani basata su un dataset JSON.

## Funzionalità
- Cerca un comune per nome
- Ottieni tutti i comuni di una provincia

## Installazione
```bash
pip install comuniitaliani
```

## Utilizzo
```python
from comuniitaliani import Comuni

comuni = Comuni()

# Cerca un comune
info = comuni.cerca_comune("Agliè")
print(info)

# Ottieni comuni di una provincia
provincia_comuni = comuni.comuni_per_provincia("TO")
print(provincia_comuni)
```

