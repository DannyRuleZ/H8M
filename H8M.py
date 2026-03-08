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

# CARTA
st.markdown("""
<div class="carta">

Hoy no es un día cualquiera.

Hoy es un día para recordar lo fuerte, valiente y especial que eres.

Tu forma de ver el mundo, tu sonrisa y la energía que transmites hacen que todo sea un poco más bonito para quienes te rodean.

Gracias por existir.  
Gracias por ser auténtica.  
Gracias por ser una persona tan increíble.

Nunca olvides lo valiosa que eres.

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# COSAS QUE ADMIRAS
st.markdown("### 🌷 Cosas que admiro de ti")

st.markdown("""
<div class="lista">

• Tu fortaleza incluso en los momentos difíciles  
• Tu forma de cuidar a los demás  
• Tu inteligencia y tu forma de pensar  
• Tu sonrisa que ilumina cualquier lugar  
• Tu forma única de ser tú misma  

</div>
""", unsafe_allow_html=True)

st.write("")
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

    Eres una persona increíble.  
    Nunca olvides lo especial que eres.  

    🌸 Feliz Día de la Mujer 🌸

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# MENSAJE FINAL
st.markdown("---")

st.markdown("""
<p style="text-align:center;font-size:18px;">
Hecho con mucho cariño 💖
</p>
""", unsafe_allow_html=True)