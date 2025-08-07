
import streamlit as st
import datetime

st.set_page_config(page_title="Zarali – Bien-être Post-Partum", page_icon="🌸", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .main {
        background-color: #FFF9F9;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button {
        background-color: #FADADD;
        color: #333;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🌸 Bienvenue sur Zarali")
st.subheader("Ton alliée bienveillante pendant le post-partum")

# --- USER INPUT ---
nom = st.text_input("Quel est ton prénom ?", "")

if nom:
    st.success(f"Enchantée {nom} 💖 Ravie d’être avec toi aujourd’hui.")
    humeur = st.radio("Comment te sens-tu ?", ["Triste", "Fatiguée", "Stressée", "Bien", "Autre"])

    if humeur == "Triste":
        st.info("Je suis là pour toi. Tu veux peut-être une respiration guidée ou un mot doux ? 🌧️")
    elif humeur == "Fatiguée":
        st.info(f"Courage, {nom}. Même une micro-sieste peut changer la journée. 💤")
    elif humeur == "Stressée":
        st.info("Respire. Tu veux essayer une technique de relaxation rapide ? 🌿")
    elif humeur == "Bien":
        st.success("Je suis heureuse de lire ça ! ☀️ Continue à prendre soin de toi.")
    else:
        st.info("Merci de partager. Chaque émotion compte. Je suis là pour t’écouter. 💬")

    st.write("---")
    besoin = st.selectbox("Souhaites-tu aborder un sujet particulier ?", ["-", "Sommeil", "Corps", "Confiance", "Solitude", "Non, merci"])

    if besoin == "Sommeil":
        st.warning("Le sommeil est précieux. As-tu pu t'accorder un moment calme aujourd'hui ?")
    elif besoin == "Corps":
        st.warning("Ton corps est fort et mérite amour et douceur. 💗")
    elif besoin == "Confiance":
        st.warning("Tu es puissante. Voici une affirmation : _'Je fais de mon mieux, et c’est déjà énorme.'_")
    elif besoin == "Solitude":
        st.warning("Tu n’es pas seule. Je peux t’orienter vers des groupes de soutien si tu veux.")

    st.write("---")

    # --- JOURNAL DE BORD ÉMOTIONNEL ---
    st.header("📔 Mon journal de bord émotionnel")
    with st.form("journal_form"):
        entry = st.text_area("Exprime-toi librement ici :")
        submitted = st.form_submit_button("Enregistrer")
        if submitted and entry:
            with open("journal_zarali.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.date.today()} - {nom}: {entry}\n")
            st.success("Ton message a bien été enregistré. Merci de t'être confiée 💖")

    # --- FORUM ANONYME ---
    st.header("🗣️ Espace de partages anonymes")
    with st.form("forum_form"):
        anonymous_msg = st.text_area("Partage une pensée ou un témoignage (anonymement)")
        forum_submit = st.form_submit_button("Partager")
        if forum_submit and anonymous_msg:
            with open("forum_zarali.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.date.today()}: {anonymous_msg}\n")
            st.success("Ton message a été partagé anonymement. Merci 💜")

    st.write("💬 Témoignages récents :")
    try:
        with open("forum_zarali.txt", "r", encoding="utf-8") as f:
            messages = f.readlines()[-5:]  # derniers messages
            for msg in messages:
                st.info(msg.strip())
    except FileNotFoundError:
        st.warning("Aucun message encore partagé. Sois la première à t'exprimer.")

    # --- ANNUAIRE ---
    st.header("📍 Annuaire de professionnels")
    st.markdown("""
    - 👩‍⚕️ **Sage-femme** : Marie Dupont — [sagesfemmesparis.fr](https://sagesfemmesparis.fr)
    - 🧠 **Psychologue périnatale** : Claire Martin — [psyparis.fr](https://psyparis.fr)
    - 💆 **Massothérapeute post-natale** : Aïcha Diallo — [bienetrebebe.fr](https://bienetrebebe.fr)
    - 🤱 **Consultante allaitement** : Sophie B. — [allaiterfacile.com](https://allaiterfacile.com)
    """)
