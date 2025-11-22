import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Funções de 1º Grau",
    page_icon="🧮",
)

# título
st.title('Funções de 1º Grau')
st.markdown("### Entendendo a Função:")
st.markdown(f"""
As funções do 1º grau, também chamadas de **funções afins**, são expressões matemáticas que descrevem uma **reta** no plano cartesiano.

A forma geral da função é:

$y = ax + b$

- **a** é o coeficiente angular: indica a inclinação da reta.
- **b** é o coeficiente linear: indica onde a reta cruza o eixo y.

---

### 📊 Características

- O gráfico é sempre uma **reta**.
- Se **a > 0**, a função é **crescente**.
- Se **a < 0**, a função é **decrescente**.
- Se **a = 0**, não é uma função do 1º grau (vira constante).

---

### 🧮 Exemplos""")

# controles - entrada usuário
a = st.slider('Selecione o valor de a (coeficiente angular)',
              min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider('Selecione o valor de b (coeficiente linear)',
              min_value=-5.0, max_value=5.0, value=0.0, step=0.1)

st.markdown(f"""

- Coeficiente Angular (a = {a}): Controla a inclinação da reta. Se $a > 0 $, a função é crescente. Se $a < 0$, a função é decrescente.
- Coeficiente Linear (b = {b}): É o ponto onde a reta cruza o eixo $y$. É o valor de $y$ quando $x = 0$.
""")

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

st.write("---")

st.markdown("""
### 🎯 Aplicações

Funções do 1º grau aparecem em situações como:

- Cálculo de preços com taxa fixa;
- Crescimento linear de uma população;
- Conversão de unidades com proporção constante...

Assista a vídeo aula a seguir para aprofundar seu conhecimento!
""")
videoaula1 = "https://youtu.be/x4k8950MVeg?si=M9zb1IMe5Eke7pI6"
st.video(videoaula1)

st.markdown("### **Agora vamos a uma lição simples para práticar o que você aprendeu:**")

st.markdown("A função $f(x)=3x-5$ representa o custo, em reais, para produzir $x$ unidades de um produto. Qual é o custo para produzir 4 unidades?")

opcoes_funcao_1grau = ["Selecione a opção correta:", "A) R$ 7", "B) R$ 12", "C) R$ 17", "D) R$ 20", "E) R$ 25"]

escolha_funcao_1grau = st.radio(" ", opcoes_funcao_1grau)

if escolha_funcao_1grau == "Selecione a opção correta:":
    st.error("Escolha uma das opções.")
elif escolha_funcao_1grau != "A) R$ 7":
    st.error("❌ Ops! Tente novamente.")
else:
    st.success("✅ Correto!: f(4)=3*4-5=12-5=7")
    st.markdown(
        """
        **Agora vamos para a explicação:
        Substituímos $x$ = 4 na função:
        $f(4)=3*4-5=12-5=7$
        | Isso dá R\$ 7, então a alternativa correta é A).
        ✅ Gabarito: A) R\$ 7**
    """)

st.page_link(
    "pages/2_☑️ Quiz 1.py",
    label="Ir para o quiz.",  
    icon="☑️" 
)