import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Pagina Inicial",
    page_icon="🧮",
)

st.sidebar.success("Selecione uma lição acima.")

st.write("# 🧮 Bem-vindo ao Funções em Movimento!")

st.write("#### Seu portal interativo para dominar a matemática do ensino médio")

st.write("---")

st.markdown(
    """
    **📘 O que você vai encontrar aqui:**
    - Lições organizadas por temas: Álgebra, Geometria, Estatística, Funções e muito mais
    - Explicações claras e exemplos práticos
    - Exercícios interativos para testar seus conhecimentos
    - Dicas para mandar bem nas provas e no ENEM
"""
)

st.write("---")

st.markdown(
    """
    🎯 Objetivo do projeto Este aplicativo foi desenvolvido como parte de um trabalho acadêmico com o propósito de facilitar o aprendizado da matemática de forma acessível, dinâmica e envolvente.
"""
)

st.write("---")

st.markdown(
    """
    👨‍🏫 Como começar Clique no botão abaixo para acessar o conteúdo e escolher sua primeira lição!
[ Começar agora ](/funcao1grau)

"""
)