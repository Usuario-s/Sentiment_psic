```python
from textblob import TextBlob 
import pandas as pd 
import streamlit as st 
from PIL import Image 
from googletrans import Translator 
 
# -----------------------------
# CONFIGURACIÓN Y DISEÑO
# -----------------------------

st.set_page_config(
    page_title="Consultorio Psicológico",
    page_icon="🧠",
    layout="centered"
)

# CSS - Diseño de consultorio psicológico
st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background: #F4F1EC;
    }

    /* Título */
    h1 {
        color: #4F6258;
        text-align: center;
        font-family: Georgia, serif;
        font-size: 42px;
        margin-bottom: 5px;
    }

    /* Subtítulos */
    h2, h3 {
        color: #596B63;
        font-family: Georgia, serif;
    }

    /* Texto */
    p, label {
        color: #4B514D;
        font-size: 16px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #E3E9E3;
    }

    /* Tarjeta principal */
    .consulta {
        background: #FFFFFF;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    /* Tarjeta resultado */
    .resultado {
        background: #EEF3EF;
        padding: 25px;
        border-radius: 18px;
        border-left: 6px solid #78958A;
        margin-top: 20px;
    }

    /* Entrada de texto */
    .stTextInput input {
        border-radius: 12px;
        border: 1px solid #B9C7BE;
        padding: 12px;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: #E8EEE9;
        border-radius: 12px;
        color: #4F6258;
        font-weight: bold;
    }

    /* Imagen */
    img {
        border-radius: 18px;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# TÍTULO
# -----------------------------

st.title('🧠 Consultorio Psicológico')

st.markdown(
    "<p style='text-align:center; color:#6B746F;'>"
    "Espacio de análisis emocional y reflexión"
    "</p>",
    unsafe_allow_html=True
)

image = Image.open('emoticones.jpg') 
st.image(image, use_container_width=True) 

st.markdown(
    "<div class='consulta'>"
    "<h3>💬 ¿Cómo te sientes hoy?</h3>"
    "<p>Escribe una frase y el sistema analizará la polaridad y subjetividad "
    "del texto.</p>"
    "</div>",
    unsafe_allow_html=True
)

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar") 
 
translator = Translator() 
 
with st.sidebar: 
    st.subheader("🧠 Polaridad y Subjetividad") 
    st.markdown("""
    **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, 
    negativo o neutral.  
    Su valor oscila entre **-1** (muy negativo) y **1** (muy positivo), 
    con **0** representando un sentimiento neutral.
    
    **Subjetividad:** Mide cuánto del contenido es subjetivo 
    (opiniones, emociones, creencias) frente a objetivo (hechos). 
    Va de **0 a 1**.
    """)  

with st.expander('🔎 Analizar texto'): 
    text = st.text_input('Escribe por favor: ') 
    
    if text: 
 
        translation = translator.translate(text, src="es", dest="en") 
        trans_text = translation.text 
        blob = TextBlob(trans_text) 
        
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.markdown("<div class='resultado'>", unsafe_allow_html=True)

        st.write('**Polaridad:** ', polarity) 
        st.write('**Subjetividad:** ', subjectivity) 
        
        x = polarity
        
        # ---------------------------------
        # SENTIMIENTO POSITIVO
        # ---------------------------------

        if x > 0.0 and x <= 1.0: 
            
            st.success('😊 Es un sentimiento Positivo')
            
            st.markdown("### 🎵 Música positiva")
            
            st.components.v1.html(
                """
                <iframe width="100%" height="100"
                src="https://www.youtube.com/embed/Y6SXV-SUYTM"
                title="Happy - Pharrell Williams"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; 
                encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
                </iframe>
                """,
                height=120
            )

        # ---------------------------------
        # SENTIMIENTO NEGATIVO
        # ---------------------------------

        elif x >= -1 and x <= 0: 
            
            st.error('😔 Es un sentimiento Negativo')
            
            st.markdown("### 🎵 Música negativa")
            
            st.components.v1.html(
                """
                <iframe width="100%" height="100"
                src="https://www.youtube.com/embed/YgSPaXgAdzE"
                title="Loser - Beck"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; 
                encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
                </iframe>
                """,
                height=120
            )

        # ---------------------------------
        # SENTIMIENTO NEUTRAL
        # ---------------------------------

        else: 
            
            st.info('😐 Es un sentimiento Neutral')
            
            st.markdown("### 🌊 Sonido blanco")
            
            st.components.v1.html(
                """
                <iframe width="100%" height="100"
                src="https://www.youtube.com/embed/nMfPqeZjc2c"
                title="White Noise"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; 
                encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
                </iframe>
                """,
                height=120
            )

        st.markdown("</div>", unsafe_allow_html=True)
```
