import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Funções de 2º Grau",
    page_icon="🧮",
)

# título
st.title('Funções de 2º Grau')
st.markdown("### Entendendo a Função:")
st.write("""

A função do segundo grau é aquele ponto da matemática onde as retas resolvem 
ficar enjoadaças e começam a fazer **curvas** elegantes. Em vez de um caminho 
direto, elas se arqueiam como uma ponte ou uma tigela. Vamos verificar isso 
de um jeito tranquilo.

---

A equação do 2º grau é um polinômio do tipo ax² + bx + c, onde **a**, **b** e 
**c** são números reais. Aqui, nosso interesse é descobrir os valores de **x**, 
que fará a expressão se igualar a 0, ou seja, suas raízes.

A forma geral da função é:""")     
            
col1, col2, col3 = st.columns([2, 2, 2]) 

with col2:
    st.write("$ax² + bx + c = 0 $")

st.write("""
Aqui, a brincadeira tem três personagens de verdade: **a**, **b** e **c**. O 
**a** é o maestro — decide o formato da curva. O **b** mexe na inclinação 
inicial e desloca o vértice para um lado ou para o outro. O **c** é o ponto onde 
tudo toca o eixo y (basta colocar $x = 0$ e ver que dá $f(0) = c$. Só que a 
parte bonita da função do segundo grau é o gráfico: uma parábola.

Se **a > 0**, essa parábola se abre para cima, como uma taça ou um sorriso 
geométrico. Se **a < 0**, ela se abre para baixo, como um arco ou um chapéu de 
bruxo. O valor de **a** também controla o quão “esticada” ela fica: quanto maior 
o valor absoluto de a, mais estreita e “empinada” a curva; quanto menor, mais 
aberta e suave.

O ponto mais especial do gráfico é o vértice. Ele é o ponto mais alto da 
parábola quando **a < 0**, ou o mais baixo quando **a > 0**. A posição desse 
vértice não é chutada; existe uma fórmula elegante para encontrá-lo. A 
coordenada x do vértice é:

$x_v = -b / (2a)$

E a coordenada **y** do vértice é simplesmente $f(x_v)$. Isso te diz exatamente 
onde a parábola alcança seu máximo ou mínimo.

Agora, como essa curva encontra o eixo **x**? É aqui que a famosa fórmula de 
Bhaskara entra em cena. Quando queremos descobrir os valores de **x** que fazem 
a expressão $ax² + bx + c$ igualar zero, estamos procurando os pontos onde o 
gráfico toca (ou cruza) o eixo **x**. Resolver $ax² + bx + c = 0$ não é trivial 
na mão, então Bhaskara nos presenteou com a solução já arrumada:

$x = -b ± √(b² - 4ac) / (2a)$

O pedaço dentro da raiz, $b² - 4ac$, é o discriminante. Ele é o juiz de quantas 
soluções a equação tem. Se ele for positivo, você tem duas interseções com o 
eixo **x**. Se for zero, a parábola encosta no eixo x em um único ponto — o 
vértice está exatamente ali. E se for negativo, a parábola fica toda acima ou 
toda abaixo do eixo **x**, sem cruzá-lo.
         
Vejamos um exemplo:
Equação ⇒ $x² - x - 12 = 0$\\
Coeficientes: $a = 1$, $b = (-1)$ e $c = (-12)$ \\
$Δ = (-1)² - 4.1.(-12)$ \\
$Δ = 1 + 48$ \\
$Δ = \sqrt{49}$ \\
$x = -(-1)±\sqrt{49}/2.1$\\
$x = 1±7/2$\\
$x' = 1 + 7/2$ ⇒ $x' = 4$\\
$x'' = 1 - 7/ 2$ ⇒ $x'' = -3$

---

### Quando o discriminante (Δ) é negativo 

Como não existe raiz quadrada real de número negativo, não existe **x** real que 
zere a função. Nesse caso, a parábola não encosta no eixo **x**. Se **a** for 
positivo, ela fica inteira acima do eixo x. Se **a** for negativo, fica inteira 
abaixo.

“Qual é o valor de y quando Δ ≤ 0?”
         
A resposta correta é:
         
O valor de **y** existe normalmente para qualquer **x**.
O que Δ ≤ 0 determina é se existe (Δ=0) ou não existe (Δ<0) algum **x** que 
torne y = 0.
         
- Δ > 0 ⇒ duas entradas na festa (duas raízes).
- Δ = 0 ⇒ só uma entrada, exclusiva.
- Δ < 0 ⇒ ninguém entra; a porta (eixo x) nunca é alcançada. (Não admite 
solução dentro dos reais.)

---

### Funções incompletas

- **Função $ax² + bx$**\\
Aqui o termo constante “c” sumiu. Isso faz a parábola passar exatamente pelo 
ponto (0,0). Como c é o valor de f(0), sem ele o gráfico sempre começa no eixo 
**y**. É uma parábola mais “simétrica” de certo modo, porque sua raiz zero 
aparece naturalmente. Basta fatorar x e perceber que uma solução já está 
garantida. Usamos: $ax² + bx = 0$ ⇒ $x.(ax + b) = 0$\\
Nesse caso, para que o resultado seja 0, é necessário que, pelo menos, um dos 
fatores seja igual a 0.\\
$x = 0$ ou $ax + b = 0$\\
Assim, temos:\\
$x' = 0$ ou $x = -b/a$ \\
Exemplo: \\
Determine a solução do polinômio: $5x² + 3x = 0$
         
    $x.(5x + 3)$\\
    $x' = 0$\\
    $x'' = 5x + 3 = 0$
    $5x = -3$ ⇒ $x = -3/5$\\
    $x'' = -0,6$
         
- **Função $ax² + c$**\\
Agora quem some é o termo “bx”. O gráfico ainda é uma parábola, mas ela fica 
perfeitamente alinhada no meio, simétrica em relação ao eixo **y**. É como se 
alguém tivesse colocado a curva no centro com régua e esquadro. A ausência do 
termo linear impede a parábola de se deslocar para a esquerda ou para a 
direita.\\
Exemplo:\\
Encontre as raízes da equação $3x² - 27 = 0$
         
    $3x² = 27$\\
    $x² = 27/3$\\
    $x² = 9$\\
    $x = ±\sqrt{9}$\\
    $x' = 3; x'' = -3$
         
---      

### Sistemas de equações

Imagine dois viajantes caminhando por um plano infinito. Cada um segue a sua 
própria trilha, traçada por uma equação. Resolver um sistema é descobrir em que 
ponto esses dois viajantes se encontram, se é que se encontram. Se eles se 
cruzam uma vez, existe uma única solução. Se caminham na mesma trilha, há 
infinitas soluções. Se seguem caminhos paralelos e teimosos que nunca se tocam, 
não existe solução.

Por isso resolver um sistema é quase como narrar o momento exato em que duas 
histórias diferentes se encontram no mesmo ponto do espaço. É uma espécie de 
geometria narrativa: cada equação conta uma rota e o sistema procura o ponto em 
que as rotas se combinam. A álgebra entra em cena para achar esse ponto sem 
precisar desenhar, mas o espírito é o mesmo.

Vejamos um exemplo:

""")
st.latex(r"""
\left\{
\begin{aligned}
2x + 3y &= 8 \\
x - y &= 1
\end{aligned}
\right.
""")
st.write("""
- Método 1 - Substituição
1. Da segunda equação, isolamos o $x$:
$x = 1 + y$
2. Substituímos na primeira:
$2(1 + y) + 3y = 8$
3. Resolvem-se os termos: $2 + 2y + 3y = 8 ⇒ 5y = 6$
4. Logo $y = 6/5 = 1,2$
5. Voltando em $x = 1 + y:x = 1 + 6/5 = 11/5 = 2,2$
         
Solução: $x = 11/5, y = 6/5$
         
- Método 2 - Eliminação (adição/subtração)
1. Multiplica a segunda por $-2$ para cancelar $x$ ao somar:
$-2x + 2y = -2$
2. Soma com a primeira: $(2x - 2x) + (3y + 2y) = 8 - 2 ⇒ 5y = 6$
3. Mesmos passos finais: $y = 6/5, x = 11/5$
         
Ambos chegam ao mesmo resultado - escolha o que te parecer mais confortável.

---
         
### Características

- O gráfico é sempre uma **parábola**. O sentido depende do sinal de **a**.
- **a é ≠ de 0**, sempre. Caso contrário, voltamos para o mundo das linhas 
retas.
- Existe sempre um vértice, que é o ponto extremo da curva. É o ponto de máximo 
ou mínimo do gráfico e aparece em $x = -b/(2a)$

Olhar para a função do segundo grau como um gráfico é uma daquelas pequenas 
janelas mentais que deixam tudo mais claro. Em vez de um amontoado de símbolos, 
você enxerga um objeto geométrico com simetria, máximo ou mínimo, abertura, 
interseções. A álgebra e a geometria fazem um pequeno trato silencioso para 
revelar o mesmo fenômeno por duas portas diferentes.

---         

""")

