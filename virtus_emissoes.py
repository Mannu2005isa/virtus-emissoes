import sqlite3
from datetime import date, datetime, timedelta

import streamlit as st
import requests
import base64
# ==============================
# CONFIGURAÇÃO DA PÁGINA (TEM QUE SER A PRIMEIRA COISA)
# ==============================
st.set_page_config(
    page_title="Virtus Solution",
    page_icon="logo metalizada.png",   
    layout="wide",
)
st.markdown("""
<style>

/* CAIXA DO LOGIN — CENTRALIZADA */
.login-box {
    max-width: 380px;      /* 🔎 controla a largura */
    margin: 0 auto;        /* 🔎 centraliza */
    padding: 25px 30px;
    border-radius: 16px;
}

/* Campos do login menores */
.login-box input {
    height: 2.2rem !important;
    font-size: 0.9rem !important;
}

</style>
""", unsafe_allow_html=True)

# --- função para converter a imagem em base64 ---
def img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# troca pelo nome da sua imagem, se for diferente
owl_b64 = img_to_base64("logo metalizada.png")
def fundo_login():
    """Coruja grande, mais central, para a tela de login."""
    st.markdown(
        f"""
        <style>
        .stApp::before {{
            content: "";
            position: fixed;
            top: 9%;
            right: 45%;
            width: 55%;
            height: 110%;
            background-image: url("data:image/png;base64,{owl_b64}");
            background-repeat: no-repeat;
            background-size: contain;
            opacity: 0.1;          /* transparência do login */
            pointer-events: none;
            z-index: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def fundo_principal():
    """Coruja no canto direito, metade para fora, para dentro do sistema."""
    st.markdown(
        f"""
        <style>
        .stApp::before {{
            content: "";
            position: fixed;
            top: 5%;
            right: -20%;        /* empurra metade para fora */
            width: 70%;
            height: 110%;
            background-image: url("data:image/png;base64,{owl_b64}");
            background-repeat: no-repeat;
            background-size: contain;
            opacity: 0.10;           /* transparência do sistema */
            pointer-events: none;
            z-index: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def apply_virtus_style():
    st.markdown(
        """
        <style>

}
        /* ==============================
           FONTE GLOBAL
        ============================== */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');

        * {
            font-family: 'outfit', sans-serif !important;
        }

         /* ==============================
           BARRA SUPERIOR (HEADER)
        ============================== */
        [data-testid="stHeader"] {
            background: rgba(237, 232, 225, 0.10) !important;  /* cor + transparência */
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
            border-bottom: 1px solid transparent !important;
        }

        /* Cor dos ícones/textos da barra */
        [data-testid="stHeader"] * {
            color: #EDE8E1 !important;
        }
        
        /* ==============================
           FUNDO DO APP / LAYOUT
        ============================== */
        .stApp {
            background: linear-gradient(135deg, #34201B 0%, #251914 45%, #1C1814 100%) !important;
        }

        /* Espaço do conteúdo principal */
        .block-container {
            padding-top: 4rem !important;
            padding-bottom: 3rem !important;
            max-width: 2000px !important;
        }

        /* Cor do texto/ícones da barra */
        header[data-testid="stAppHeader"] * {
            color: #EDE8E1 !important;
        }

        header[data-testid="stAppHeader"] {
            background: rgba(237, 232, 225, 0.6) !important;
            backdrop-filter: blur(6px);
        }

        /* ==============================
           SIDEBAR
        ============================== */
        section[data-testid="stSidebar"] {
            background: rgba(237, 232, 225, 0.2) !important;
            backdrop-filter: blur(6px);
        
        /* ==============================
        SIDEBAR — GLASS + SHINE STRONG
        ============================== */

        section[data-testid="stSidebar"] {
            background: rgba(52, 32, 27, 0.78) !important;   /* mais claro */
            backdrop-filter: blur(18px) saturate(140%) !important; /* vidro mais forte */
            -webkit-backdrop-filter: blur(18px) saturate(140%) !important;
            border-right: 1px solid rgba(255,255,255,0.15);
            position: relative;
            overflow: hidden;
        }

        /* CAMADA DO BRILHO */
        section[data-testid="stSidebar"]::before {
            content: "";
            position: absolute;
            top: -10%;
            left: -75%;
            width: 70%;                         /* faixa mais larga */
            height: 120%;
            background: linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.55),          /* brilho bem mais forte */
                rgba(255,255,255,0.15),
                transparent
            );
            transform: skewX(-25deg);
            filter: blur(2px);                   /* deixa mais suave porém mais visível */
        }

        /* BRILHO AO PASSAR O MOUSE */
        section[data-testid="stSidebar"]:hover::before {
            animation: shine 2.2s ease-in-out;
        }

        /* ANIMAÇÃO MAIS LENTA E LONGA */
        @keyframes shine {
            0%   { left: -90%; opacity: 0.4; }
            40%  { opacity: 0.9; }
            100% { left: 140%; opacity: 0; }
        }

            border-right: 1px solid transparent !important;
        }

        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] p {
            color: #EDE8E1 !important;
        }
    
    /* ===== MENU DA SIDEBAR ===== */

        section[data-testid="stSidebar"] h2 {
            font-size: 1.6rem !important;
            font-weight: 700 !important;
            color: #EDE8E1 !important;
        }

        section[data-testid="stSidebar"] input[type="radio"] {
            accent-color: #251914 !important;
            width: 18px;
            height: 18px;
            border: 2px solid #EDE8E1;
            border-radius: 50%;
        }


        /* ==============================
           TÍTULOS E TEXTOS
        ============================== */
        h1, h2, h3 {
            color: #EDE8E1 !important;
            letter-spacing: 0.02em;
        }

        h1 {
            font-size: 3rem !important; 
            font-weight: 800 !important;
        }

        h2, h3 {
            font-weight: 600 !important;
        }

        p, label, li {
            color: #ede8e1 !important;
        }


        /* ==============================
           CARTÕES / CONTAINERS
        ============================== */
        .stMarkdown, .stText, .stDataFrame, .stTable, .stAlert {
            border-radius: 12px !important;
        }

        /* ==============================
           CAMPOS DE ENTRADA (INPUTS)
        ============================== */

        /* TextInput */
        div[data-testid="stTextInput"] input {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border-radius: 5px !important;
            border: 2px solid #C7C2BA !important;
        }

        /* NumberInput */
        div[data-testid="stNumberInput"] input {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border-radius: 5px !important;
            border: 2px solid #C7C2BA !important;
        }

        /* TextArea */
        textarea {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border-radius: 10px !important;
            border: 2px solid #C7C2BA !important;
        }

        /* Selectbox */
        div[data-baseweb="select"] > div {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border-radius: 10px !important;
            border: 2px solid #C7C2BA !important;
        }

        /* DateInput */
        div[data-testid="stDateInput"] input {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border-radius: 10px !important;
            border: 2px solid #C7C2BA !important;
        }

        /* Placeholders */
        input::placeholder,
        textarea::placeholder {
            color: #f0f2f6 !important;
        }

        /* Foco */
        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stNumberInput"] input:focus,
        textarea:focus,
        div[data-testid="stDateInput"] input:focus,
        div[data-baseweb="select"] > div:focus-within {
            border: 2px solid #A86185 !important;
            background-color: #FFFFFF !important;
            outline: none !important;
        }

        /* Labels dos campos */
        label, .st-emotion-cache-1v0mbdj {
            color: #F7F3EC !important;
            font-weight: 500 !important;
        }

        
        /* ==============================
           BOTÕES (TODOS)
        ============================== */

        /* Desabilitado */
        div[data-testid="stFormSubmitButton"] > button:disabled,
        div[data-testid="stFormSubmitButton"] > button:disabled * {
            background-color: #EDE8E1 !important;
            color: #251914 !important;          /* continua marrom mesmo desabilitado */
            border-color: #C7C2BA !important;
        }

        /* Botões normais e de formulário */
        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button,
        button[kind="primary"],
        button[kind="secondary"] {
            background-color: transparent !important;
            color: #251914 !important;
            border: 1px solid #EDE8E1 !important;
            border-radius: 30px !important;
            font-weight: 600 !important;
            padding: 0.4rem 1.4rem !important;
            box-shadow: none !important;
        }

        /* Hover */
        div.stButton > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover,
        button[kind="primary"]:hover,
        button[kind="secondary"]:hover {
            background-color: transparent !important;
            color: #251914 !important;
            border-color: transparent !important;
        }

        /* ==============================
           TABS
        ============================== */
        button[role="tab"] {
            color:  #251914 !important;
            background-color: transparent !important;
            border-radius: 999px !important;
            padding: 0.4rem 1rem !important;
        }

        button[role="tab"][aria-selected="true"] {
            background-color: transparent !important;
            color: #251914 !important;
        }

        /* ==============================
           ALERTAS
        ============================== */
        .stAlert {
            background-color: #2C1B18 !important;
            border: 1px solid #3A2420 !important;
        }

        .stAlert > div {
            color: #F7F3EC !important;
        }

        /* ==============================
           DATAFRAME / TABELAS
        ============================== */
        .stDataFrame {
            background-color: #2B1A17 !important;
            border-radius: 12px !important;
            padding: 0.4rem !important;
        }

        .stDataFrame table {
            color: #F7F3EC !important;
        }

        .stDataFrame tbody tr:nth-child(even) {
            background-color: #231511 !important;
        }

        .stDataFrame tbody tr:nth-child(odd) {
            background-color: #1E120F !important;
        }

        /* ==============================
           LINKS
        ============================== */
        a {
            color: #A86185 !important;
        }

        a:hover {
            color: #E79ABB !important;
        }

        //* ====== AJUSTE ESPECÍFICO DO CAMPO DE SENHA ====== */

        /* Input de senha (mesma cara dos outros, mas preparado pra “juntar” com o olho) */
        div[data-testid="stTextInput"] input[type="password"] {
            background-color: #ede8e1 !important;
            color: #251914 !important;
            border: 2px solid #C7C2BA !important;
            border-right: none !important;                 /* tira a divisória do lado do olho */
            border-radius: 8px 0 0 8px !important;         /* arredonda só o lado esquerdo */
        }

        /* Botão do olho – Streamlit usa um button com aria-label “Mostrar senha / Ocultar senha” */
        div[data-testid="stTextInput"] button[aria-label*="senha"] {
            background-color: #ede8e1 !important;          /* mesma cor do input */
            border: 2px solid #C7C2BA !important;          /* mesma borda */
            border-left: none !important;                  /* cola visualmente no input */
            border-radius: 0 8px 8px 0 !important;         /* arredonda só o lado direito */
            box-shadow: none !important;
            padding: 0 14px !important;
        }

        /* Cor do ícone do olho */
        div[data-testid="stTextInput"] button[aria-label*="senha"] svg {
            color: #251914 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

apply_virtus_style()

# ==============================
# LOGIN ÚNICO DA VIRTUS
# ==============================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login_screen():
    # 3 colunas: esquerda, centro (login), direita
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:   # tudo do login vai aqui no meio
        # logo + título
        col1, col2 = st.columns([1, 3])

        with col2:
            st.markdown(
                """
            <div style="text-align:center; margin-left:-130px;">
                <h2 style="margin-top: 10px; margin-bottom: 1px; margin-left: 0px;">
                    Virtus Emissões
                </h2>
                <p style="color:#ede8e1;">
                    🔒 Acesso restrito · Virtus Solution Assessoria Contábil
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")  # espaço

        # usuários válidos
        usuarios_validos = {
            "veronica": "virtus2026",
            "emannuely": "mannu2026",
        }

        # FORMULÁRIO DE LOGIN
        with st.form("login_form"):
            usuario = st.text_input("USUÁRIO")
            senha   = st.text_input("SENHA", type="password")
            entrar  = st.form_submit_button("ENTRAR")

        if entrar:
            if usuario in usuarios_validos and senha == usuarios_validos[usuario]:
                st.session_state.logged_in = True
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def require_login():
    # ainda não logou → mostra fundo do login e tela de login
    if not st.session_state.logged_in:
        fundo_login()      # 👈 coruja da tela de login
        login_screen()
        st.stop()
    else:
        # já logado → aplica fundo da tela principal
        fundo_principal()  # 👈 coruja no canto direito

# ---------- TÍTULO PRINCIPAL DA APLICAÇÃO ----------
require_login()   # isso vai decidir qual fundo usar

st.title("Emissões dos clientes")
st.markdown(
    """
    <p style="
        color:#ede8e1;
        font-size: 1rem;
        margin-top: 1px;
    ">
        Controle interno de emissões de notas da <strong>Virtus Solution</strong>
    </p>
    """,
    unsafe_allow_html=True,
)


# ⬇️ AGORA SIM, CHAMA A FUNÇÃO
apply_virtus_style()


# ==============================
# CONEXÃO E CRIAÇÃO DO BANCO
# ==============================

def get_connection():
    # check_same_thread=False é importante para o Streamlit
    conn = sqlite3.connect("virtus_emissoes.db", check_same_thread=False)
    return conn


def init_db(conn):
    cur = conn.cursor()

    # Tabela de empresas
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT
        );
        """
    )

    # Tabela de clientes
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            observacoes TEXT
        );
        """
    )

    # Tabela de projetos
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_empresa INTEGER NOT NULL,
            id_cliente INTEGER NOT NULL,
            nome TEXT NOT NULL,
            tipo_nota TEXT,
            valor_padrao REAL,
            periodicidade TEXT,
            dia_fixo INTEGER,
            data_inicio TEXT,
            data_fim TEXT,
            ativo INTEGER DEFAULT 1,
            FOREIGN KEY (id_empresa) REFERENCES empresas(id),
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        );
        """
    )

    # Tabela de emissões
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS emissoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_projeto INTEGER NOT NULL,
            data_prevista TEXT NOT NULL,
            status TEXT DEFAULT 'Pendente',   -- Pendente, Emitida, Atrasada
            data_emitida TEXT,
            numero_nf TEXT,
            observacoes TEXT,
            FOREIGN KEY (id_projeto) REFERENCES projetos(id)
        );
        """
    )

     # ✅ NOVA TABELA: recebimentos
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS recebimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_emissao INTEGER NOT NULL UNIQUE,      -- 1 recebimento por emissão (pode virar 1:N no futuro)
            data_vencimento TEXT NOT NULL,           -- YYYY-MM-DD
            valor_previsto REAL NOT NULL DEFAULT 0,
            forma_pagamento TEXT,                    -- PIX, boleto, etc.
            status TEXT NOT NULL DEFAULT 'A Receber', -- A Receber, Pago
            data_pagamento TEXT,                     -- YYYY-MM-DD
            valor_pago REAL,
            observacoes TEXT,
            FOREIGN KEY (id_emissao) REFERENCES emissoes(id)
        );
        """
    )
    
    conn.commit()


conn = get_connection()
init_db(conn)

def consultar_cnpj(cnpj: str) -> dict:
    """
    Consulta CNPJ na BrasilAPI e retorna um dicionário
    com os dados principais para preencher o cadastro.
    """
    # deixa só números
    cnpj_limpo = "".join(filter(str.isdigit, cnpj))

    if len(cnpj_limpo) != 14:
        raise ValueError("CNPJ deve ter 14 dígitos (apenas números).")

    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    resp = requests.get(url, timeout=10)

    if resp.status_code != 200:
        raise ValueError("CNPJ não encontrado ou BrasilAPI fora do ar.")

    data = resp.json()

    # Campos principais (veem da própria BrasilAPI):contentReference[oaicite:5]{index=5}
    return {
        "cnpj": data.get("cnpj", cnpj_limpo),
        "razao_social": data.get("razao_social", ""),
        "nome_fantasia": data.get("nome_fantasia", ""),
        "logradouro": data.get("logradouro", ""),
        "numero": data.get("numero", ""),
        "complemento": data.get("complemento", ""),
        "bairro": data.get("bairro", ""),
        "municipio": data.get("municipio", ""),
        "uf": data.get("uf", ""),
        "cep": data.get("cep", ""),
        "cnae": data.get("cnae_fiscal_descricao", ""),
        "situacao": data.get("descricao_situacao_cadastral", ""),
    }


# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def data_br(data_str):
    if not data_str:
        return ""
    return datetime.strptime(data_str, "%Y-%m-%d").strftime("%d/%m/%Y")


def criar_ou_atualizar_recebimento(id_emissao, data_vencimento, valor_previsto, forma_pagamento, observacoes=""):
    cur = conn.cursor()
    # tenta inserir; se já existir, atualiza
    cur.execute(
        """
        INSERT INTO recebimentos (id_emissao, data_vencimento, valor_previsto, forma_pagamento, observacoes)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(id_emissao) DO UPDATE SET
            data_vencimento=excluded.data_vencimento,
            valor_previsto=excluded.valor_previsto,
            forma_pagamento=excluded.forma_pagamento,
            observacoes=excluded.observacoes
        ;
        """,
        (id_emissao, data_vencimento, float(valor_previsto), forma_pagamento, observacoes)
    )
    conn.commit()


def marcar_recebimento_pago(id_emissao, data_pagamento, valor_pago):
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE recebimentos
        SET status='Pago',
            data_pagamento=?,
            valor_pago=?
        WHERE id_emissao=?;
        """,
        (data_pagamento, float(valor_pago), id_emissao)
    )
    conn.commit()


