import streamlit as st

st.set_page_config(page_title="Empresas Parceiras", layout="wide")

st.title("🌐 Empresas Parceiras")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("spacex.png")
    st.subheader("🚀 SpaceX")

    st.write("""
    Empresa aeroespacial criada por Elon Musk.
    Atua no desenvolvimento de foguetes e viagens espaciais.
    """)

    st.link_button("Acessar Site", "https://www.spacex.com/")

with col2:
    st.image("apple.png")
    st.subheader("🍎 Apple")

    st.write("""
    Empresa mundialmente conhecida pelos seus produtos tecnológicos,
    como iPhone, iPad e MacBook.
    """)

    st.link_button("Acessar Site", "https://www.apple.com/br/")
  
with col3:
    st.image("netflix.png")
    st.subheader("🎬 Netflix")

    st.write("""
    Plataforma de streaming com filmes, séries e documentários
    assistidos no mundo inteiro.
    """)

    st.link_button("Acessar Site", "https://www.netflix.com/br/")

--
