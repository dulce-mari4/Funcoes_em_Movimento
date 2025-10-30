import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# título
st.title('Funções de 1º Grau')
st.subheader('A forma geral desta função é: y = ax + b')

# controles - entrada usuário
a = st.slider('Selecione o valor de a (coeficiente angular)',
              min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider('Selecione o valor de b (coeficiente linear)',
              min_value=-5.0, max_value=5.0, value=0.0, step=0.1)

st.markdown(f"---")
st.markdown("### Entendendo a Função:")
st.markdown(
    f"**Coeficiente Angular (a = {a}):** Controla a inclinação da reta. Se $a > 0$, a função é crescente. Se $a < 0$, a função é decrescente.")
st.markdown(
    f"**Coeficiente Linear (b = {b}):** É o ponto onde a reta cruza o eixo $y$. É o valor de $y$ quando $x = 0$.")

# lógica - 100 pontos pro eixo X de -10 a 10
x = np.linspace(-10, 10, 100)
# valores de Y para cada X com os de 'a' e 'b'
y = a * x + b

# gráfico
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x + {b}')
ax.axhline(0, color='gray', linestyle='--')  # Eixo X
ax.axvline(0, color='gray', linestyle='--')  # Eixo Y
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Gráfico da Função Afim')
ax.grid(True)
ax.legend()
st.pyplot(fig)