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

st.page_link(
    "pages/1_🔘 Função do 1º grau.py",
    label="Ir para Função do 1º grau.",  
    icon="🔘" 
)
st.page_link(
    "pages/3_🔘 Função do 2º grau.py",
    label="Ir para Função do 2º grau.",  
    icon="🔘" 
)

#rodapé (ajuda do gemini pois o streamlit não possui função específica para tal)
import streamlit as st
st.divider()
footer_html = """
<style>
/* Estiliza o conteúdo do rodapé (o texto) */
.footer-content {
    text-align: center; /* Centraliza o texto */
    padding: 10px 0 10px 0; /* Espaçamento interno (cima, direita, baixo, esquerda) */
    color: #FAFAFA; /* Cor do texto (branco claro para contraste) */
    font-size: 14px;
}
</style>
<div class="footer-content">
    Projeto de Site/App de Matemática | Desenvolvido por Dulce Maria e Patrick Oliveira | Estudantes de Ciência da Computação 
    https://github.com/dulce-mari4 | https://github.com/PatrickOliveira1
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)