st.write("""### Exemplos:""")

# controles - entrada usuário
a = st.number_input("Valor de **a**", value=1.0)
b = st.number_input("Valor de **b**", value=0.0)
c = st.number_input("Valor de **c**", value=0.0)
intervalo = st.slider(
    "Selecione o intervalo de **x**",
    -20.0, 20.0, (-5.0, 5.0)
)
x_min, x_max = intervalo

# Pontos do gráfico
x = np.linspace(x_min, x_max, 400)
y = a*x**2 + b*x + c

# Cálculo do vértice
# Fórmula: x_v = -b/(2a), y_v = f(x_v)
if a != 0:
    x_v = -b / (2*a)
    y_v = a*x_v**2 + b*x_v + c
else:
    x_v = None
    y_v = None

fig, ax = plt.subplots()

# Curva da parábola
ax.plot(x, y, label="f(x) = ax² + bx + c")

# Marcar e legendar o vértice
if x_v is not None and x_min <= x_v <= x_max:
    ax.scatter(x_v, y_v, color="red", s=50, label=f"""Vértice 
    ({x_v:.2f}, {y_v:.2f})""")
    ax.text(
        x_v, y_v,
        f"  ({x_v:.2f}, {y_v:.2f})",
        fontsize=10,
        verticalalignment="bottom"
    )

