
import streamlit as st
from datetime import datetime

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
    .affirmation-box {
        background-color: #ffe6f0;
        border-left: 6px solid #ff66a3;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🌸 Bienvenue sur Zarali")
st.subheader("Ton alliée bienveillante pendant le post-partum")

nom = st.text_input("Quel est ton prénom ?", "")

if nom:
    st.success(f"Enchantée {nom} 💖 Ravie d’être avec toi aujourd’hui.")
    humeur = st.radio("Comment te sens-tu en ce moment ?", ["Triste", "Fatiguée", "Stressée", "Bien", "Autre"])

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

    if st.button("💾 Sauvegarder mon humeur"):
        with open("humeurs_log.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {nom} : {humeur}\n")
        st.success("Ton ressenti a bien été sauvegardé 🌸")

    st.write("---")
    besoin = st.selectbox("Souhaites-tu parler d’un thème particulier ?", ["-", "Sommeil", "Corps", "Confiance", "Solitude", "Non, merci"])

    if besoin == "Sommeil":
        st.warning("Le sommeil est précieux. Une courte sieste, une tisane... as-tu pu t'accorder un moment calme aujourd'hui ?")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    elif besoin == "Corps":
        st.warning("Ton corps est fort et mérite amour et douceur. 💗")
    elif besoin == "Confiance":
        st.warning("Tu es puissante. Voici une affirmation : _'Je fais de mon mieux, et c’est déjà énorme.'_")
    elif besoin == "Solitude":
        st.warning("Tu n’es pas seule. Je peux t’orienter vers des groupes de soutien si tu veux.")
    elif besoin == "Non, merci":
        st.write("Pas de souci. Je suis juste là, en cas de besoin. 🌺")

    # Affirmations personnalisées
    st.write("💬 Affirmation du jour")
    st.markdown(f"<div class='affirmation-box'>Je suis assez. Chaque jour, je progresse à mon rythme. 🌸</div>", unsafe_allow_html=True)

    # Ressources utiles
    st.write("📚 Ressources utiles")
    with st.expander("Découvrir les liens"):
        st.markdown("- [Comprendre le baby blues – ameli.fr](https://www.ameli.fr/assure/sante/devenir-parent/accouchement-et-nouveau-ne/baby-blues-depression-post-partum-grossesse)")
        st.markdown("- [Groupes de parole de jeunes mamans – lembrassecoeur.fr](https://lembrassecoeur.fr)")
        st.markdown("- [Soutien psychologique – mamazoa.fr](https://mamazoa.fr)")

    # Journal de bord émotionnel
    st.write("📝 Journal de bord émotionnel")
    note = st.text_area("Note ton ressenti du jour ici (privé)")
    if st.button("🗂️ Enregistrer dans le journal"):
        with open("journal_emotionnel.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d')} - {nom} : {note}\n")
        st.success("Ton entrée a été enregistrée dans le journal 💌")

    # Annuaire de professionnelles
    st.write("📞 Annuaire de professionnelles du bien-être")
    with st.expander("Voir l'annuaire"):
        st.markdown("""**📍 Marie Dupont – Sage-femme libérale**  
Adresse : 10 rue des Lilas, 75020 Paris  
Tél : 01 23 45 67 89  
Spécialité : Suivi post-partum, allaitement
""")
        st.markdown("""**📍 Sophie Leclerc – Sophrologue spécialisée maternité**
Lyon – 07 11 11 11 11""")
        st.markdown("""**📍 Awa Ndiaye – Coach bien-être postnatal**
Dakar – +221 77 123 45 67""")

    # Forum anonyme (témoignages)
    st.write("💬 Forum anonyme – Partage & Lecture")
    st.markdown("Partage ton expérience ou lis les pensées d'autres mères")

    # Lecture des témoignages
    try:
        with open("temoignages.txt", "r") as f:
            temoins = f.readlines()
            for t in temoins[-5:]:
                st.info(t.strip())
    except FileNotFoundError:
        st.warning("Aucun témoignage pour le moment.")

    # Partage de témoignage
    nouveau = st.text_area("Écris ici ton témoignage anonyme :")
    if st.button("📤 Partager anonymement"):
        with open("temoignages.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : {nouveau}\n")
        st.success("Merci pour ton partage 🌷")

    st.write("---")
    st.write("💜 Merci pour cet échange. N’oublie pas que tu fais un travail incroyable. Zarali est là, avec toi.")