def buscar_recebimentos(data_ini=None, data_fim=None, id_cliente=None):
    cur = conn.cursor()

    query = """
        SELECT
            em.id AS id_emissao,
            em.data_prevista,
            em.status AS status_emissao,
            em.data_emitida,
            em.numero_nf,
            p.nome AS projeto_nome,
            c.nome AS cliente_nome,
            e.nome AS empresa_nome,
            r.data_vencimento,
            r.valor_previsto,
            r.forma_pagamento,
            r.status AS status_recebimento,
            r.data_pagamento,
            r.valor_pago
        FROM emissoes em
        JOIN projetos p ON p.id = em.id_projeto
        JOIN clientes c ON c.id = p.id_cliente
        JOIN empresas e ON e.id = p.id_empresa
        LEFT JOIN recebimentos r ON r.id_emissao = em.id
        WHERE 1=1
    """
    params = []

    if id_cliente:
        query += " AND c.id = ?"
        params.append(id_cliente)

    if data_ini:
        query += " AND date(COALESCE(r.data_vencimento, em.data_prevista)) >= date(?)"
        params.append(data_ini)

    if data_fim:
        query += " AND date(COALESCE(r.data_vencimento, em.data_prevista)) <= date(?)"
        params.append(data_fim)

    query += " ORDER BY date(COALESCE(r.data_vencimento, em.data_prevista));"

    cur.execute(query, params)
    itens = fetchall_dict(cur)

    # ✅ Alertas automáticos
    hoje = date.today()
    for it in itens:
        it["alerta"] = ""
        if it.get("status_recebimento") == "Pago":
            continue

        # se ainda não cadastrou vencimento, avisa
        if not it.get("data_vencimento"):
            it["alerta"] = "⚠️ Sem vencimento cadastrado"
            continue

        venc = datetime.strptime(it["data_vencimento"], "%Y-%m-%d").date()
        diff = (venc - hoje).days

        if diff < 0:
            it["alerta"] = f"🔴 Em atraso há {-diff} dia(s)"
        elif diff == 0:
            it["alerta"] = "🟠 Vence HOJE"
        elif diff <= 5:
            it["alerta"] = f"🟡 Vence em {diff} dia(s)"
        else:
            it["alerta"] = "🟢 OK"

    return itens


