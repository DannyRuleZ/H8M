import streamlit as st
import time

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Feliz 8 de Marzo",
    page_icon="🌸",
    layout="centered"
)

# ESTILO PERSONALIZADO
st.markdown("""
<style>

body {
    background-color: #fff0f6;
}

.titulo {
    text-align: center;
    font-size: 50px;
    color: #d63384;
    font-weight: bold;
}

.subtitulo {
    text-align: center;
    font-size: 24px;
    color: #6f42c1;
}

.carta {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    font-size: 18px;
    line-height: 1.8;
}

.lista {
    font-size: 18px;
}

.final {
    text-align: center;
    font-size: 22px;
    color: #c9184a;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# TITULO
st.markdown('<p class="titulo">🌸 Feliz 8 de Marzo 🌸</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitulo">Hoy quiero recordarte lo increíble que eres 💜</p>', unsafe_allow_html=True)

st.write("")


# BOTON SORPRESA
st.markdown("### 💌 Un pequeño mensaje")

if st.button("Presiona aquí"):
    with st.spinner("Preparando algo especial..."):
        time.sleep(2)

    st.success("Solo quería recordarte algo importante 💜")

    st.balloons()

    st.markdown("""
    <div class="final">

    Eres una persona increíble
    Nunca olvides lo especial que eres

    🌸 Feliz Día de la Mujer Mika 🌸

    </div>
    """, unsafe_allow_html=True)

st.write("")

# MENSAJE FINAL
st.markdown("---")

st.markdown("""
<p style="text-align:center;font-size:18px;">
Hecho con mucho cariño 💖
</p>

""", unsafe_allow_html=True)


