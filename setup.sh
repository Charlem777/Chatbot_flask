#!/bin/bash

echo "📦 Initialisation de l’environnement virtuel…"

# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement (macOS/Linux)
source venv/bin/activate

echo "📚 Installation des dépendances…"

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Tout est prêt ! Ton environnement est opérationnel."
