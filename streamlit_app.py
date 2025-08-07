
import streamlit as st

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

nom = st.text_input("Quel est ton prénom ?", "")

if nom:
    st.success(f"Enchantée {nom} 💖 Ravie d’être avec toi aujourd’hui.")
    st.write("Comment te sens-tu en ce moment ?")

    humeur = st.radio("Choisis ce qui te parle :", ["Triste", "Fatiguée", "Stressée", "Bien", "Autre"])

    if humeur == "Triste":
        st.info("Je suis là pour toi. Tu veux peut-être une respiration guidée ou un mot doux ? 🌧️")
    elif humeur == "Fatiguée":
        st.info("Courage, {nom}. Même une micro-sieste peut changer la journée. 💤")
    elif humeur == "Stressée":
        st.info("Respire. Tu veux essayer une technique de relaxation rapide ? 🌿")
    elif humeur == "Bien":
        st.success("Je suis heureuse de lire ça ! ☀️ Continue à prendre soin de toi.")
    else:
        st.info("Merci de partager. Chaque émotion compte. Je suis là pour t’écouter. 💬")

    st.write("---")
    st.write("Souhaites-tu qu’on parle de quelque chose en particulier ?")
    besoin = st.selectbox("Choisis un thème :", ["-", "Sommeil", "Corps", "Confiance", "Solitude", "Non, merci"])

    if besoin == "Sommeil":
        st.warning("Le sommeil est précieux. Une courte sieste, une tisane... as-tu pu t'accorder un moment calme aujourd'hui ?")
    elif besoin == "Corps":
        st.warning("Ton corps est fort et mérite amour et douceur. 💗")
    elif besoin == "Confiance":
        st.warning("Tu es puissante. Voici une affirmation : _'Je fais de mon mieux, et c’est déjà énorme.'_")
    elif besoin == "Solitude":
        st.warning("Tu n’es pas seule. Je peux t’orienter vers des groupes de soutien si tu veux.")
    elif besoin == "Non, merci":
        st.write("Pas de souci. Je suis juste là, en cas de besoin. 🌺")

    st.write("---")
    st.write("💜 Merci pour cet échange. N’oublie pas que tu fais un travail incroyable. Zarali est là, avec toi.")