# Eixos
ax.axhline(0, linewidth=1, color="black")
ax.axvline(0, linewidth=1, color="black")

ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Gráfico da Função do 2º Grau")

ax.legend()

st.pyplot(fig)

st.write("---")

st.markdown("""
### Aplicações

Funções do 2º grau aparecem em situações como:

- Cálculo de lucro máximo de empresas;
- Quando queremos minimizar ou maximizar;
- Quando um objeto cai de uma altura sob certas condições, a variação da altura
com o tempo pode assumir forma quadrática dependendo do modelo físico.

Assista a vídeo aula a seguir para aprofundar seu conhecimento!
""")
videoaula2 = "https://youtu.be/1QlFNgCuccU?si=2NgwRSQRfxkLxNcE"
st.video(videoaula2)

st.write("---")

st.markdown("""
### Mapa Mental

Veja o mapa mental abaixo para fixar o conteúdo da aula!
""")
BASE_DIR = Path(__file__).resolve().parent.parent
img_path = BASE_DIR / "imagens" / "mapamental2.jpeg"

st.image(str(img_path))

st.write("---")

st.markdown("### Agora vamos a uma lição simples para praticar o que você " \
"aprendeu:")

st.markdown("""Resolva a seguinte equação: $x² - 5x + 6 = 0$""")

opcoes_funcao_2grau = ["Selecione a opção correta, que contém as duas raízes:", 
"A) $x' = 1$ e $x'' = 2$", "B) $x' = 3$ e $x'' = 4$ ", 
"C) $x' = 2$ e $x'' = 3$", "D) $x' = 3$ e $x'' = 2$", "E) $x' = 2$ e $x'' = 4$"]

escolha_funcao_2grau = st.radio(" ", opcoes_funcao_2grau)

if escolha_funcao_2grau == "Selecione a opção correta:":
    st.error("Escolha uma das opções.")
elif escolha_funcao_2grau != "D) $x' = 3$ e $x'' = 2$":
    st.error("Ops! Tente novamente.")
else:
    st.success("Correto!")
    st.markdown(
        """
        Agora vamos para a resolução:\\
        Nós temos: $a = 1, b = -5, c = 6$\\
        Seguimos:\\
        $Δ = (-5)² - 4.1.6$ \\
        $Δ = 25 - 24$ \\
        $Δ = \sqrt{1} = 1$ \\
        $x = -(-5)±\sqrt{1}/(2.1)$
        
        $x' = (5 + 1)/2$ ⇒ $x' = 6/2$ ⇒ $x' = 3$\\
        $x'' = (5 - 1)/2$ ⇒ $x'' = 4/2$ ⇒ $x'' = 2$
        Gabarito: D) $x' = 3$ e $x'' = 2$**
    """)

st.page_link(
    "pages/4_☑️ Quiz 2.py",
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