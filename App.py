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

import streamlit as st

#rodapé (ajuda do gemini pois o streamlit não possui função específica para tal)
footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #000000;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    z-index: 9999; 
}
</style>
<div class="footer">
    Desenvolvido por Dulce Maria e Patrick Oliveira | Estudantes de Ciência da Computação 
    https://github.com/dulce-mari4 | https://github.com/PatrickOliveira1
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)