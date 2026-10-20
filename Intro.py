import streamlit as st
from PIL import Image
import base64
import io

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Portafolio · Juan Pablo",
    page_icon="⛩",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# ESTILOS — ZEN / JAPONÉS MINIMALISTA
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --washi:        #faf6f0;
        --washi-2:      #f2ebe0;
        --paper:        #ffffff;
        --ink:          #1a1815;
        --ink-2:        #3a3833;
        --muted:        #8a8378;
        --muted-2:      #b8b0a3;
        --line:         #e8e0d0;
        --line-2:       #d9d0bd;
        --vermillion:   #c73e1d;
        --vermillion-2: #a83018;
        --vermillion-soft: #fbe9e4;
        --sage:         #7a8b6f;
    }

    html, body, [class*="css"], .stApp, button, input, textarea, select {
        font-family: 'Inter', sans-serif !important;
        color: var(--ink);
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Shippori Mincho', serif !important;
        font-weight: 500 !important;
        color: var(--ink) !important;
        letter-spacing: -0.01em !important;
    }

    /* ═══ FONDO WASHI ═══ */
    .stApp {
        background-color: var(--washi) !important;
        background-image:
            radial-gradient(circle at 15% 5%, rgba(199, 62, 29, 0.05), transparent 42%),
            radial-gradient(circle at 85% 95%, rgba(122, 139, 111, 0.06), transparent 42%);
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
        color: var(--vermillion);
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    .hero-kicker::before {
        content: '';
        display: inline-block;
        width: 34px;
        height: 1px;
        background: var(--vermillion);
    }
    .hero h1 {
        font-family: 'Shippori Mincho', serif !important;
        font-size: 3.5rem !important;
        line-height: 1.08 !important;
        letter-spacing: -0.015em !important;
        font-weight: 500 !important;
        margin: 0 0 1.5rem 0 !important;
        color: var(--ink) !important;
    }
    .hero h1 em {
        font-style: italic;
        color: var(--vermillion);
        font-weight: 400;
    }
    .hero-desc {
        font-size: 1.02rem;
        line-height: 1.75;
        color: var(--ink-2);
        margin: 0 0 1.75rem 0;
        max-width: 560px;
        font-weight: 300;
    }
    .hero-desc strong {
        color: var(--ink);
        font-weight: 600;
    }

    /* Hanko stamp (sello rojo) */
    .hanko {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        background: var(--vermillion);
        color: #ffffff !important;
        font-family: 'Shippori Mincho', serif;
        font-size: 1.35rem;
        font-weight: 700;
        border-radius: 3px;
        box-shadow: inset 0 0 0 2px rgba(255,255,255,0.18);
        margin-bottom: 1.5rem;
    }

    /* Aviso primera parte */
    .hero-note {
        display: inline-flex;
        align-items: flex-start;
        gap: 0.85rem;
        padding: 0.9rem 0 0.9rem 1.1rem;
        border-left: 2px solid var(--vermillion);
        margin: 0 0 1.75rem 0;
        max-width: 540px;
        font-size: 0.9rem;
        line-height: 1.6;
        color: var(--ink-2);
        font-weight: 400;
    }
    .hero-note b {
        color: var(--vermillion);
        font-weight: 600;
    }

    /* Chips minimal */
    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem 1.25rem;
    }
    .chip {
        display: inline-flex;
        align-items: baseline;
        gap: 0.5rem;
        font-size: 0.85rem;
        color: var(--ink-2);
        padding: 0.15rem 0;
    }
    .chip::before {
        content: '·';
        color: var(--vermillion);
        font-weight: 700;
        font-size: 1.2rem;
        line-height: 1;
    }
    .chip strong {
        font-weight: 600;
        color: var(--ink);
    }

    /* ═══ MARCO DEL RETRATO (kakemono) ═══ */
    .st-key-portrait_card {
        background: var(--paper) !important;
        border: 1px solid var(--ink) !important;
        padding: 1.1rem !important;
        position: relative;
        max-width: 380px;
        margin: 0 auto;
        box-shadow: 6px 6px 0 rgba(199, 62, 29, 0.15) !important;
    }
    .st-key-portrait_card::before {
        content: '';
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        width: 1px;
        height: 12px;
        background: var(--ink);
    }
    .st-key-portrait_card::after {
        content: '';
        position: absolute;
        top: -18px;
        left: 50%;
        transform: translateX(-50%);
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--vermillion);
    }
    .st-key-portrait_card [data-testid="stImage"] {
        border-radius: 0 !important;
    }
    .st-key-portrait_card img {
        border-radius: 0 !important;
        display: block;
        width: 100%;
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
    .portrait-caption .stamp {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        background: var(--vermillion);
        color: #ffffff;
        font-family: 'Shippori Mincho', serif;
        font-weight: 700;
        font-size: 0.78rem;
        border-radius: 2px;
        margin: 0 0.7rem;
        vertical-align: middle;
    }

    /* ═══ SECCIONES ═══ */
    .section-head {
        display: grid;
        grid-template-columns: auto auto 1fr auto;
        align-items: baseline;
        gap: 1.25rem;
        padding-bottom: 1.25rem;
        margin: 4rem 0 2.25rem 0;
        border-bottom: 1px solid var(--line-2);
    }
    .section-head:first-of-type { margin-top: 4rem; }
    .section-kanji {
        font-family: 'Shippori Mincho', serif;
        font-size: 2rem;
        font-weight: 500;
        color: var(--vermillion);
        line-height: 1;
    }
    .section-num {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 500;
        color: var(--muted);
        letter-spacing: 0.2em;
        padding-bottom: 0.2rem;
    }
    .section-title {
        font-family: 'Shippori Mincho', serif !important;
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.02em !important;
        margin: 0 !important;
        color: var(--ink) !important;
    }
    .section-en {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--muted-2);
        font-weight: 500;
        padding-bottom: 0.2rem;
    }

    /* ═══ TARJETAS DE APP ═══ */
    .app-card {
        display: block !important;
        background: var(--paper);
        border: 1px solid var(--line-2);
        padding: 1.75rem 1.65rem 1.6rem 1.65rem;
        text-decoration: none !important;
        color: var(--ink) !important;
        transition: all 0.35s ease;
        height: 100%;
        margin-bottom: 0.5rem;
        position: relative;
        overflow: hidden;
    }
    .app-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--vermillion);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.35s ease;
    }
    .app-card:hover {
        border-color: var(--ink);
        text-decoration: none !important;
        color: var(--ink) !important;
        box-shadow: 8px 8px 0 rgba(199, 62, 29, 0.10);
        transform: translate(-2px, -2px);
    }
    .app-card:hover::before {
        transform: scaleX(1);
    }

    /* Glifo circular con kanji */
    .app-glyph {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 62px;
        height: 62px;
        border: 1px solid var(--ink);
        border-radius: 50%;
        margin-bottom: 1.5rem;
        font-family: 'Shippori Mincho', serif;
        font-size: 1.65rem;
        font-weight: 500;
        color: var(--ink);
        background: transparent;
        transition: all 0.35s ease;
    }
    .app-card:hover .app-glyph {
        background: var(--vermillion);
        color: #ffffff;
        border-color: var(--vermillion);
        transform: rotate(-8deg);
    }

    .app-kicker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.63rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--vermillion);
        font-weight: 500;
        margin-bottom: 0.7rem;
    }
    .app-title {
        font-family: 'Shippori Mincho', serif !important;
        font-size: 1.28rem !important;
        font-weight: 500 !important;
        line-height: 1.3 !important;
        margin: 0 0 0.65rem 0 !important;
        color: var(--ink) !important;
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
        color: var(--ink);
        font-weight: 500;
        transition: gap 0.2s ease, color 0.2s ease;
    }
    .app-card:hover .app-link {
        gap: 0.9rem;
        color: var(--vermillion);
    }

    /* ═══ FOOTER ═══ */
    .footer {
        text-align: center;
        padding: 3.5rem 0 1rem 0;
        margin-top: 5rem;
        border-top: 1px solid var(--line-2);
        position: relative;
    }
    .footer-enso {
        display: inline-block;
        width: 44px;
        height: 44px;
        border: 2px solid var(--vermillion);
        border-radius: 50%;
        border-right-color: transparent;
        border-bottom-color: transparent;
        transform: rotate(45deg);
        margin-bottom: 1.25rem;
    }
    .footer-text {
        font-family: 'Shippori Mincho', serif;
        font-size: 1.1rem;
        font-style: italic;
        color: var(--ink);
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
    ::-webkit-scrollbar-track { background: var(--washi); }
    ::-webkit-scrollbar-thumb {
        background: var(--line-2);
        border: 2px solid var(--washi);
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--vermillion); }

    /* ═══ RESPONSIVE ═══ */
    @media (max-width: 900px) {
        .hero h1 { font-size: 2.4rem !important; }
        .section-title { font-size: 1.25rem !important; }
        .section-head { grid-template-columns: auto auto 1fr; gap: 0.85rem; }
        .section-en { display: none; }
        .app-title { font-size: 1.1rem !important; }
        .block-container { padding-top: 1.75rem !important; }
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════
def section_header(kanji, num, title, title_en):
    st.markdown(f"""
        <div class="section-head">
            <div class="section-kanji">{kanji}</div>
            <div class="section-num">{num}</div>
            <h2 class="section-title">{title}</h2>
            <span class="section-en">{title_en}</span>
        </div>
    """, unsafe_allow_html=True)


def app_card(glyph, kicker, title, desc, url):
    return f"""
        <a href="{url}" target="_blank" class="app-card">
            <div class="app-glyph">{glyph}</div>
            <div class="app-kicker">{kicker}</div>
            <h3 class="app-title">{title}</h3>
            <p class="app-desc">{desc}</p>
            <span class="app-link">Abrir aplicación →</span>
        </a>
    """


# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
col_left, col_right = st.columns([1, 1.5], gap="large", vertical_alignment="center")

with col_left:
    with st.container(key="portrait_card"):
        try:
            st.image('yo.png', use_container_width=True)
        except Exception:
            st.markdown(
                '<div style="aspect-ratio:1; display:flex; align-items:center; justify-content:center; font-size:6rem;">👋</div>',
                unsafe_allow_html=True,
            )
    st.markdown(
        '<div class="portrait-caption">Juan Pablo<span class="stamp">誠</span>2026</div>',
        unsafe_allow_html=True,
    )

with col_right:
    st.markdown("""
        <div class="hanko">誠</div>
        <div class="hero-kicker">Portafolio · Primera parte · 2026</div>
        <h1 class="hero-h1">Hola, soy<br><em>Juan Pablo</em></h1>
        <p class="hero-desc">
            Tengo <strong>20 años</strong> y estudio <strong>Diseño Interactivo</strong>
            en <strong>EAFIT</strong>. Este es el primer capítulo de mi portafolio para
            la materia de <strong>Interfaces Multimodales</strong>, donde exploramos cómo
            la inteligencia artificial puede extender nuestros sentidos y crear nuevas
            formas de interacción.
        </p>
        <div class="hero-note">
            <span>🚧 Esta es la <b>primera parte</b> del portafolio. Aún quedan más clases, actividades y proyectos por venir durante el semestre.</span>
        </div>
        <div class="chips">
            <span class="chip"><strong>EAFIT</strong> Diseño Interactivo</span>
            <span class="chip"><strong>20 años</strong> Medellín</span>
            <span class="chip"><strong>2026</strong> Interfaces Multimodales</span>
        </div>
    """, unsafe_allow_html=True)

# Fix h1 font (needed since we use custom class for h1)
st.markdown("""
<style>
    .hero-h1 {
        font-family: 'Shippori Mincho', serif !important;
        font-size: 3.5rem !important;
        line-height: 1.08 !important;
        letter-spacing: -0.015em !important;
        font-weight: 500 !important;
        margin: 0 0 1.5rem 0 !important;
        color: #1a1815 !important;
    }
    .hero-h1 em {
        font-style: italic;
        color: #c73e1d;
        font-weight: 400;
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 01 · LENGUAJE E IA
# ═══════════════════════════════════════════════════════════════
section_header("言", "01", "Lenguaje e inteligencia", "Language & AI")

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown(app_card(
        "文",
        "NLP · Procesamiento",
        "Procesamiento de Lenguaje",
        "Explora cómo la IA comprende, analiza y genera lenguaje natural en español.",
        "https://procesamientolenguajejplg-dpcdtmrteadz4zxvzn8adh.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "智",
        "Visión + GPT",
        "Tablero inteligente",
        "Dibuja un boceto y deja que la IA lo interprete, lo describa o lo resuelva.",
        "https://tablerotuneado-dqjtotfrqskiyeosh6youa.streamlit.app/"
    ), unsafe_allow_html=True)
with c3:
    st.markdown(app_card(
        "算",
        "Matemáticas · GPT",
        "Tablero de matemáticas",
        "Dibuja una operación o ecuación y la IA la resuelve paso a paso con LaTeX.",
        "https://tablerotuneado-ez8ftd2kuoia7yoh7cpdhe.streamlit.app/"
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 02 · VISIÓN Y TRAZO
# ═══════════════════════════════════════════════════════════════
section_header("視", "02", "Visión y trazo", "Vision & drawing")

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown(app_card(
        "眼",
        "Computer Vision",
        "Visión artificial",
        "Modelos de visión por computadora que reconocen imágenes, objetos y patrones.",
        "https://visionapp-8whsafj8pj5hdiuow4yjyb.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "数",
        "OCR · Números",
        "Tablero que lee números",
        "Escribe un número a mano y la IA lo reconoce e interpreta al instante.",
        "https://tactilnumeros-kdpcwepxhzeer6zvu3cq6x.streamlit.app/"
    ), unsafe_allow_html=True)
with c3:
    st.markdown(app_card(
        "描",
        "Canvas · Personalizable",
        "Tablero para dibujar",
        "Un lienzo libre con herramientas y colores personalizables para crear.",
        "https://tableropersonalizado-nkqwmc7lntrdxrnqmo7nl6.streamlit.app/"
    ), unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN 03 · VOZ E IoT
# ═══════════════════════════════════════════════════════════════
section_header("声", "03", "Voz y hardware", "Voice & IoT")

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown(app_card(
        "声",
        "Voz · Control",
        "Control de voz",
        "Interactúa con la aplicación usando únicamente tu voz, sin tocar el teclado.",
        "https://ctrlvoice-4zw5fqi5pmuizke4vdecw7.streamlit.app/"
    ), unsafe_allow_html=True)
with c2:
    st.markdown(app_card(
        "光",
        "Sensor · MQTT",
        "Wokwi a Streamlit",
        "Un sensor simulado en Wokwi envía datos a Streamlit a través de MQTT.",
        "https://lectormqtt-t59niwifyecackdckk82fx.streamlit.app/"
    ), unsafe_allow_html=True)
with c3:
    st.markdown(app_card(
        "操",
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
        <div class="footer-enso"></div>
        <p class="footer-text">Hecho con curiosidad desde Medellín</p>
        <p class="footer-sub">Juan Pablo · EAFIT · Interfaces Multimodales · 2026</p>
    </div>
""", unsafe_allow_html=True)
