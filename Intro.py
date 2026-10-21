import streamlit as st
from PIL import Image
import base64
import io

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Portafolio · Juan Pablo · Parte 2",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# ESTILOS — COSMIC AMETHYST
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --bg:            #0a0618;
        --bg-2:          #0f0a20;
        --surface:       #140c26;
        --surface-hover: #1e1133;
        --border:        #2d1f4a;
        --border-2:      #3d2b5f;
        --text:          #f0eaff;
        --text-2:        #c9bde0;
        --muted:         #9a8bb5;
        --muted-2:       #6b5a8a;
        --violet:        #c084fc;
        --violet-2:      #a855f7;
        --violet-soft:   rgba(192, 132, 252, 0.14);
        --amber:         #fbbf24;
        --emerald:       #34d399;
    }

    html, body, [class*="css"], .stApp, button, input, textarea, select {
        font-family: 'Inter', sans-serif !important;
        color: var(--text);
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Instrument Serif', serif !important;
        font-weight: 400 !important;
        color: var(--text) !important;
        letter-spacing: -0.01em !important;
    }

    /* ═══ FONDO ESPACIAL ═══ */
    .stApp {
        background-color: var(--bg) !important;
        background-image:
            radial-gradient(ellipse at 15% -5%, rgba(168, 85, 247, 0.18), transparent 45%),
            radial-gradient(ellipse at 85% 100%, rgba(192, 132, 252, 0.10), transparent 45%),
            radial-gradient(circle at 60% 30%, rgba(251, 191, 36, 0.035), transparent 35%),
            radial-gradient(circle at 20% 70%, rgba(52, 211, 153, 0.04), transparent 35%);
        background-attachment: fixed;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header[data-testid="stHeader"] { background: transparent; }

    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 4rem !important;
        max-width: 1240px !important;
    }

    /* ═══ HERO ═══ */
    .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 0.85rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        color: var(--violet);
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    .hero-kicker::before {
        content: '';
        display: inline-block;
        width: 34px;
        height: 1px;
        background: var(--violet);
    }
    .hero-h1 {
        font-family: 'Instrument Serif', serif !important;
        font-size: 3.6rem !important;
        line-height: 1.05 !important;
        letter-spacing: -0.02em !important;
        font-weight: 400 !important;
        margin: 0 0 1.5rem 0 !important;
        color: var(--text) !important;
    }
    .hero-h1 em {
        font-style: italic;
        color: var(--violet);
        font-weight: 400;
    }
    .hero-desc {
        font-size: 1.02rem;
        line-height: 1.75;
        color: var(--text-2);
        margin: 0 0 1.75rem 0;
        max-width: 560px;
        font-weight: 300;
    }
    .hero-desc strong {
        color: var(--text);
        font-weight: 600;
    }

    /* Badge "Parte 2" */
    .part-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.4rem 0.9rem 0.4rem 0.55rem;
        background: var(--violet-soft);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 100px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--violet);
        font-weight: 600;
        margin-bottom: 1.25rem;
    }
    .part-badge .num {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 22px;
        height: 22px;
        background: var(--violet);
        color: var(--bg);
        border-radius: 50%;
        font-size: 0.65rem;
        font-weight: 700;
    }

    /* Note */
    .hero-note {
        display: flex;
        align-items: flex-start;
        gap: 0.85rem;
        padding: 1rem 1.1rem;
        background: rgba(251, 191, 36, 0.06);
        border-left: 2px solid var(--amber);
        border-radius: 0 8px 8px 0;
        margin: 0 0 1.75rem 0;
        max-width: 540px;
        font-size: 0.9rem;
        line-height: 1.6;
        color: var(--text-2);
        font-weight: 400;
    }
    .hero-note .icon {
        color: var(--amber);
        font-size: 1rem;
        flex-shrink: 0;
    }
    .hero-note b {
        color: var(--amber);
        font-weight: 600;
    }

    /* Chips */
    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    .chip {
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.4rem 0.85rem;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 100px;
        font-size: 0.82rem;
        color: var(--text-2);
        white-space: nowrap;
    }
    .chip::before {
        content: '';
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background: var(--violet);
    }
    .chip strong {
        font-weight: 600;
        color: var(--text);
    }

    /* ═══ MARCO DEL RETRATO (Aumentado) ═══ */
    .st-key-portrait_card {
        background: var(--surface) !important;
        border: 1px solid var(--border-2) !important;
        padding: 1rem !important; /* Padding reducido para dar más espacio a la imagen */
        position: relative;
        width: 100%;             /* Ocupa todo el ancho disponible de la columna */
        min-height: 600px;       /* Asegura que el marco sea alto */
        margin: 0 auto;
        border-radius: 20px !important;
        box-shadow: 0 24px 60px rgba(168, 85, 247, 0.20),
                    0 0 80px rgba(168, 85, 247, 0.08) !important;
        display: flex !important;
        flex-direction: column;
        justify-content: center; 
        align-items: center;     
    }
    .st-key-portrait_card::before {
        content: '';
        position: absolute;
        inset: -1px;
        border-radius: 21px;
        padding: 1px;
        background: linear-gradient(135deg,
            rgba(192, 132, 252, 0.6),
            transparent 40%,
            transparent 60%,
            rgba(251, 191, 36, 0.4));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        pointer-events: none;
    }
    .st-key-portrait_card [data-testid="stImage"] {
        border-radius: 12px !important;
        overflow: hidden;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .st-key-portrait_card img {
        border-radius: 12px !important;
        display: block;
        width: 100%;
        height: auto;
        max-height: none;        /* Eliminado el límite de 400px para que crezca */
        object-fit: contain;      
    }

    .portrait-caption {
        text-align: center;
        margin-top: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        color: var(--muted);
    }
    .portrait-caption .star {
        color: var(--violet);
        margin: 0 0.6rem;
    }

    /* ═══ SECCIONES ═══ */
    .section-head {
        display: flex;
        align-items: center;
        gap: 1.15rem;
        padding-bottom: 1.25rem;
        margin: 4rem 0 2.25rem 0;
        border-bottom: 1px solid var(--border);
    }
    .section-head:first-of-type { margin-top: 4rem; }
    .section-num {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 42px;
        height: 32px;
        padding: 0 0.55rem;
        background: var(--violet-soft);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        font-weight: 600;
        color: var(--violet);
        letter-spacing: 0.05em;
        flex-shrink: 0;
    }
    .section-title {
        font-family: 'Instrument Serif', serif !important;
        font-size: 1.65rem !important;
        font-weight: 400 !important;
        letter-spacing: -0.005em !important;
        margin: 0 !important;
        color: var(--text) !important;
        flex: 1;
    }
    .section-count {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--muted-2);
        font-weight: 500;
    }

    /* ═══ TARJETAS DE APP ═══ */
    .app-card {
        display: block !important;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        text-decoration: none !important;
        color: var(--text) !important;
        transition: all 0.3s ease;
        height: 100%;
        margin-bottom: 0.5rem;
        overflow: hidden;
        position: relative;
    }
    .app-card:hover {
        border-color: var(--violet);
        text-decoration: none !important;
        color: var(--text) !important;
        transform: translateY(-4px);
        box-shadow: 0 20px 48px rgba(168, 85, 247, 0.18),
                    0 0 0 1px rgba(192, 132, 252, 0.2);
        background: var(--surface-hover);
    }

    /* Espacio blanco para la imagen de la página */
    .app-thumb {
        width: 100%;
        aspect-ratio: 16 / 10;
        background: #ffffff;
        border-bottom: 1px solid var(--border);
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .app-thumb::after {
        content: '◇';
        font-family: 'Instrument Serif', serif;
        font-size: 1.5rem;
        color: #e5e0ec;
        opacity: 0.8;
        transition: all 0.3s ease;
    }
    .app-card:hover .app-thumb::after {
        color: var(--violet);
        opacity: 1;
        transform: scale(1.15) rotate(15deg);
    }

    /* Contenido de la tarjeta */
    .app-body {
        padding: 1.35rem 1.4rem 1.5rem 1.4rem;
    }
    .app-kicker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.63rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--violet);
        font-weight: 500;
        margin-bottom: 0.7rem;
        display: block;
    }
    .app-title {
        font-family: 'Instrument Serif', serif !important;
        font-size: 1.28rem !important;
        font-weight: 400 !important;
        line-height: 1.3 !important;
        margin: 0 0 0.65rem 0 !important;
        color: var(--text) !important;
        letter-spacing: -0.005em !important;
    }
    .app-desc {
        font-size: 0.87rem;
        line-height: 1.65;
        color: var(--muted);
        margin: 0 0 1.25rem 0;
        font-weight: 400;
    }
    .app-link {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--text-2);
        font-weight: 500;
        transition: gap 0.2s ease, color 0.2s ease;
    }
    .app-card:hover .app-link {
        gap: 0.9rem;
        color: var(--violet);
    }

    /* ═══ FOOTER ═══ */
    .footer {
        text-align: center;
        padding: 3.5rem 0 1rem 0;
        margin-top: 5rem;
        border-top: 1px solid var(--border);
        position: relative;
    }
    .footer-ornament {
        font-family: 'Instrument Serif', serif;
        font-size: 1.5rem;
        color: var(--violet);
        margin-bottom: 1rem;
        display: block;
        letter-spacing: 1rem;
    }
    .footer-text {
        font-family: 'Instrument Serif', serif;
        font-size: 1.15rem;
        font-style: italic;
        color: var(--text);
        margin: 0 0 0.5rem 0;
        font-weight: 400;
    }
    .footer-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--muted);
        margin: 0;
    }

    .stMarkdown a { text-decoration: none !important; }

    /* ═══ SCROLLBAR ═══ */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb {
        background: var(--border-2);
        border: 2px solid var(--bg);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--violet); }

    /* ═══ RESPONSIVE ═══ */
    @media (max-width: 900px) {
        .hero-h1 { font-size: 2.4rem !important; }
        .section-title { font-size: 1.3rem !important; }
        .section-count { display: none; }
        .app-title { font-size: 1.1rem !important; }
        .block-container { padding-top: 1.75rem !important; }
        .st-key-portrait_card { min-height: 450px; }
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════
def section_header(num, title, count):
    st.markdown(f"""
        <div class="section-head">
            <span class="section-num">{num}</span>
            <h2 class="section-title">{title}</h2>
            <span class="section-count">{count}</span>
        </div>
    """, unsafe_allow_html=True)


def app_card(kicker, title, desc, url):
    return f"""
        <a href="{url}" target="_blank" class="app-card">
            <div class="app-thumb"></div>
            <div class="app-body">
                <span class="app-kicker">{kicker}</span>
                <h3 class="app-title">{title}</h3>
                <p class="app-desc">{desc}</p>
                <span class="app-link">Abrir aplicación →</span>
            </div>
        </a>
    """


# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
col_left, col_right = st.columns([1, 1.5], gap="large", vertical_alignment="center")

with col_left:
    with st.container(key="portrait_card"):
        try:
            # Nota: al aumentar el ancho del contenedor, la imagen crecerá proporcionalmente
            st.image('yo.png', use_container_width=True)
        except Exception:
            st.markdown(
                '<div style="aspect-ratio:1; display:flex; align-items:center; justify-content:center; font-size:6rem;">👋</div>',
                unsafe_allow_html=True,
            )
    st.markdown(
        '<div class="portrait-caption">Juan Pablo<span class="star">✦</span>Parte 2 · 2026</div>',
        unsafe_allow_html=True,
    )

with col_right:
    st.markdown("""
        <div class="part-badge">
            <span class="num">2</span>
            <span>Segunda parte · Portafolio 2026</span>
        </div>
        <div class="hero-kicker">Interfaces Multimodales</div>
        <h1 class="hero-h1">Hola, soy<br><em>Juan Pablo</em></h1>
        <p class="hero-desc">
            Tengo <strong>20 años</strong> y estudio <strong>Diseño Interactivo</strong>
            en <strong>EAFIT</strong>. Esta es la <strong>segunda parte</strong> de mi
            portafolio para la materia de <strong>Interfaces Multimodales</strong>, donde
            reunimos los proyectos más recientes del semestre: desde modelos de lenguaje
            hasta integraciones con hardware y visión por computadora.
        </p>
        <div class="hero-note">
            <span class="icon">✦</span>
            <span>Esta es la <b>segunda parte</b> del portafolio. Reúne las actividades más recientes del curso, incluyendo las integraciones con hardware y los tableros interactivos.</span>
        </div>
        <div class="chips">
            <span class="chip"><strong>EAFIT</strong> Diseño Interactivo</span>
            <span class="chip"><strong>20 años</strong> Medellín</span>
            <span class="chip"><strong>2026</strong> Interfaces Multimodales</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 01 · APLICACIONES CON LLMs
# ═══════════════════════════════════════════════════════════════
section_header("01", "Aplicaciones con LLMs", "2 aplicaciones")

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown(app_card(
        "NLP · Procesamiento",
        "Procesamiento de Lenguaje",
        "Explora cómo la IA comprende, analiza y genera lenguaje natural en español.",
        "https://procesamientolenguajejplg-dpcdtmrteadz4zxvzn8adh.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "Computer Vision",
        "Visión artificial",
        "Modelos de visión por computadora que reconocen imágenes, objetos y patrones.",
        "https://visionapp-8whsafj8pj5hdiuow4yjyb.streamlit.app/"
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 02 · INTERACCIÓN CON INTERFACES TÁCTILES
# ═══════════════════════════════════════════════════════════════
section_header("02", "Interacción con interfaces táctiles", "4 aplicaciones")

# Fila 1
c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown(app_card(
        "Visión + GPT",
        "Tablero inteligente",
        "Dibuja un boceto y deja que la IA lo interprete, lo describa o lo resuelva.",
        "https://tablerotuneado-dqjtotfrqskiyeosh6youa.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "Matemáticas · GPT",
        "Tablero de matemáticas",
        "Dibuja una operación o ecuación y la IA la resuelve paso a paso con LaTeX.",
        "https://tablerotuneado-ez8ftd2kuoia7yoh7cpdhe.streamlit.app/"
    ), unsafe_allow_html=True)

# Fila 2
c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown(app_card(
        "OCR · Números",
        "Tablero que lee números",
        "Escribe un número a mano y la IA lo reconoce e interpreta al instante.",
        "https://tactilnumeros-kdpcwepxhzeer6zvu3cq6x.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "Canvas · Personalizable",
        "Tablero para dibujar",
        "Un lienzo libre con herramientas y colores personalizables para crear.",
        "https://tableropersonalizado-nkqwmc7lntrdxrnqmo7nl6.streamlit.app/"
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 03 · SISTEMAS CON INTERNET DE LAS COSAS
# ═══════════════════════════════════════════════════════════════
section_header("03", "Sistemas con internet de las cosas", "3 aplicaciones")

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown(app_card(
        "Voz · Control",
        "Control de voz",
        "Interactúa con la aplicación usando únicamente tu voz, sin tocar el teclado.",
        "https://ctrlvoice-4zw5fqi5pmuizke4vdecw7.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "Sensor · MQTT",
        "Wokwi a Streamlit",
        "Un sensor simulado en Wokwi envía datos a Streamlit a través de MQTT.",
        "https://lectormqtt-t59niwifyecackdckk82fx.streamlit.app/"
    ), unsafe_allow_html=True)
with c3:
    st.markdown(app_card(
        "Control · MQTT",
        "Streamlit a Wokwi",
        "Controla dispositivos simulados en Wokwi desde una interfaz en Streamlit.",
        "https://appawokwicmqtt-spyylhsrmng4sdf5fncrty.streamlit.app/"
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
    <div class="footer">
        <span class="footer-ornament">✦ ✦ ✦</span>
        <p class="footer-text">Hecho con curiosidad desde Medellín</p>
        <p class="footer-sub">Juan Pablo · EAFIT · Interfaces Multimodales · Parte 2 · 2026</p>
    </div>
""", unsafe_allow_html=True)
