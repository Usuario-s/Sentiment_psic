from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.set_page_config(
    page_title="Consultorio Psicológico",
    page_icon="🧠",
    layout="centered"
)

# Diseño
st.markdown("""
<style>

.stApp {
    background-color: #F3F0EA;
    color: black;
}

p, span, label, div {
    color: black;
}

.titulo {
    text-align: center;
    color: black;
    font-family: Georgia, serif;
    font-size: 42px;
    font-weight: bold;
}

.subtitulo {
    text-align: center;
    color: black;
    font-size: 17px;
    margin-bottom: 30px;
}

.info {
    background-color: #E4ECE8;
    padding: 20px;
    border-radius: 15px;
    color: black;
    margin-top: 20px;
    margin-bottom: 20px;
}

.resultado {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    color: black;
}

section[data-testid="stSidebar"] {
    background-color: #E7E0D5;
    color: black;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: black;
}

input {
    color: black !important;
    background-color: white !important;
}

input::placeholder {
    color: #555555 !important;
}

</style>
""", unsafe_allow_html=True)


# Título
st.markdown(
    '<div class="titulo">🧠 Consultorio Psicológico</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Espacio de análisis emocional y reflexión personal</div>',
    unsafe_allow_html=True
)


# Imagen
image = Image.open("emoticones.jpg")
st.image(image, use_container_width=True)


# Bienvenida
st.markdown("""
<div class="info">

<b>Bienvenido al consultorio.</b><br><br>

Escribe una frase y nuestro sistema analizará su polaridad
y subjetividad para identificar si expresa un sentimiento
positivo, negativo o neutral.

</div>
""", unsafe_allow_html=True)


st.subheader("💬 ¿Cómo te sientes hoy?")

st.write(
    "Escribe en el siguiente campo la frase que deseas analizar."
)


translator = Translator()


# Barra lateral
with st.sidebar:

    st.subheader("🧠 Polaridad y Subjetividad")

    st.write("""
    **Polaridad:** Indica si el sentimiento expresado en el texto
    es positivo, negativo o neutral.

    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo),
    con 0 representando un sentimiento neutral.

    **Subjetividad:** Mide cuánto del contenido es subjetivo
    (opiniones, emociones, creencias) frente a objetivo (hechos).

    Va de 0 a 1, donde 0 es completamente objetivo
    y 1 es completamente subjetivo.
    """)

    st.divider()

    st.write("🛋️ Consultorio de análisis emocional")

    st.caption(
        "Este espacio analiza el texto introducido por el usuario."
    )


# Análisis
with st.expander("📝 Analizar texto", expanded=True):

    text = st.text_input(
        "Escribe por favor:",
        placeholder="Ejemplo: Hoy me siento muy feliz..."
    )

    if text:

        translation = translator.translate(
            text,
            src="es",
            dest="en"
        )

        trans_text = translation.text

        blob = TextBlob(trans_text)

        st.markdown(
            '<div class="resultado">',
            unsafe_allow_html=True
        )

        st.write("Polarity: ", round(blob.sentiment.polarity, 2))
        st.write("Subjectivity: ", round(blob.sentiment.subjectivity, 2))

        x = round(blob.sentiment.polarity, 2)


        # Sentimiento positivo
        if x > 0.0 and x <= 1.0:

            st.success("😊 Es un sentimiento Positivo")

            st.markdown(
                "### 🎵 Música para acompañar este estado"
            )

            st.components.v1.html("""
                <iframe
                    width="100%"
                    height="166"
                    src="https://www.youtube.com/embed/ZbZSe6N_BXs"
                    title="Happy - Pharrell Williams"
                    frameborder="0"
                    allow="autoplay; encrypted-media"
                    allowfullscreen>
                </iframe>
            """, height=180)


        # Sentimiento negativo
        elif x >= -1 and x < 0:

            st.error("😔 Es un sentimiento Negativo")

            st.markdown(
                "### 🎵 Música para acompañar este estado"
            )

            st.components.v1.html("""
                <iframe
                    width="100%"
                    height="166"
                    src="https://www.youtube.com/embed/YgSPaXgAdzE"
                    title="Loser - Beck"
                    frameborder="0"
                    allow="autoplay; encrypted-media"
                    allowfullscreen>
                </iframe>
            """, height=180)


        # Sentimiento neutral
        else:

            st.info("😐 Es un sentimiento Neutral")

            st.markdown(
                "### 🔊 Ruido blanco"
            )

            st.components.v1.html("""
                <iframe
                    width="100%"
                    height="166"
                    src="https://www.youtube.com/embed/nMfPqeZjc2c"
                    title="White Noise"
                    frameborder="0"
                    allow="autoplay; encrypted-media"
                    allowfullscreen>
                </iframe>
            """, height=180)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )
