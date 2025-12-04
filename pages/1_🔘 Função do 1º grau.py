import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Funções de 1º Grau",
    page_icon="🧮",
)

# título
st.title('Funções de 1º Grau')
st.markdown("### Entendendo a Função:")
st.write("""

A função do 1º grau é uma **equação** que possui incógnita, onde as letras 
representam valores desconhecidos. A sentença matemática da equação do 1º grau 
é ax + b = 0, em que **a** e **b** são números reais, e **a** é diferente de 0. 
O objetivo de escrever uma equação do 1º grau é encontrar qual é o valor da 
incógnita que satisfaz a equação. Esse valor é conhecido como solução ou raiz da 
equação. 

---

As funções do 1º grau, também chamadas de **funções afins**, são expressões 
matemáticas que descrevem uma **reta** no plano cartesiano.

A forma geral da função é:""")     
            
col1, col2, col3 = st.columns([2, 1, 2]) 

with col2:
    st.write("$y = ax + b$")

st.write("""Essa expressão tem só dois protagonistas. O termo “a” e o termo “b”. 
O primeiro determina a inclinação da reta; o segundo, o ponto onde ela toca o 
eixo vertical. 
Sempre que temos algo da forma “uma constante multiplicada por x, mais outra 
constante”, estamos lidando com uma reta.

- **a** é o coeficiente angular: indica a inclinação da reta.
- **b** é o coeficiente linear: indica onde a reta cruza o eixo y.
            
Para construir essa reta no papel ou em um plano cartesiano, você só precisa de 
dois pontos. O primeiro é sempre fácil: x = 0 dá f(0) = b. O segundo pode ser 
x = 1: f(1) = a + b. Conecta os dois e pronto. A magia da linearidade é essa: 
duas informações fixam todo o comportamento.

No gráfico, alguns cenários famosos aparecem sempre. Quando **a** é positivo, a 
reta sobe e parece otimista, sempre crescendo. Quando **a** é negativo, ela 
desce — um pequeno vale matemático. Quando **a** é zero, fica uma reta 
horizontal, indiferente ao valor de x. E **b** desloca essa forma para cima 
ou para baixo sem mudar sua inclinação.

---

### Características

- O gráfico é sempre uma **reta**.
- Se **a > 0**, a função é **crescente**.
- Se **a < 0**, a função é **decrescente**.
- Se **a = 0**, não é uma função do 1º grau (vira constante).

---

### Exemplos""")

# controles - entrada usuário
a = st.slider('Selecione o valor de **a** (coeficiente angular)',
              min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider('Selecione o valor de **b** (coeficiente linear)',
              min_value=-5.0, max_value=5.0, value=0.0, step=0.1)

st.markdown(f"""

- Coeficiente Angular (a = {a}): Controla a inclinação da reta. Se $a > 0 $, a 
função é crescente. Se $a < 0$, a função é decrescente.
- Coeficiente Linear (b = {b}): É o ponto onde a reta cruza o eixo $y$. É o 
valor de $y$ quando $x = 0$.
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

st.markdown("Para calcular o **coeficiente angular**, usamos a seguinte regra:")
st.latex(r"""
\left\{
\begin{aligned}
m=\frac{y_2 - y_1}{x_2 - x_1} \\
\end{aligned}
\right.
""")
st.markdown("""Já o **coeficiente linear** corresponde ao valor de b. Se a função já 
está na forma $f(x) = ax + b$ o coeficiente linear, é o valor de **b**. Caso a 
função não esteja escrita de forma explícita, basta substituir o valor de $x$ 
por 0 na equação e resolver para encontrar o valor de $y$.\\
Exemplo:\\
Para a função $f(x) = 3x + 2$ -> $f(0) = 3(0) + 2 = 0 + 2 = 2$\\
Logo, o coeficiente linear é 2.""")
st.write("---")

st.markdown("""
### Aplicações

Funções do 1º grau aparecem em situações como:

- Cálculo de preços com taxa fixa;
- Crescimento linear de uma população;
- Conversão de unidades com proporção constante...

#### Assista a vídeo aula a seguir para aprofundar seu conhecimento!
""")
st.markdown("Clique aqui para ser redirecionado: [Função do 1º Grau](https://youtu.be/x4k8950MVeg?si=M9zb1IMe5Eke7pI6)")

st.write("---")

st.markdown("### **Agora vamos a uma lição simples para praticar o que você " \
"aprendeu:**")

st.markdown("""A função $f(x)=3x-5$ representa o custo, em reais, para produzir 
$x$ unidades de um produto. Qual é o custo para produzir 4 unidades?""")

opcoes_funcao_1grau = ["Selecione a opção correta:", "A) R$ 7", "B) R$ 12", 
"C) R$ 17", "D) R$ 20", "E) R$ 25"]

escolha_funcao_1grau = st.radio(" ", opcoes_funcao_1grau)

if escolha_funcao_1grau == "Selecione a opção correta:":
    st.error("Escolha uma das opções.")
elif escolha_funcao_1grau != "A) R$ 7":
    st.error("Ops! Tente novamente.")
else:
    st.success("Correto!: f(4)=3*4-5=12-5=7")
    st.markdown(
        """
        **Agora vamos para a explicação:
        Substituímos $x$ = 4 na função:
        $f(4)=3*4-5=12-5=7$
        | Isso dá R\$ 7, então a alternativa correta é A).
        Gabarito: A) R\$ 7**
    """)

st.page_link(
    "pages/2_☑️ Quiz 1.py",
    label="Ir para o quiz.",  
    icon="☑️" 
)

#rodapé (ajuda do gemini pois o streamlit não possui função específica para tal)
import streamlit as st
st.divider()
footer_html = """
<style>
/* Estiliza o conteúdo do rodapé (o texto) */
.footer-content {
    text-align: center; /* Centraliza o texto */
    padding: 10px 0 10px 0; /* Espaçamento interno (cima, direita, baixo, 
    esquerda) */
    color: #FAFAFA; /* Cor do texto (branco claro para contraste) */
    font-size: 14px;
}
</style>
<div class="footer-content">
    Projeto de Site/App de Matemática | Desenvolvido por Dulce Maria e 
    Patrick Oliveira | Estudantes de Ciência da Computação 
    https://github.com/dulce-mari4 | https://github.com/PatrickOliveira1
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)