from setuptools import setup, find_packages

setup(
    name="comuniitaliani",  # Nome del pacchetto
    version="0.1.0",  # Versione iniziale
    description="Libreria Python per ottenere informazioni sui comuni italiani dal file ISTAT",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",  # Specifica il tipo di README
    author="Andrea Carboni",  # Inserisci il tuo nome
    author_email="andreacarboni@stepservizi.net",  # Inserisci il tuo indirizzo email
    url="https://github.com/cvrboni/comuniitaliani",  # Link al repository (opzionale)
    packages=find_packages(),  # Trova automaticamente i pacchetti nella directory
    include_package_data=True,  # Include i file non-Python (es. JSON)
    package_data={
        "comuniitaliani": ["database/comuni.csv"]  # Specifica i file extra da includere
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Licenza, es. MIT
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versione minima di Python
    install_requires=[],  # Dipendenze (lascia vuoto se non ci sono)
)