def montar_mensagem_vencimento(item):
    return (
        f"Olá! Tudo bem?\n\n"
        f"Passando para lembrar que a NF {item.get('numero_nf') or '(sem nº)'} "
        f"({item['empresa_nome']} → {item['cliente_nome']}) vence em {item.get('data_vencimento')}.\n"
        f"Valor: R$ {item.get('valor_previsto') or 0:.2f}\n\n"
        f"Se precisar de qualquer coisa, fico à disposição."
    )


def montar_mensagem_atraso(item):
    return (
        f"Olá! Tudo bem?\n\n"
        f"Identificamos que a NF {item.get('numero_nf') or '(sem nº)'} "
        f"({item['empresa_nome']} → {item['cliente_nome']}) está em atraso desde {item.get('data_vencimento')}.\n"
        f"Valor: R$ {item.get('valor_previsto') or 0:.2f}\n\n"
        f"Consegue me confirmar a previsão de pagamento, por favor?"
    )


def fetchall_dict(cur):
    """
    Converte resultado do cursor em lista de dicionários.
    Facilita para usar com o Streamlit.
    """
    cols = [c[0] for c in cur.description]
    rows = cur.fetchall()
    return [dict(zip(cols, r)) for r in rows]


def get_empresas():
    cur = conn.cursor()
    cur.execute("SELECT * FROM empresas ORDER BY nome;")
    return fetchall_dict(cur)


