# 🤖 Chatbot Flask (avec TinyLLaMA local)

Ce projet est un chatbot développé avec **Flask** et conçu pour intégrer un modèle IA de type LLaMA en local. Il met l'accent sur la **réduction des dépendances lourdes**, la **personnalisation linguistique** (Baoulé, Dioula), et une **architecture propre** adaptée aux environnements limités.

---

## 📁 Structure du dépôt

├── ai/ # Logique de traitement du chatbot ├── app.py  # Point d’entrée de l’application Flask ├── model_config.py # Paramètres du modèle IA local ├── setup.sh  # Script d’installation pour l’environnement local ├── templates/ # Pages HTML (interface utilisateur) ├── static/ # Fichiers CSS, JS, images ├── requirements.txt  # Dépendances Python ├── .gitignore # Fichiers exclus du dépôt

---

## ⚠️ Modèles LLaMA non inclus

Les dossiers `llama2_model/`, `llama_env/` et `test_llama_local.py` **ne sont pas poussés sur GitHub** pour éviter d’alourdir le dépôt.

> 💡 Pour utiliser le chatbot avec le modèle LLaMA, place les fichiers requis localement dans ton environnement selon cette structure :

llama2_model/ │ └── model.bin  llama_env/ │ └── tokenizer.model

---

## 🔧 Installation locale

1. Clone le repo :
```bash
git clone https://github.com/Charlem777/Chatbot_flask.git
cd Chatbot_flask
Crée un environnement virtuel :
bash
python -m venv .venv
source .venv/bin/activate
Installe les dépendances :
bash
pip install -r requirements.txt
Lance le chatbot :
bash
python app.py
