from langdetect import detect_langs
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 📦 Chargement modèle TinyLLaMA
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model.eval()

# 🌍 Détection personnalisée
def detect_langue_personnalisee(texte):
    texte = texte.lower()
    if any(mot in texte for mot in ["mi yé", "i yé", "bɛ", "fɛ"]):  # Dioula
        return "diu"
    elif any(mot in texte for mot in ["ba yô", "man gbè", "gnin nan", "n’dè"]):  # Baoulé
        return "bau"
    else:
        try:
            langues = detect_langs(texte)
            return langues[0].lang if langues[0].prob > 0.90 else "en"
        except:
            return "en"

# 🤖 Fonction principale
def get_bot_response(message):
    langue = detect_langue_personnalisee(message)

    personalities = {
        "fr": "Tu es un assistant francophone, clair et chaleureux.",
        "en": "You are an assistant who speaks English, friendly and helpful.",
        "diu": "You are a culturally aware Dioula-speaking assistant.",
        "bau": "You are a respectful and proud Baoulé assistant."
    }

    style = personalities.get(langue, personalities["en"])

    # 💬 Création du prompt TinyLLaMA
# prompt dynamique basé sur la langue
    prompt = f'<|system|>\nYou are a helpful assistant. Always reply in {langue}.\n<|user|>\n{message}\n<|assistant|>'

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
            top_k=50,
            pad_token_id=tokenizer.eos_token_id
        )

    texte_genere = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return texte_genere.split("<|assistant|>")[-1].strip()
