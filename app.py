from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

# ============================================================
# DISEÑO DEL CONSULTORIO PSICOLÓGICO
# ============================================================

st.set_page_config(
    page_title="Consultorio de Sentimientos",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background-color: #EAF4F4;
    }

    /* Título */
    h1 {
        color: #315C5C;
        text-align: center;
        font-family: Georgia, serif;
        font-size: 42px;
        margin-bottom: 5px;
    }

    /* Subtítulos */
    h2, h3 {
        color: #477878;
        font-family: Georgia, serif;
    }

    /* Texto normal */
    p, label, .stMarkdown {
        color: #385454;
        font-family: Arial, sans-serif;
    }

    /* Caja principal */
    .consultorio {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #D2E4E4;
        box-shadow: 0px 6px 20px rgba(50, 90, 90, 0.12);
        margin-bottom: 25px;
    }

    /* Caja de análisis */
    .analisis {
        background-color: #F7FBFB;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8CBABA;
        margin-top: 20px;
    }

    /* Campo de texto */
    .stTextInput input {
        border-radius: 12px;
        border: 2px solid #B9D6D6;
        padding: 12px;
    }

    .stTextInput input:focus {
        border-color: #6FA3A3;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #DCEEEE;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: #DCEEEE;
        border-radius: 12px;
        color: #315C5C;
        font-weight: bold;
    }

    /* Resultado */
    .resultado {
        text-align: center;
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        margin-top: 25px;
        box-shadow: 0px 4px 15px rgba(50, 90, 90, 0.10);
    }

    /* GIF */
    .gif-container {
        text-align: center;
        margin-top: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# CONSULTORIO
# ============================================================

st.markdown("""
<div class="consultorio">
""", unsafe_allow_html=True)

st.title('🧠 Consultorio de Sentimientos')

st.markdown("""
<p style="text-align:center; font-size:18px;">
Un pequeño espacio para conocer qué emociones transmite tu mensaje.
</p>
""", unsafe_allow_html=True)

image = Image.open('emoticones.jpg')
st.image(image)

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

st.markdown("</div>", unsafe_allow_html=True)


translator = Translator()

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 

with st.expander('🔎 Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        st.markdown('<div class="analisis">', unsafe_allow_html=True)

        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))

        x=round(blob.sentiment.polarity,2)

        # ====================================================
        # SENTIMIENTO POSITIVO
        # ====================================================

        if x > 0.0 and x <=1.0:

            st.write('Es un sentimiento Positivo 😊')

            st.markdown('<div class="resultado">', unsafe_allow_html=True)

            st.markdown("""
            <h2>😊 Resultado positivo</h2>
            <p>El análisis detecta una emoción predominantemente positiva.</p>
            """, unsafe_allow_html=True)

            st.image(
                'Loader cat.gif',
                caption='Tu estado emocional parece estar bien 🐱'
            )

            st.markdown('</div>', unsafe_allow_html=True)


        # ====================================================
        # SENTIMIENTO NEGATIVO
        # ====================================================

        elif x >=-1 and x < 0:

            st.write('Es un sentimiento Negativo 😔')

            st.markdown('<div class="resultado">', unsafe_allow_html=True)

            st.markdown("""
            <h2>😔 Resultado negativo</h2>
            <p>El análisis detecta una emoción predominantemente negativa.</p>
            """, unsafe_allow_html=True)

            st.image(
                'Failed.gif',
                caption='Parece que hoy no ha sido un buen día 😿'
            )

            st.markdown('</div>', unsafe_allow_html=True)


        # ====================================================
        # SENTIMIENTO NEUTRAL
        # ====================================================

        else:

            st.write('Es un sentimiento Neutral 😐')

            st.markdown('<div class="resultado">', unsafe_allow_html=True)

            st.markdown("""
            <h2>😐 Resultado neutral</h2>
            <p>El análisis no detecta una emoción positiva o negativa dominante.</p>
            """, unsafe_allow_html=True)

            st.image(
                'Loader 4.gif',
                caption='Tu estado emocional parece estar estable 😐'
            )

            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