def get_clientes():
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes ORDER BY nome;")
    return fetchall_dict(cur)


def get_projetos(only_active=True):
    cur = conn.cursor()
    if only_active:
        cur.execute(
            """
            SELECT p.*, e.nome AS empresa_nome, c.nome AS cliente_nome
            FROM projetos p
            JOIN empresas e ON e.id = p.id_empresa
            JOIN clientes c ON c.id = p.id_cliente
            WHERE p.ativo = 1
            ORDER BY e.nome, c.nome, p.nome;
            """
        )
    else:
        cur.execute(
            """
            SELECT p.*, e.nome AS empresa_nome, c.nome AS cliente_nome
            FROM projetos p
            JOIN empresas e ON e.id = p.id_empresa
            JOIN clientes c ON c.id = p.id_cliente
            ORDER BY e.nome, c.nome, p.nome;
            """
        )
    return fetchall_dict(cur)


def adicionar_empresa(nome, cnpj):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO empresas (nome, cnpj) VALUES (?, ?);",
        (nome, cnpj if cnpj else None),
    )
    conn.commit()


def adicionar_cliente(nome, observacoes):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO clientes (nome, observacoes) VALUES (?, ?);",
        (nome, observacoes if observacoes else None),
    )
    conn.commit()


def adicionar_projeto(
    id_empresa,
    id_cliente,
    nome,
    tipo_nota,
    valor_padrao,
    periodicidade,
    dia_fixo,
    data_inicio,
    data_fim,
    ativo,
):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO projetos 
            (id_empresa, id_cliente, nome, tipo_nota, valor_padrao,
             periodicidade, dia_fixo, data_inicio, data_fim, ativo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
        (
            id_empresa,
            id_cliente,
            nome,
            tipo_nota,
            valor_padrao,
            periodicidade,
            dia_fixo,
            data_inicio,
            data_fim,
            1 if ativo else 0,
        ),
    )
    
    conn.commit()


