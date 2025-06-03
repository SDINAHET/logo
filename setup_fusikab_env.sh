#!/bin/bash

# Supprimer ancien venv s'il existe
rm -rf venv_fusikab

# Créer environnement virtuel
python3 -m venv venv_fusikab
source venv_fusikab/bin/activate

# Mettre à jour pip
pip install --upgrade pip

# Installer MoviePy version stable avec editor.py
pip install "moviepy==1.0.3"

# Vérification
if [ -f "venv_fusikab/lib/python3.10/site-packages/moviepy/editor.py" ]; then
    echo "✅ moviepy.editor est bien installé !"
else
    echo "❌ editor.py est toujours manquant. Échec installation."
    exit 1
fi

# Lancer le script
python3 fusikab_script.py
