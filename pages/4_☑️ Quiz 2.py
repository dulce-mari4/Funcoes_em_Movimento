import streamlit as st
st.header("Quiz funções do 2º grau")
st.write("""Olá! Seja bem vindo ao quiz sobre funções do 2º grau. É hora de 
         testar seus conhecimentos!""")

questoes_2_grau = [
    {
        "id": 1,
        "enunciado": """O lucro de uma empresa é dado por $L(x) = -x² + 60x - 
        500$. Para qual quantidade vendida $(x)$ o lucro é máximo?""",
        "opcoes": ["20", "30", "40", "50"],
        "correta": "30",
        "resolucao": "O máximo ocorre no $X$ do vértice $(Xv)$. "
        "$Xv = -b / 2a. Xv = -60 / (2 * -1) = -60 / -2 = 30$."
    },
    {
        "id": 2,
        "enunciado": """Uma bola é chutada e sua trajetória segue a função 
        $h(t) = -t² + 4t$, onde $h$ é altura e $t$ é tempo. Em que instante a 
        bola toca o chão novamente?""",
        "opcoes": ["2 s", "3 s", "4 s", "0 s"],
        "correta": "4 s",
        "resolucao": "Tocar o chão significa $h(t) = 0$. $-t² + 4t = 0$ => "
        "$t(-t + 4) = 0$. As raízes são $t=0$ (início) e $t=4$ (final)."
    },
    {
        "id": 3,
        "enunciado": """Qual é a coordenada do vértice da parábola 
        $y = x² - 4x + 3$?""",
        "opcoes": ["$V(2, -1)$", "$V(-2, 1)$", "$V(2, 1)$", "$V(0, 3)$"],
        "correta": "$V(2, -1)$",
        "resolucao": """$Xv = -(-4)/2 = 2. Yv = 2² - 4(2) + 3 = 4 - 8 + 3 = -1$. 
        Vértice é $(2, -1)$."""
    },
    {
        "id": 4,
        "enunciado": """Para cercar uma área retangular utilizando 40 metros de 
        tela de forma a obter a maior área possível, quais devem ser as 
        dimensões dos lados?""",
        "opcoes": ["15m e 5m", "10m e 10m", "12m e 8m", "20m e 1m"],
        "correta": "10m e 10m",
        "resolucao": """Perímetro $2x + 2y = 40$ => $x + y = 20$ => $y = 20 - 
        x$. Área = $x(20 - x) = -x² + 20x$. O máximo $(Xv)$ é $-20/-2 = 10$. 
        Se $x=10$, $y=10$."""
    },
    {
        "id": 5,
        "enunciado": """A função $f(x) = x² - 5x + 6$ intercepta o eixo $X$ em 
        quais pontos?""",
        "opcoes": ["$(2$,$0)$ e $(3$,$0)$", "$(-2$,$0)$ e $(-3$,$0)$", 
                   "$(1$,$0)$ e $(6$,$0)$", "$(0$,$6)$ e $(0$,$0)$"],
        "correta": "$(2,0)$ e $(3,0)$",
        "resolucao": "Resolvendo $x² - 5x + 6 = 0$ por Bhaskara ou Soma e "
        "Produto ($S=5$, $P=6$), as raízes são $2$ e $3$."
    },
    {
        "id": 6,
        "enunciado": """A área de uma praça quadrada é de 144 m². Qual é a 
        do lado dessa praça? (Modele como $x² = 144$)""",
        "opcoes": ["10 m", "11 m", "12 m", "14 m"],
        "correta": "12 m",
        "resolucao": "A área do quadrado é $L². L² = 144$ => $L = √144 = 12 m$."
        "(Descartamos -12 pois é medida de comprimento)."
    },
    {
        "id": 7,
        "enunciado": """Um objeto é solto de uma altura h. A distância 
        percorrida é dada por $d(t) = 5t²$ (onde $t$ é o tempo em segundos). Se 
        o objeto percorreu 45 metros, quanto tempo levou?""",
        "opcoes": ["2 s", "3 s", "4 s", "5 s"],
        "correta": "3 s",
        "resolucao": "$5t² = 45$ => $t² = 9$ => $t = 3$ segundos."
    },
    {
        "id": 8,
        "enunciado": "Resolva a equação incompleta $2x² - 18 = 0$ no conjunto "
        "dos números reais.",
        "opcoes": ["$S = {3}$", "$S = {-3}$", "$S = {-3, 3}$", "$S = {9}$"],
        "correta": "$S = {-3, 3}$",
        "resolucao": "$2x² = 18$ => $x² = 9$ => $x = ±√9$ => $x = ±3$."
    },
    {
        "id": 9,
        "enunciado": """Em um sítio há galinhas e porcos, totalizando 10 cabeças 
        e 28 pés. Quantas galinhas e quantos porcos há, respectivamente? 
        (Sistema Linear 2x2)""",
        "opcoes": ["6 galinhas e 4 porcos", "4 galinhas e 6 porcos", 
                   "5 galinhas e 5 porcos", "8 galinhas e 2 porcos"],
        "correta": "6 galinhas e 4 porcos",
        "resolucao": "$G + P = 10 e 2G + 4P = 28$. Multiplicando a 1ª por $-2$:"
        "$-2G - 2P = -20$. Somando com a 2ª: $2P = 8$ => $P = 4$. Logo, $G = 6$."
    },
    {
        "id": 10,
        "enunciado": """A soma de dois números é 20 e a diferença entre eles é 4. 
        Quais são esses números?""",
        "opcoes": ["10 e 10", "12 e 8", "14 e 6", "15 e 5"],
        "correta": "12 e 8",
        "resolucao": "$x + y = 20$ e $x - y = 4$. Somando as duas equações: "
        "$2x = 24$ => $x = 12$. Substituindo: $12 + y = 20$ => $y = 8$."
    }
]
if 'submetido' not in st.session_state:
    st.session_state.submetido = False

def pagina_quiz():

    questoes = questoes_2_grau  
    
    respostas_usuario = {}

    with st.form("quiz_form"):
        for q in questoes:
            st.subheader(f"Questão {q['id']}")
            st.write(q['enunciado'])
            
            respostas_usuario[q['id']] = st.radio(
                "Selecione uma opção:", 
                q['opcoes'], 
                key=f"q_{q['id']}",
                index=None 
            )
            st.markdown("---")
        
        botao_enviar = st.form_submit_button("Enviar Respostas")
        
        if botao_enviar:
            st.session_state.submetido = True
            st.rerun() 

    if st.session_state.submetido:
        st.header("Resultados e Correção")
        acertos = 0
        
        for q in questoes:
            resposta_dada = respostas_usuario.get(q['id'])
            
            if resposta_dada == q['correta']:
                st.success(f"**Questão {q['id']}: Correta!**")
                acertos += 1
            else:
                st.error(f"**Questão {q['id']}: Incorreta.**")
                st.write(f"Você marcou: {resposta_dada}")
            
            with st.expander(f"Ver resolução da Questão {q['id']}"):
                st.info(f"**Gabarito:** {q['correta']}")
                st.write(f"**Explicação:** {q['resolucao']}")
        
        st.metric("Pontuação Final", f"{acertos}/{len(questoes)}")
        
        if st.button("Refazer Quiz"):
            st.session_state.submetido = False
            st.rerun()

if __name__ == "__main__":
    pagina_quiz()