# ------------------------------
# GERAÇÃO DE DATAS DE EMISSÃO
# ------------------------------

def add_months(current_date, months):
    """
    Soma 'months' meses a uma data, cuidando de ano/mês.
    Ex.: 31/01 + 1 mês -> 28/02 (ou 29/02 em ano bissexto).
    """
    year = current_date.year
    month = current_date.month + months
    day = current_date.day

    # Ajusta ano/mês
    while month > 12:
        month -= 12
        year += 1

    # Tenta criar a data, se o dia não existir (ex. 31/02),
    # volta até achar um dia válido (último dia do mês).
    while True:
        try:
            return date(year, month, day)
        except ValueError:
            day -= 1
            if day < 1:
                # fallback, não deveria acontecer na prática
                return date(year, month, 1)


def gerar_agenda_projeto(id_projeto):
    """
    Gera (ou regenera) as emissões previstas de um projeto
    com base em data_inicio, data_fim, dia_fixo e periodicidade.
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM projetos
        WHERE id = ?;
        """,
        (id_projeto,),
    )
    projeto = cur.fetchone()

    if not projeto:
        return "Projeto não encontrado."

    # Índices do SELECT acima:
    # 0:id, 1:id_empresa, 2:id_cliente, 3:nome, 4:tipo_nota,
    # 5:valor_padrao, 6:periodicidade, 7:dia_fixo,
    # 8:data_inicio, 9:data_fim, 10:ativo
    periodicidade = projeto[6]
    dia_fixo = projeto[7]
    data_inicio = projeto[8]
    data_fim = projeto[9]

    if not (data_inicio and data_fim and dia_fixo and periodicidade):
        return "Projeto sem informações suficientes (data início/fim, dia fixo ou periodicidade)."

    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

    # Define o intervalo de meses de acordo com a periodicidade
    mapa_periodicidade = {
        "Mensal": 1,
        "Bimestral": 2,
        "Trimestral": 3,
        "Semestral": 6,
        "Anual": 12,
    }

    if periodicidade not in mapa_periodicidade:
        return "Periodicidade não reconhecida. Use Mensal, Bimestral, Trimestral ou Anual."

    passo_meses = mapa_periodicidade[periodicidade]

    # Começa do mês de data_inicio, ajustando o dia para dia_fixo
    primeira_data = date(data_inicio.year, data_inicio.month, dia_fixo)
    if primeira_data < data_inicio:
        # se a primeira data calculada for antes do início,
        # pula para o próximo mês
        primeira_data = add_months(primeira_data, passo_meses)

    # Apaga emissões anteriores do projeto (para não duplicar)
    cur.execute("DELETE FROM emissoes WHERE id_projeto = ?;", (id_projeto,))

    datas_geradas = []
    atual = primeira_data
    while atual <= data_fim:
        datas_geradas.append(atual)
        atual = add_months(atual, passo_meses)

    # Insere as novas emissões
    for d in datas_geradas:
        cur.execute(
            """
            INSERT INTO emissoes (id_projeto, data_prevista, status)
            VALUES (?, ?, 'Pendente');
            """,
            (id_projeto, d.strftime("%Y-%m-%d")),
        )

    conn.commit()
    return f"{len(datas_geradas)} emissões geradas para o projeto."


# ------------------------------
# ATUALIZAÇÃO DE EMISSÃO (marcar como emitida)
# ------------------------------

