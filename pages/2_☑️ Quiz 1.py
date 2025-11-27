import streamlit as st
st.header("Quiz - funções do 1º grau")
st.write("""Olá! Seja bem vindo ao quiz sobre funções do 1º grau. É hora de 
         testar seus conhecimentos!""")

questoes_1_grau = [
    {
        "id": 1,
        "enunciado": """Um motorista de aplicativo cobra um valor fixo de 
        R\$ 5,00 pela partida mais R\$ 2,00 por quilômetro rodado. Qual a lei 
        da função que representa o valor total $(V)$ da corrida em função dos 
        quilômetros $(x)$ rodados?""",
        "opcoes": ["$V(x) = 2x + 5$", "$V(x) = 5x + 2$", "$V(x) = 7x$", 
                   "$V(x) = 5x - 2$"],
        "correta": "$V(x) = 2x + 5$",
        "resolucao": """O valor fixo $(b)$ é 5 e o valor variável $(a)$ é 2. Na 
        função afim $f(x) = ax + b$, substituímos pelos valores: $V(x) = 2x + 5$."""
    },
    {
        "id": 2,
        "enunciado": """Uma caixa d'água de 1000 litros está cheia e começa a 
        vazar. O vazamento é constante de 5 litros por hora. Após quanto tempo a 
        caixa estará completamente vazia?""",
        "opcoes": ["100 horas", "200 horas", "50 horas", "500 horas"],
        "correta": "200 horas",
        "resolucao": """A função é $V(t) = 1000 - 5t$. Para estar vazia, $V(t) = 0$.
        Logo, $1000 - 5t = 0$ => $5t = 1000$ => $t = 200$ horas."""
    },
    {
        "id": 3,
        "enunciado": """O salário mensal de um vendedor é composto por uma parte 
        fixa de R\$ 1.500,00 mais uma comissão de 5% sobre o total de vendas $(v)$ 
        realizadas no mês. Qual a expressão do salário $(S)$?""",
        "opcoes": ["$S = 1500 + 5v$", "$S = 1500 + 0,5v$", "$S = 1500 + 0,05v$", 
                   "$S = 1500v + 0,05$"],
        "correta": "$S = 1500 + 0,05v$",
        "resolucao": "5% equivale a 0,05. A parte fixa é 1500. Logo, a função é "
        "$S(v) = 1500 + 0,05v$."
    },
    {
        "id": 4,
        "enunciado": """Uma temperatura de 20°C corresponde a quantos graus 
        Fahrenheit? Dado: $F = 1,8C + 32$.""",
        "opcoes": ["68°F", "52°F", "42°F", "74°F"],
        "correta": "68°F",
        "resolucao": """Substituindo $C$ por $20$ na fórmula: $F = 1,8(20) + 32$. 
        $F = 36 + 32 = 68°F$."""
    },
    {
        "id": 5,
        "enunciado": """Para produzir um determinado sapato, uma fábrica tem um 
        custo fixo de R\$ 2.000,00 e um custo variável de R\$ 30,00 por par. Qual 
        o custo total para produzir 100 pares?""",
        "opcoes": ["R$ 3.000,00", "R$ 2.300,00", "R$ 5.000,00", "R$ 3.200,00"],
        "correta": "R$ 5.000,00",
        "resolucao": "A função custo é $C(x) = 30x + 2000$. Para $x = 100: C(100)$ "
        "$= 30(100) + 2000 = 3000 + 2000 = 5000$."
    },
    {
        "id": 6,
        "enunciado": """O gráfico de uma função do 1º grau passa pelos pontos 
        $A(1, 3)$ e $B(2, 5)$. Qual é o coeficiente angular $(a)$ dessa função?""",
        "opcoes": ["$1$", "$2$", "$3$", "$0,5$"],
        "correta": "$2$",
        "resolucao": "O coeficiente angular $a = (y2 - y1) / (x2 - x1)$. "
        "$a = (5 - 3) / (2 - 1) = 2 / 1 = 2$."
    },
    {
        "id": 7,
        "enunciado": """Uma vela de 15 cm de altura queima a uma taxa constante 
        de 3 cm por hora. Qual a altura da vela após 4 horas de queima?""",
        "opcoes": ["$12 cm$", "$9 cm$", "$3 cm$", "$0 cm$"],
        "correta": "$3 cm$",
        "resolucao": "A função altura é $h(t) = 15 - 3t$. Para $t = 4: $"
        "$h(4) = 15 - 3(4) = 15 - 12 = 3 cm$."
    },
    {
        "id": 8,
        "enunciado": """Em uma função $f(x) = -3x + 9$, qual é o valor da raiz 
        (zero da função)?""",
        "opcoes": ["$3$", "$-3$", "$9$", "$0$"],
        "correta": "$3$",
        "resolucao": "Para achar a raiz, igualamos a zero: $-3x + 9 = 0$ => "
        "$3x = 9 $=> $x = 3$."
    },
    {
        "id": 9,
        "enunciado": """Um plano telefônico cobra R\$ 30,00 mensais fixos e 
        oferece minutos ilimitados, mas cobra R\$ 0,50 por SMS enviado. Se a 
        conta veio R\$ 42,50, quantos SMS foram enviados?""",
        "opcoes": ["$20$", "$25$", "$30$", "$15$"],
        "correta": "$25$",
        "resolucao": "$C(x) = 0,50x + 30$. Se $C(x) = 42,50$, então $42,50 = $"
        "$0,50x + 30. 12,50 = 0,50x$. $x = 12,5 / 0,5 = 25$."
    },
    {
        "id": 10,
        "enunciado": """Uma máquina agrícola foi comprada nova por R\$ 50.000,00. 
        Sabe-se que ela sofre uma desvalorização (perda de valor) fixa de 
        R\$ 4.000,00 por ano de uso. Qual será o valor dessa desvalorização após 
        6 anos?""",
        "opcoes": ["R\$ 26.000,00", "R\$ 24.000,00", "R\$ 30.000,00", 
                   "R\$ 46.000,00"],
        "correta": "R\$ 26.000,00",
        "resolucao": """O valor inicial é 50.000 e a taxa de variação 
        é -4.000 (perda). A função é $V(t) = 50000 - 4000t$. 
        Para $t = 6: V(6) = 50000 - 4000(6) = 50000 - 24000 = 26.000$."""
    }
]

if 'submetido' not in st.session_state:
    st.session_state.submetido = False

def pagina_quiz():

    questoes = questoes_1_grau  
    
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