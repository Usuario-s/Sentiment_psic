import base64
from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator


# ============================================================
# CONFIGURACIÓN DE STREAMLIT
# ============================================================

st.set_page_config(
    page_title="Análisis de Sentimiento",
    page_icon="🧠",
    layout="centered"
)


# ============================================================
# FUNCIÓN PARA MOSTRAR GIFS ANIMADOS
# ============================================================

def mostrar_gif(ruta, ancho=350):

    with open(ruta, "rb") as archivo:
        datos = archivo.read()

    gif_base64 = base64.b64encode(datos).decode()

    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            margin-bottom: 15px;
        ">
            <img 
                src="data:image/gif;base64,{gif_base64}" 
                width="{ancho}"
                style="
                    border-radius: 15px;
                    display: block;
                "
            >
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DISEÑO DEL CONSULTORIO PSICOLÓGICO
# ============================================================

st.markdown("""
<style>

    /* =========================================
       FONDO GENERAL
       ========================================= */

    .stApp {
        background-color: #E8F1F2;
    }


    /* =========================================
       TEXTO GENERAL
       ========================================= */

    p, label, span, div {
        color: #1F3333;
    }


    /* =========================================
       TÍTULO PRINCIPAL
       ========================================= */

    h1 {
        color: #173F3F !important;
        text-align: center;
        font-family: Georgia, serif;
        font-size: 42px !important;
        font-weight: bold;
        margin-bottom: 5px;
    }


    /* =========================================
       SUBTÍTULOS
       ========================================= */

    h2, h3 {
        color: #245757 !important;
        font-family: Georgia, serif;
    }


    /* =========================================
       TARJETA PRINCIPAL
       ========================================= */

    .consultorio {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #B8D1D1;
        box-shadow: 0px 8px 25px rgba(31, 63, 63, 0.15);
        margin-bottom: 25px;
    }


    /* =========================================
       DESCRIPCIÓN
       ========================================= */

    .descripcion {
        text-align: center;
        color: #385858 !important;
        font-size: 18px;
        margin-bottom: 20px;
    }


    /* =========================================
       EXPANDER
       ========================================= */

    div[data-testid="stExpander"] {
        background-color: #FFFFFF;
        border: 2px solid #A8C5C5;
        border-radius: 15px;
        box-shadow: 0px 5px 15px rgba(31, 63, 63, 0.10);
    }

    div[data-testid="stExpander"] summary {
        color: #173F3F !important;
        font-weight: bold;
        font-size: 17px;
    }


    /* =========================================
       CAMPO DE TEXTO
       ========================================= */

    .stTextInput label {
        color: #173F3F !important;
        font-weight: bold;
        font-size: 16px;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #172B2B !important;
        border: 2px solid #7FAAAA !important;
        border-radius: 12px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }

    .stTextInput input::placeholder {
        color: #637777 !important;
    }


    /* =========================================
       SIDEBAR
       ========================================= */

    section[data-testid="stSidebar"] {
        background-color: #D4E7E7;
        border-right: 2px solid #A8C5C5;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #173F3F !important;
    }

    section[data-testid="stSidebar"] p {
        color: #1F3333 !important;
        font-size: 15px;
        line-height: 1.6;
    }


    /* =========================================
       CAJA DE RESULTADOS
       ========================================= */

    .resultado {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #B8D1D1;
        box-shadow: 0px 6px 20px rgba(31, 63, 63, 0.12);
        margin-top: 25px;
        text-align: center;
    }


    .resultado h2 {
        color: #173F3F !important;
        margin-bottom: 10px;
    }


    .resultado p {
        color: #385858 !important;
        font-size: 16px;
    }


    /* =========================================
       POLARIDAD Y SUBJETIVIDAD
       ========================================= */

    .dato {
        background-color: #E8F1F2;
        border-radius: 10px;
        padding: 10px;
        margin: 8px 0;
        color: #173F3F !important;
        font-weight: bold;
    }


    /* =========================================
       PIE DE PÁGINA
       ========================================= */

    .footer {
        text-align: center;
        color: #527070 !important;
        font-size: 13px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# ENCABEZADO DEL CONSULTORIO
# ============================================================

st.markdown("""
<div class="consultorio">
""", unsafe_allow_html=True)

st.title('🧠 Análisis de Sentimiento')

st.markdown("""
<div class="descripcion">
Este espacio analiza las emociones presentes en una frase
y determina si el sentimiento expresado es positivo, negativo o neutral.
</div>
""", unsafe_allow_html=True)


image = Image.open('emoticones.jpg')
st.image(image, use_container_width=True)


st.subheader(
    "Por favor escribe en el campo de texto la frase que deseas analizar"
)

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# TRADUCTOR
# ============================================================

translator = Translator()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.subheader("🧠 Polaridad y Subjetividad")

    st.markdown("""
    <p>
    <b>Polaridad:</b> Indica si el sentimiento expresado en el texto
    es positivo, negativo o neutral.
    </p>

    <p>
    Su valor oscila entre <b>-1</b> (muy negativo) y
    <b>1</b> (muy positivo), con <b>0</b> representando
    un sentimiento neutral.
    </p>

    <p>
    <b>Subjetividad:</b> Mide cuánto del contenido es subjetivo
    (opiniones, emociones, creencias) frente a objetivo
    (hechos).
    </p>

    <p>
    Va de <b>0</b> a <b>1</b>, donde 0 es completamente objetivo
    y 1 es completamente subjetivo.
    </p>
    """, unsafe_allow_html=True)


# ============================================================
# ANALIZAR TEXTO
# ============================================================

with st.expander('🔎 Analizar texto'):

    text = st.text_input('Escribe por favor: ')

    if text:

        translation = translator.translate(
            text,
            src="es",
            dest="en"
        )

        trans_text = translation.text

        blob = TextBlob(trans_text)

        # Valores
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)

        # Mostrar resultados
        st.markdown("""
        <div class="resultado">
        """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="dato">
                📊 Polaridad: {polaridad}
            </div>

            <div class="dato">
                🧠 Subjetividad: {subjetividad}
            </div>
            """,
            unsafe_allow_html=True
        )


        # ====================================================
        # POSITIVO
        # ====================================================

        if polaridad > 0.0 and polaridad <= 1.0:

            st.write('Es un sentimiento Positivo 😊')

            st.markdown("""
            <h2>😊 Sentimiento positivo</h2>

            <p>
            El análisis detecta una emoción predominantemente positiva.
            </p>
            """, unsafe_allow_html=True)

            mostrar_gif(
                'Loader cat.gif',
                350
            )


        # ====================================================
        # NEGATIVO
        # ====================================================

        elif polaridad >= -1.0 and polaridad < 0.0:

            st.write('Es un sentimiento Negativo 😔')

            st.markdown("""
            <h2>😔 Sentimiento negativo</h2>

            <p>
            El análisis detecta una emoción predominantemente negativa.
            </p>
            """, unsafe_allow_html=True)

            mostrar_gif(
                'Failed.gif',
                350
            )


        # ====================================================
        # NEUTRAL
        # ====================================================

        else:

            st.write('Es un sentimiento Neutral 😐')

            st.markdown("""
            <h2>😐 Sentimiento neutral</h2>

            <p>
            El análisis no detecta una emoción positiva o negativa dominante.
            </p>
            """, unsafe_allow_html=True)

            mostrar_gif(
                'Loader 4.gif',
                350
            )


        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("""
<div class="footer">
    Consultorio de Análisis de Sentimientos · Análisis basado en TextBlob
</div>
""", unsafe_allow_html=True)