def marcar_emissao_emitida(id_emissao, data_emitida, numero_nf):
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE emissoes
        SET status = 'Emitida',
            data_emitida = ?,
            numero_nf = ?
        WHERE id = ?;
        """,
        (data_emitida, numero_nf, id_emissao),
    )
    conn.commit()


def buscar_emissoes_filtradas(id_cliente=None, data_ini=None, data_fim=None):
    cur = conn.cursor()
    query = """
        SELECT 
            em.id,
            em.data_prevista,
            em.status,
            em.data_emitida,
            em.numero_nf,
            p.nome AS projeto_nome,
            c.nome AS cliente_nome,
            e.nome AS empresa_nome
        FROM emissoes em
        JOIN projetos p ON p.id = em.id_projeto
        JOIN clientes c ON c.id = p.id_cliente
        JOIN empresas e ON e.id = p.id_empresa
        WHERE 1 = 1
    """
    params = []

    if id_cliente:
        query += " AND c.id = ?"
        params.append(id_cliente)

    if data_ini:
        query += " AND date(em.data_prevista) >= date(?)"
        params.append(data_ini)

    if data_fim:
        query += " AND date(em.data_prevista) <= date(?)"
        params.append(data_fim)

    query += " ORDER BY em.data_prevista;"

    cur.execute(query, params)
    emissoes = fetchall_dict(cur)

    # --- Cálculo de alerta (atrasada / próxima) ---
    hoje = date.today()

    for em in emissoes:
        # só calcula alerta para notas não emitidas
        if em["status"] != "Emitida":
            data_prev = datetime.strptime(em["data_prevista"], "%Y-%m-%d").date()
            diff = (data_prev - hoje).days

            if diff < 0:
                em["status"] = "Atrasada"
                em["alerta"] = f"ATRASADA há {-diff} dia(s)"
            elif diff == 0:
                em["alerta"] = "Emitir HOJE"
            elif 0 < diff <= 7:
                em["alerta"] = f"Emitir em {diff} dia(s)"
            else:
                em["alerta"] = "Pendente"
        else:
            em["alerta"] = ""

    return emissoes



# ==============================
# INTERFACE - MENU LATERAL
# ==============================

# EXIGIR LOGIN ANTES DE MOSTRAR O SISTEMA
require_login()

with st.sidebar:
    # TÍTULO PERSONALIZADO DO MENU
    st.markdown(
        "<h2 class='virtus-menu-titulo'>Menu</h2>",
        unsafe_allow_html=True,
    )

    # RADIO SEM LABEL (label vazio)
    menu = st.radio(
    "",
    ["Cadastros", "Agenda de Emissões", "Recebimentos"],  # ✅ novo item
    index=0,
    key="menu_principal",
)


# ==============================
# PÁGINA: CADASTROS
# ==============================

if menu == "Cadastros":
    st.subheader("Cadastros")

    tab_empresas, tab_clientes, tab_projetos = st.tabs(
        ["🏢 Empresas", "👤 Clientes", "📁 Projetos"]
    )

    # --------- Empresas ---------
    with tab_empresas:
        st.markdown("### Cadastro de Empresas")

        with st.form("form_empresas"):
            nome = st.text_input("Nome da empresa *")
            cnpj = st.text_input("CNPJ (opcional)")
            submitted = st.form_submit_button("Salvar empresa")

        if submitted:
            if not nome.strip():
                st.error("Informe o nome da empresa.")
            else:
                adicionar_empresa(nome.strip(), cnpj.strip())
                st.success("Empresa cadastrada com sucesso!")

        st.markdown("#### Empresas cadastradas")
        empresas = get_empresas()
        if empresas:
            st.table(empresas)
        else:
            st.info("Nenhuma empresa cadastrada ainda.")

    # --------- Clientes ---------
    with tab_clientes:
        st.markdown("### Cadastro de Clientes (cliente do seu cliente)")

    # --- BUSCA PELO CNPJ ANTES DO FORM ---
    cnpj_busca = st.text_input("CNPJ do cliente (opcional)", key="cliente_cnpj_busca")

    dados_preenchidos = {}

    if st.button("🔎 Buscar dados pelo CNPJ"):
        if not cnpj_busca.strip():
            st.error("Informe um CNPJ para buscar.")
        else:
            try:
                dados_preenchidos = consultar_cnpj(cnpj_busca)
                st.success(f"Dados carregados para: {dados_preenchidos.get('razao_social')}")
                # Guarda no session_state pra usar logo abaixo no form
                st.session_state["cliente_cnpj_dados"] = dados_preenchidos
            except Exception as e:
                st.error(f"Erro ao consultar CNPJ: {e}")

    # Recupera dados já buscados anteriormente (se existirem)
    dados_preenchidos = st.session_state.get("cliente_cnpj_dados", {})

    # --- FORMULÁRIO DE CADASTRO ---
    with st.form("form_clientes"):
        nome_c = st.text_input(
            "Nome / Razão Social *",
            value=dados_preenchidos.get("razao_social", "")
        )
        cnpj_c = st.text_input(
            "CNPJ (apenas números)",
            value=dados_preenchidos.get("cnpj", "")
        )
        endereco_c = st.text_input(
            "Endereço",
            value=f"{dados_preenchidos.get('logradouro', '')}, {dados_preenchidos.get('numero', '')}".strip(", ")
        )
        bairro_c = st.text_input(
            "Bairro",
            value=dados_preenchidos.get("bairro", "")
        )
        cidade_c = st.text_input(
            "Cidade",
            value=dados_preenchidos.get("municipio", "")
        )
        uf_c = st.text_input(
            "UF",
            value=dados_preenchidos.get("uf", "")
        )
        cep_c = st.text_input(
            "CEP",
            value=dados_preenchidos.get("cep", "")
        )
        ie_c = st.text_input(
            "Inscrição Estadual (preencher manualmente por enquanto)"
        )
        obs_c = st.text_area("Observações (opcional)")

        submitted_c = st.form_submit_button("Salvar cliente")

    if submitted_c:
        if not nome_c.strip():
            st.error("Informe o nome / razão social do cliente.")
        else:
            # Aqui você pode adaptar sua função de gravação para salvar também CNPJ, endereço, etc.
            adicionar_cliente(nome_c.strip(), obs_c.strip())
            st.success("Cliente cadastrado com sucesso!")
            # limpa os dados buscados
            st.session_state["cliente_cnpj_dados"] = {}

    # --------- Projetos ---------
    with tab_projetos:
        st.markdown("### Cadastro de Projetos")

        empresas = get_empresas()
        clientes = get_clientes()

        if not empresas or not clientes:
            st.warning(
                "Para cadastrar projetos, primeiro cadastre ao menos uma empresa e um cliente."
            )
        else:
            # Mapas para facilitar selecionar no selectbox
            mapa_empresas = {e["nome"]: e["id"] for e in empresas}
            mapa_clientes = {c["nome"]: c["id"] for c in clientes}

            with st.form("form_projetos"):
                col1, col2 = st.columns(2)

                with col1:
                    empresa_nome = st.selectbox(
                        "Empresa *",
                        list(mapa_empresas.keys()),
                    )
                    cliente_nome = st.selectbox(
                        "Cliente *",
                        list(mapa_clientes.keys()),
                    )
                    nome_proj = st.text_input("Nome do projeto * (ex: Honorários Zenux/CROW)")

                with col2:
                    tipo_nota = st.selectbox(
                        "Tipo de nota",
                        ["Recorrente", "Avulsa"],
                    )
                    valor_padrao = st.number_input(
                        "Valor padrão da nota (opcional)",
                        min_value=0.0,
                        step=0.01,
                    )
                    periodicidade = st.selectbox(
                        "Periodicidade *",
                        ["Mensal", "Bimestral", "Trimestral", "Semestral", "Anual"],
                        )

                    col3, col4 = st.columns(2)
                with col3:
                    dia_fixo = st.number_input(
                        "Dia fixo de emissão (1 a 31) *",
                        min_value=1,
                        max_value=31,
                        step=1,
                        value=25,
                    )
                    data_inicio = st.date_input(
                        "Data de início *",
                        value=date.today(),
                    )

                with col4:
                    data_fim = st.date_input(
                        "Data de fim *",
                        value=date.today().replace(month=12, day=31),
                    )
                    ativo = st.checkbox("Projeto ativo", value=True)

                submitted_p = st.form_submit_button("Salvar projeto")

            if submitted_p:
                if not nome_proj.strip():
                    st.error("Informe o nome do projeto.")
                elif data_fim < data_inicio:
                    st.error("Data de fim não pode ser anterior à data de início.")
                else:
                    adicionar_projeto(
                        mapa_empresas[empresa_nome],
                        mapa_clientes[cliente_nome],
                        nome_proj.strip(),
                        tipo_nota,
                        float(valor_padrao) if valor_padrao else 0.0,
                        periodicidade,
                        int(dia_fixo),
                        data_inicio.strftime("%Y-%m-%d"),
                        data_fim.strftime("%Y-%m-%d"),
                        ativo,
                    )
                    st.success("Projeto cadastrado com sucesso!")

            st.markdown("#### Projetos cadastrados")
            projetos = get_projetos(only_active=False)
            if projetos:
                st.table(projetos)
            else:
                st.info("Nenhum projeto cadastrado ainda.")

            st.markdown("---")
            st.markdown("### Gerar/Atualizar agenda de um projeto")

            projetos_ativos = get_projetos(only_active=True)
            if projetos_ativos:
                mapa_proj = {
                    f'{p["empresa_nome"]} - {p["cliente_nome"]} - {p["nome"]} (id {p["id"]})': p["id"]
                    for p in projetos_ativos
                }
                proj_escolhido_label = st.selectbox(
                    "Selecione o projeto:",
                    list(mapa_proj.keys()),
                )
                if st.button("Gerar agenda deste projeto"):
                    msg = gerar_agenda_projeto(mapa_proj[proj_escolhido_label])
                    if "emissões geradas" in msg:
                        st.success(msg)
                    else:
                        st.error(msg)
            else:
                st.info("Não há projetos ativos para gerar agenda.")


# ==============================
# PÁGINA: AGENDA DE EMISSÕES
# ==============================

elif menu == "Agenda de Emissões":
    st.subheader("Agenda de Emissões")

    clientes = get_clientes()
    mapa_clientes = {c["nome"]: c["id"] for c in clientes} if clientes else {}

    col_f1, col_f2, col_f3 = st.columns(3)

    with col_f1:
        nome_cliente_filtro = None
        if clientes:
            nome_cliente_filtro = st.selectbox(
                "Filtrar por cliente (opcional)",
                ["Todos"] + list(mapa_clientes.keys()),
            )
        else:
            st.info("Cadastre clientes na aba de Cadastros.")

    with col_f2:
       data_ini = st.date_input(
            "Data inicial (opcional)",
            value=date.today().replace(day=1),
            format="DD/MM/YYYY",
        )

    with col_f3:
        data_fim = st.date_input(
            "Data final (opcional)",
            value=date.today().replace(day=28),
            format="DD/MM/YYYY",
        )
    id_cliente_filtro = None
    if nome_cliente_filtro and nome_cliente_filtro != "Todos":
        id_cliente_filtro = mapa_clientes[nome_cliente_filtro]

    emissoes = buscar_emissoes_filtradas(
        id_cliente=id_cliente_filtro,
        data_ini=data_ini.strftime("%d-%m-%Y") if data_ini else None,
        data_fim=data_fim.strftime("%d-%m-%Y") if data_fim else None,
    )

    st.markdown("### Emissões encontradas")

    if emissoes:
        st.dataframe(emissoes, use_container_width=True)
    else:
        st.info("Nenhuma emissão encontrada para os filtros selecionados.")

    st.markdown("---")
    st.markdown("### Marcar emissão como emitida")

    # Apenas emissões pendentes para selecionar
    emissoes_pendentes = [e for e in emissoes if e["status"] != "Emitida"]

    if emissoes_pendentes:
        mapa_emissoes = {
            f'ID {e["id"]} - {e["data_prevista"]} - {e["cliente_nome"]} - {e["projeto_nome"]}':
            e["id"]
            for e in emissoes_pendentes
        }

        with st.form("form_emissao_emitida"):
            desc_escolhida = st.selectbox(
                "Selecione a emissão:",
                list(mapa_emissoes.keys()),
            )
            data_emitida = st.date_input(
                "Data da emissão",
                value=date.today(),
            )
            numero_nf = st.text_input("Número da NF *")
            obs = st.text_area("Observações (opcional)")
            submitted_emissao = st.form_submit_button("Marcar como emitida")

        if submitted_emissao:
            if not numero_nf.strip():
                st.error("Informe o número da NF.")
            else:
                marcar_emissao_emitida(
                    mapa_emissoes[desc_escolhida],
                    data_emitida.strftime("%d-%m-%Y"),
                    numero_nf.strip(),
                )
                # Observações não estão sendo salvas neste exemplo,
                # mas poderiam ser incluídas com um UPDATE extra.
                st.success("Emissão marcada como emitida com sucesso!")
    else:
        st.info("Não há emissões pendentes dentro dos filtros para marcar como emitida.")
elif menu == "Recebimentos":
    st.subheader("Recebimentos e Cobrança")

    clientes = get_clientes()
    mapa_clientes = {c["nome"]: c["id"] for c in clientes} if clientes else {}

    col1, col2, col3 = st.columns(3)

    with col1:
        nome_cliente = st.selectbox("Cliente (opcional)", ["Todos"] + list(mapa_clientes.keys())) if clientes else "Todos"

    with col2:
        data_ini = st.date_input("Data inicial", value=date.today().replace(day=1), format="DD/MM/YYYY")

    with col3:
        data_fim = st.date_input("Data final", value=date.today().replace(day=28), format="DD/MM/YYYY")

    id_cliente = None
    if nome_cliente != "Todos":
        id_cliente = mapa_clientes[nome_cliente]

    receb = buscar_recebimentos(
        data_ini=data_ini.strftime("%Y-%m-%d"),
        data_fim=data_fim.strftime("%Y-%m-%d"),
        id_cliente=id_cliente
    )

    st.markdown("### Lista de recebimentos")
    if receb:
        st.dataframe(receb, use_container_width=True)
    else:
        st.info("Nenhum recebimento encontrado.")

    st.markdown("---")
    st.markdown("### Cadastrar/Atualizar vencimento de uma emissão")

    # pega só emissões emitidas (recomendado) OU todas
    emissoes = buscar_emissoes_filtradas(id_cliente=id_cliente)  # usa sua função já existente
    # filtra para facilitar: só emitidas
    emissoes_emitidas = [e for e in emissoes if e["status"] == "Emitida"]

    if not emissoes_emitidas:
        st.info("Não há emissões 'Emitida' nos filtros para cadastrar recebimento.")
    else:
        mapa = {
            f'ID {e["id"]} | NF {e.get("numero_nf","")} | {e["cliente_nome"]} | {e["projeto_nome"]} | {e["data_prevista"]}': e["id"]
            for e in emissoes_emitidas
        }

        with st.form("form_cad_receb"):
            escolha = st.selectbox("Selecione a emissão", list(mapa.keys()))
            venc = st.date_input("Data de vencimento", value=date.today())
            valor_prev = st.number_input("Valor previsto", min_value=0.0, step=0.01)
            forma = st.selectbox("Forma de pagamento", ["", "PIX", "Boleto", "Transferência", "Cartão", "Outro"])
            obs = st.text_area("Observações (opcional)")
            ok = st.form_submit_button("Salvar recebimento")

        if ok:
            criar_ou_atualizar_recebimento(
                id_emissao=mapa[escolha],
                data_vencimento=venc.strftime("%Y-%m-%d"),
                valor_previsto=valor_prev,
                forma_pagamento=forma,
                observacoes=obs
            )
            st.success("Recebimento salvo com sucesso!")

    st.markdown("---")
    st.markdown("### Marcar como pago")

    # só os que têm vencimento e ainda não estão pagos
    pendentes = [r for r in receb if r.get("status_recebimento") != "Pago" and r.get("data_vencimento")]

    if not pendentes:
        st.info("Nenhum recebimento pendente para marcar como pago.")
    else:
        mapa_p = {
            f'Emissão {r["id_emissao"]} | NF {r.get("numero_nf","")} | vence {r.get("data_vencimento")} | {r["cliente_nome"]}': r["id_emissao"]
            for r in pendentes
        }

        with st.form("form_pago"):
            es = st.selectbox("Selecione", list(mapa_p.keys()))
            dt_pg = st.date_input("Data de pagamento", value=date.today())
            vl_pg = st.number_input("Valor pago", min_value=0.0, step=0.01)
            ok2 = st.form_submit_button("Marcar como pago")

        if ok2:
            marcar_recebimento_pago(mapa_p[es], dt_pg.strftime("%Y-%m-%d"), vl_pg)
            st.success("Marcado como pago!")

    st.markdown("---")
    st.markdown("### Mensagem pronta para cobrança (copiar e colar)")

    if receb:
        # sugere a primeira que esteja atrasada, senão a primeira da lista
        sugestao = None
        for r in receb:
            if "🔴" in (r.get("alerta") or ""):
                sugestao = r
                break
        if sugestao is None:
            sugestao = receb[0]

        msg_tipo = st.selectbox("Tipo de mensagem", ["Aviso de vencimento", "Cobrança de atraso"])
        if msg_tipo == "Aviso de vencimento":
            texto = montar_mensagem_vencimento(sugestao)
        else:
            texto = montar_mensagem_atraso(sugestao)

        st.text_area("Mensagem (copie e envie)", value=texto, height=180)
    else:
        st.info("Carregue uma lista para gerar mensagens.")
