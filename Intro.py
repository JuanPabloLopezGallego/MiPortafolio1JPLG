import streamlit as st
import base64
import os
import streamlit.components.v1 as components

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE PÁGINA
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Portafolio · Juan Pablo · Parte 2",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════
def get_image_base64(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
                ext = path.split(".")[-1].lower()
                mime = "image/png" if ext == "png" else "image/jpeg"
                return f"data:{mime};base64,{data}"
        except Exception:
            return ""
    return ""


def render_thumb(image_path, title):
    b64 = get_image_base64(image_path)
    if b64:
        return f'<img src="{b64}" alt="{title}" draggable="false" loading="lazy" />'
    return '<div class="app-thumb-placeholder">◇</div>'


def render_card(kicker, title, desc, url, image_path):
    thumb_html = render_thumb(image_path, title)
    return f"""
    <a href="{url}" target="_blank" rel="noopener noreferrer" class="app-card" draggable="false">
        <div class="card-glow"></div>
        <div class="app-thumb">
            {thumb_html}
            <div class="app-thumb-overlay">
                <span class="thumb-badge">streamlit.app ↗</span>
            </div>
        </div>
        <div class="app-body">
            <span class="app-kicker">{kicker}</span>
            <h3 class="app-title">{title}</h3>
            <p class="app-desc">{desc}</p>
            <span class="app-link">
                Abrir aplicación <span class="app-link-arrow">→</span>
            </span>
        </div>
    </a>
    """


def render_grid(cards):
    return f'<div class="cards-grid">{"".join(cards)}</div>'


def render_carousel(carousel_id, cards_html):
    cards_joined = "\n".join([f'<div class="carousel-slide">{c}</div>' for c in cards_html])
    dots_joined = "\n".join([
        f'<button class="carousel-dot {"is-active" if i == 0 else ""}" '
        f'data-index="{i}" aria-label="Slide {i+1}"></button>'
        for i in range(len(cards_html))
    ])
    total = len(cards_html)
    return f"""
    <div class="carousel-wrap" id="{carousel_id}">
        <div class="carousel-track">
            {cards_joined}
            <div class="carousel-spacer"></div>
        </div>
        <button class="carousel-arrow carousel-arrow-left" aria-label="Anterior">‹</button>
        <button class="carousel-arrow carousel-arrow-right" aria-label="Siguiente">›</button>
        <div class="carousel-nav">
            <div class="carousel-dots">{dots_joined}</div>
            <span class="carousel-counter" id="{carousel_id}-counter">01 / {total:02d}</span>
        </div>
    </div>
    """


# ═══════════════════════════════════════════════════════════════
# DATOS DE LOS PROYECTOS
# ═══════════════════════════════════════════════════════════════
sec1_cards = [
    render_card(
        "NLP · Procesamiento",
        "Procesamiento de Lenguaje",
        "Explora cómo la IA comprende, analiza y genera lenguaje natural en español.",
        "https://procesamientolenguajejplg-dpcdtmrteadz4zxvzn8adh.streamlit.app/",
        "LLM1.PNG",
    ),
    render_card(
        "Computer Vision",
        "Visión artificial",
        "Modelos de visión por computadora que reconocen imágenes, objetos y patrones.",
        "https://visionapp-8whsafj8pj5hdiuow4yjyb.streamlit.app/",
        "LLM2.PNG",
    ),
]

sec2_cards = [
    render_card(
        "Visión + GPT",
        "Tablero inteligente",
        "Dibuja un boceto y deja que la IA lo interprete, lo describa o lo resuelva.",
        "https://tablerotuneado-dqjtotfrqskiyeosh6youa.streamlit.app/",
        "Tablero3.PNG",
    ),
    render_card(
        "Matemáticas · GPT",
        "Tablero de matemáticas",
        "Dibuja una operación o ecuación y la IA la resuelve paso a paso con LaTeX.",
        "https://tablerotuneado-ez8ftd2kuoia7yoh7cpdhe.streamlit.app/",
        "Tablero4.PNG",
    ),
    render_card(
        "OCR · Números",
        "Tablero que lee números",
        "Escribe un número a mano y la IA lo reconoce e interpreta al instante.",
        "https://tactilnumeros-kdpcwepxhzeer6zvu3cq6x.streamlit.app/",
        "Tablero1.PNG",
    ),
    render_card(
        "Canvas · Personalizable",
        "Tablero para dibujar",
        "Un lienzo libre con herramientas y colores personalizables para crear.",
        "https://tableropersonalizado-nkqwmc7lntrdxrnqmo7nl6.streamlit.app/",
        "Tablero2.PNG",
    ),
]

sec3_cards = [
    render_card(
        "Voz · Control",
        "Control de voz",
        "Interactúa con la aplicación usando únicamente tu voz, sin tocar el teclado.",
        "https://ctrlvoice-4zw5fqi5pmuizke4vdecw7.streamlit.app/",
        "IOT3.PNG",
    ),
    render_card(
        "Sensor · MQTT",
        "Wokwi a Streamlit",
        "Un sensor simulado en Wokwi envía datos a Streamlit a través de MQTT.",
        "https://lectormqtt-t59niwifyecackdckk82fx.streamlit.app/",
        "IOT1.PNG",
    ),
    render_card(
        "Control · MQTT",
        "Streamlit a Wokwi",
        "Controla dispositivos simulados en Wokwi desde una interfaz en Streamlit.",
        "https://appawokwicmqtt-spyylhsrmng4sdf5fncrty.streamlit.app/",
        "IOT2.PNG",
    ),
]

portrait_b64 = get_image_base64("yo.png")
portrait_html = (
    f'<img src="{portrait_b64}" alt="Juan Pablo" draggable="false" />'
    if portrait_b64
    else '<div class="portrait-placeholder">JP</div>'
)

# ═══════════════════════════════════════════════════════════════
# HTML + CSS
# ═══════════════════════════════════════════════════════════════
html_content = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {{
        --bg: #070512;
        --surface: #140c28;
        --surface-hover: #1d1238;
        --border: #2d1f4a;
        --border-2: #4a3770;
        --text: #f3ecff;
        --text-2: #cbbfe6;
        --muted: #9a8bb5;
        --muted-2: #6b5a8a;
        --violet: #c084fc;
        --violet-2: #a855f7;
        --pink: #f472b6;
        --amber: #fbbf24;
    }}

    html, body {{
        font-family: 'Inter', sans-serif !important;
        background-color: var(--bg) !important;
        color: var(--text) !important;
        overflow-x: hidden !important;
    }}

    /* ═══════ CRÍTICO: contenedores de Streamlit transparentes ═══════ */
    .stApp,
    .stApp > div,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    .main,
    .block-container,
    .stMarkdown,
    [data-testid="stMarkdownContainer"],
    [data-testid="stVerticalBlock"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    #MainMenu, footer, header[data-testid="stHeader"] {{
        display: none !important;
        visibility: hidden !important;
    }}

    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}

    /* ═══════ WRAPPER DE FONDOS (se mueve al body vía JS) ═══════ */
    #cosmos-bg {{
        position: fixed;
        inset: 0;
        z-index: -1;
        pointer-events: none;
        overflow: hidden;
    }}

    /* ═══════ FONDO BASE ═══════ */
    .bg-cosmos {{
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse at 15% -10%, rgba(168, 85, 247, 0.22), transparent 50%),
            radial-gradient(ellipse at 85% 110%, rgba(192, 132, 252, 0.14), transparent 50%),
            radial-gradient(circle at 60% 35%, rgba(251, 191, 36, 0.05), transparent 40%),
            radial-gradient(circle at 20% 75%, rgba(52, 211, 153, 0.05), transparent 40%),
            radial-gradient(circle at 80% 60%, rgba(244, 114, 182, 0.06), transparent 40%),
            #070512;
    }}

    /* ═══════ MOUSE GLOW ═══════ */
    .mouse-glow {{
        position: absolute;
        top: 0; left: 0;
        width: 520px; height: 520px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(192, 132, 252, 0.18), rgba(192,132,252,0.06) 40%, transparent 65%);
        pointer-events: none;
        transform: translate3d(calc(var(--mx, 50vw) - 260px), calc(var(--my, 50vh) - 260px), 0);
        transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1);
        filter: blur(20px);
        will-change: transform;
    }}

    /* ═══════ ORBES CON PARALLAX ═══════ */
    .orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(90px);
        pointer-events: none;
        opacity: 0.65;
        will-change: translate, transform;
    }}
    .orb-1 {{
        width: 520px; height: 520px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.45), transparent 70%);
        top: -120px; left: -120px;
        animation: floatOrb 20s ease-in-out infinite;
        translate: var(--px, 0) var(--py, 0);
        transition: translate 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .orb-2 {{
        width: 620px; height: 620px;
        background: radial-gradient(circle, rgba(244, 114, 182, 0.3), transparent 70%);
        bottom: -180px; right: -120px;
        animation: floatOrb 26s ease-in-out infinite reverse;
        translate: var(--px, 0) var(--py, 0);
        transition: translate 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    @keyframes floatOrb {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        50% {{ transform: translate(40px, -30px) scale(1.08); }}
    }}

    /* ═══════ AURORA ═══════ */
    .aurora {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        opacity: 0.55;
    }}
    .aurora-blob {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        will-change: transform;
    }}
    .aurora-1 {{
        width: 45vw; height: 45vw;
        background: radial-gradient(circle, rgba(192, 132, 252, 0.6), transparent 70%);
        top: -15%; left: 5%;
        animation: aurora1 24s ease-in-out infinite;
    }}
    .aurora-2 {{
        width: 40vw; height: 40vw;
        background: radial-gradient(circle, rgba(244, 114, 182, 0.55), transparent 70%);
        top: 35%; right: 0%;
        animation: aurora2 28s ease-in-out infinite;
    }}
    .aurora-3 {{
        width: 35vw; height: 35vw;
        background: radial-gradient(circle, rgba(251, 191, 36, 0.45), transparent 70%);
        bottom: -15%; left: 30%;
        animation: aurora3 22s ease-in-out infinite;
    }}
    @keyframes aurora1 {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        50% {{ transform: translate(15vw, 8vh) scale(1.15); }}
    }}
    @keyframes aurora2 {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        50% {{ transform: translate(-12vw, -5vh) scale(1.2); }}
    }}
    @keyframes aurora3 {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        50% {{ transform: translate(8vw, -10vh) scale(1.1); }}
    }}

    /* ═══════ ESTRELLAS ═══════ */
    .stars {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        background-repeat: repeat;
        background-image:
            radial-gradient(1.5px 1.5px at 20px 30px, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 40px 70px, rgba(192,132,252,0.7), transparent),
            radial-gradient(1px 1px at 90px 40px, rgba(255,255,255,0.6), transparent),
            radial-gradient(1.5px 1.5px at 160px 120px, rgba(244,114,182,0.7), transparent),
            radial-gradient(1px 1px at 250px 160px, rgba(192,132,252,0.5), transparent),
            radial-gradient(1.5px 1.5px at 350px 200px, rgba(255,255,255,0.5), transparent);
        background-size: 450px 250px;
        animation: starsMove 120s linear infinite, starsTwinkle 5s ease-in-out infinite;
        opacity: 0.7;
    }}
    .stars-2 {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        background-repeat: repeat;
        background-image:
            radial-gradient(1px 1px at 60px 40px, rgba(251,191,36,0.55), transparent),
            radial-gradient(1.2px 1.2px at 180px 90px, rgba(255,255,255,0.4), transparent),
            radial-gradient(1px 1px at 300px 150px, rgba(192,132,252,0.5), transparent);
        background-size: 340px 220px;
        animation: starsMove 75s linear infinite reverse, starsTwinkle 7s ease-in-out infinite 1s;
        opacity: 0.55;
    }}
    @keyframes starsMove {{
        from {{ transform: translateY(0); }}
        to {{ transform: translateY(-250px); }}
    }}
    @keyframes starsTwinkle {{
        0%, 100% {{ opacity: 0.7; }}
        50% {{ opacity: 0.3; }}
    }}

    /* ═══════ CANVAS DE PARTÍCULAS ═══════ */
    .particle-canvas {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        width: 100%;
        height: 100%;
        opacity: 0.9;
    }}

    /* ═══════ GRID OVERLAY ═══════ */
    .grid-overlay {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        background-image:
            linear-gradient(rgba(192, 132, 252, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(192, 132, 252, 0.05) 1px, transparent 1px);
        background-size: 90px 90px;
        mask-image: radial-gradient(ellipse at 50% 40%, black 15%, transparent 70%);
        -webkit-mask-image: radial-gradient(ellipse at 50% 40%, black 15%, transparent 70%);
    }}

    /* ═══════ ESTRELLAS FUGACES ═══════ */
    .shooting-star {{
        position: absolute;
        top: 15%; left: -120px;
        width: 120px; height: 2px;
        background: linear-gradient(90deg, transparent, var(--violet), transparent);
        border-radius: 100px;
        filter: blur(0.5px);
        pointer-events: none;
        opacity: 0;
        animation: shoot 12s linear infinite;
    }}
    .shooting-star.s2 {{ top: 55%; animation-delay: 4s; animation-duration: 16s; }}
    .shooting-star.s3 {{ top: 80%; animation-delay: 8s; animation-duration: 20s; background: linear-gradient(90deg, transparent, var(--amber), transparent); }}
    @keyframes shoot {{
        0%, 88% {{ opacity: 0; transform: translate(0, 0) rotate(18deg); }}
        90% {{ opacity: 1; }}
        100% {{ opacity: 0; transform: translate(115vw, 45vh) rotate(18deg); }}
    }}

    /* ═══════ SCROLL PROGRESS ═══════ */
    .scroll-progress {{
        position: fixed;
        top: 0; left: 0;
        height: 2px;
        z-index: 100;
        background: linear-gradient(90deg, var(--violet), var(--pink), var(--amber));
        box-shadow: 0 0 10px rgba(192, 132, 252, 0.6);
        width: 0%;
        transition: width 0.15s ease-out;
    }}

    /* ═══════ SIDE NAV ═══════ */
    .side-nav {{
        position: fixed;
        right: 2.25rem;
        top: 50%;
        transform: translateY(-50%);
        z-index: 40;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 1.2rem;
    }}
    .side-nav-dot-wrap {{
        display: flex;
        align-items: center;
        gap: 0.7rem;
        background: none;
        border: none;
        cursor: pointer;
        padding: 0.3rem 0;
        text-decoration: none !important;
    }}
    .side-nav-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: var(--muted);
        opacity: 0;
        transform: translateX(8px);
        transition: all 0.3s ease;
        white-space: nowrap;
    }}
    .side-nav-dot-wrap:hover .side-nav-label,
    .side-nav-dot-wrap.is-active .side-nav-label {{
        opacity: 1;
        transform: translateX(0);
        color: var(--text);
    }}
    .side-nav-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: rgba(154, 139, 181, 0.4);
        border: 1px solid rgba(154, 139, 181, 0.5);
        transition: all 0.35s ease;
    }}
    .side-nav-dot-wrap:hover .side-nav-dot {{
        background: rgba(192, 132, 252, 0.6);
        border-color: var(--violet);
    }}
    .side-nav-dot-wrap.is-active .side-nav-dot {{
        background: var(--violet);
        border-color: var(--violet);
        box-shadow: 0 0 12px rgba(192, 132, 252, 0.9);
        transform: scale(1.5);
    }}
    @media (max-width: 1024px) {{ .side-nav {{ display: none !important; }} }}

    /* ═══════ CONTENEDOR PRINCIPAL ═══════ */
    .experience-wrap {{
        position: relative;
        z-index: 1;
        max-width: 1240px;
        margin: 0 auto;
        padding: 3rem 2rem 5rem;
    }}

    /* ═══════ HERO ═══════ */
    .hero-grid {{
        display: grid;
        grid-template-columns: 1fr 1.2fr;
        gap: 3.5rem;
        align-items: center;
        min-height: 75vh;
    }}
    @media (max-width: 860px) {{
        .hero-grid {{ grid-template-columns: 1fr; gap: 2.5rem; }}
    }}

    .portrait-wrap {{
        position: relative;
        max-width: 460px;
        margin: 0 auto;
    }}
    .orbit-ring {{
        position: absolute;
        top: 50%; left: 50%;
        width: 116%; height: 116%;
        border: 1px dashed rgba(192, 132, 252, 0.3);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: spin 40s linear infinite;
        pointer-events: none;
    }}
    .orbit-ring::before, .orbit-ring::after {{
        content: '✦';
        position: absolute;
        font-size: 1rem;
    }}
    .orbit-ring::before {{ top: -8px; left: 50%; transform: translateX(-50%); color: var(--violet); }}
    .orbit-ring::after {{ bottom: -8px; left: 50%; transform: translateX(-50%); color: var(--amber); }}
    @keyframes spin {{ from {{ transform: translate(-50%, -50%) rotate(0deg); }} to {{ transform: translate(-50%, -50%) rotate(360deg); }} }}

    .portrait-frame {{
        position: relative;
        border-radius: 30px;
        padding: 12px;
        background: linear-gradient(135deg, rgba(192,132,252,0.8), rgba(168,85,247,0.3) 30%, transparent 50%, rgba(251,191,36,0.4) 80%, rgba(192,132,252,0.7));
        background-size: 300% 300%;
        animation: borderGlow 6s ease-in-out infinite, pulseGlow 3s ease-in-out infinite;
    }}
    @keyframes borderGlow {{ 0%, 100% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} }}
    @keyframes pulseGlow {{
        0%, 100% {{ box-shadow: 0 0 20px rgba(192,132,252,0.3), 0 0 40px rgba(168,85,247,0.15); }}
        50% {{ box-shadow: 0 0 30px rgba(192,132,252,0.5), 0 0 60px rgba(168,85,247,0.25); }}
    }}

    .portrait-inner {{
        background: #fff;
        border-radius: 22px;
        overflow: hidden;
        aspect-ratio: 4 / 5;
        position: relative;
    }}
    .portrait-inner img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}
    .portrait-placeholder {{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #1d1238, #0f0a1f);
        font-family: 'Fraunces', serif;
        font-size: 5rem;
        color: rgba(192, 132, 252, 0.4);
    }}

    .floating-chip {{
        position: absolute;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 1.1rem;
        background: rgba(20, 12, 40, 0.8);
        border: 1px solid rgba(192, 132, 252, 0.35);
        border-radius: 100px;
        font-size: 0.74rem;
        color: var(--text-2);
        white-space: nowrap;
        backdrop-filter: blur(14px);
        box-shadow: 0 10px 30px rgba(7, 5, 18, 0.5), 0 0 20px rgba(192, 132, 252, 0.1);
        animation: chipFloat 5s ease-in-out infinite;
        z-index: 5;
    }}
    .floating-chip strong {{ color: var(--text); font-weight: 600; }}
    .chip-1 {{ left: -4rem; top: 1rem; animation-delay: 0s; }}
    .chip-2 {{ right: -2.5rem; top: 35%; animation-delay: 1.2s; }}
    .chip-3 {{ left: -2rem; bottom: 1.5rem; animation-delay: 0.6s; }}
    @keyframes chipFloat {{
        0%, 100% {{ transform: translateY(0) rotate(-1deg); }}
        50% {{ transform: translateY(-12px) rotate(1deg); }}
    }}
    @media (max-width: 860px) {{ .floating-chip {{ display: none !important; }} }}

    .portrait-caption {{
        text-align: center;
        margin-top: 1.75rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        color: var(--muted);
    }}
    .portrait-caption .star {{ color: var(--violet); margin: 0 0.6rem; }}

    /* HERO TEXTOS */
    .part-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.4rem 1rem 0.4rem 0.5rem;
        background: rgba(192, 132, 252, 0.1);
        border: 1px solid rgba(192, 132, 252, 0.3);
        border-radius: 100px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--violet);
        font-weight: 600;
        margin-bottom: 1.5rem;
    }}
    .part-badge .num {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        background: linear-gradient(135deg, var(--violet), var(--violet-2));
        color: var(--bg);
        border-radius: 50%;
        font-size: 0.7rem;
        font-weight: 700;
    }}

    .hero-kicker {{
        display: inline-flex;
        align-items: center;
        gap: 0.85rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        color: var(--violet);
        font-weight: 500;
        margin-bottom: 1.4rem;
    }}
    .hero-kicker::before {{
        content: '';
        display: inline-block;
        width: 34px;
        height: 1px;
        background: var(--violet);
    }}

    .hero-h1 {{
        font-family: 'Fraunces', serif !important;
        font-size: clamp(3rem, 7vw, 5rem) !important;
        line-height: 0.98 !important;
        letter-spacing: -0.03em !important;
        font-weight: 500 !important;
        font-variation-settings: 'opsz' 144, 'SOFT' 30, 'WONK' 1;
        margin: 0 0 1.5rem 0 !important;
        color: var(--text) !important;
    }}
    .hero-h1 em {{
        font-style: italic;
        font-weight: 400 !important;
        background: linear-gradient(135deg, var(--violet), var(--pink), var(--amber));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }}

    .hero-desc {{
        font-size: 1.05rem;
        line-height: 1.8;
        color: var(--text-2);
        margin: 0 0 2rem 0;
        max-width: 580px;
        font-weight: 300;
    }}
    .hero-desc strong {{ color: var(--text); font-weight: 600; }}

    .hero-note {{
        display: flex;
        align-items: flex-start;
        gap: 0.85rem;
        padding: 1.1rem 1.3rem;
        background: linear-gradient(90deg, rgba(251, 191, 36, 0.08), rgba(251, 191, 36, 0.02));
        border-left: 2px solid var(--amber);
        border-radius: 0 10px 10px 0;
        margin: 0 0 2rem 0;
        max-width: 580px;
        font-size: 0.9rem;
        line-height: 1.7;
        color: var(--text-2);
    }}
    .hero-note .icon {{ color: var(--amber); flex-shrink: 0; font-size: 1rem; }}
    .hero-note b {{ color: var(--amber); font-weight: 600; }}

    .chips-mobile {{
        display: none;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }}
    .chip {{
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.45rem 0.95rem;
        background: rgba(20, 12, 40, 0.6);
        border: 1px solid var(--border);
        border-radius: 100px;
        font-size: 0.8rem;
        color: var(--text-2);
    }}
    .chip::before {{ content: ''; width: 6px; height: 6px; border-radius: 50%; background: var(--violet); }}
    @media (max-width: 860px) {{ .chips-mobile {{ display: flex; }} }}

    .hero-stats {{
        display: flex;
        gap: 2.5rem;
        margin-top: 2.5rem;
    }}
    .stat-num {{
        display: block;
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        line-height: 1;
        margin-bottom: 0.35rem;
        font-weight: 500;
    }}
    .stat-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--muted);
    }}

    /* ═══════ SECCIONES ═══════ */
    .category-section {{
        position: relative;
        padding: 4rem 0;
        overflow: hidden;
    }}

    .bg-number {{
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-family: 'Fraunces', serif;
        font-size: clamp(14rem, 30vw, 24rem);
        line-height: 1;
        color: transparent;
        -webkit-text-stroke: 1.5px var(--sec-accent-soft, rgba(192, 132, 252, 0.15));
        pointer-events: none;
        user-select: none;
        z-index: 0;
        opacity: 0.7;
    }}
    .bg-number-left {{ left: -2%; }}
    .bg-number-right {{ right: -2%; }}
    @media (max-width: 900px) {{ .bg-number {{ display: none; }} }}

    .cat-head {{
        position: relative;
        z-index: 1;
        margin-bottom: 2.5rem;
        max-width: 620px;
    }}
    .cat-head.align-right {{
        margin-left: auto;
        text-align: right;
    }}

    .section-num {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 48px;
        height: 36px;
        padding: 0 0.7rem;
        background: var(--sec-accent-soft, rgba(192, 132, 252, 0.1));
        border: 1px solid var(--sec-accent, var(--violet));
        border-radius: 10px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--sec-accent, var(--violet));
        letter-spacing: 0.05em;
        margin-bottom: 1.25rem;
    }}

    .cat-title {{
        font-family: 'Instrument Serif', serif !important;
        font-size: clamp(2rem, 4.5vw, 2.9rem) !important;
        line-height: 1.1 !important;
        margin: 0 0 1rem 0 !important;
        color: var(--text) !important;
    }}

    .cat-desc {{
        font-size: 0.98rem;
        line-height: 1.75;
        color: var(--muted);
        margin: 0 0 1.25rem 0;
        font-weight: 300;
    }}

    .cat-count {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.66rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--sec-accent, var(--violet));
        font-weight: 600;
    }}

    /* ═══════ GRID (reemplazo de carrusel 1 y 2) ═══════ */
    .cards-grid {{
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 2rem;
    }}
    @media (max-width: 720px) {{
        .cards-grid {{ grid-template-columns: 1fr; gap: 1.5rem; }}
    }}

    /* ═══════ CARRUSEL (solo sección 3) ═══════ */
    .carousel-wrap {{ position: relative; z-index: 2; }}
    .carousel-track {{
        display: flex;
        gap: 1.75rem;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        padding: 0.5rem 0.25rem 1.75rem;
        -ms-overflow-style: none;
        scrollbar-width: none;
    }}
    .carousel-track::-webkit-scrollbar {{ display: none; }}

    .carousel-slide {{
        scroll-snap-align: start;
        flex: 0 0 auto;
        width: min(380px, 82vw);
    }}
    @media (min-width: 768px) {{ .carousel-slide {{ width: 380px; }} }}
    .carousel-spacer {{ flex: 0 0 1px; }}

    .carousel-arrow {{
        position: absolute;
        top: 42%;
        transform: translateY(-50%);
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: rgba(20, 12, 40, 0.9);
        border: 1px solid rgba(192, 132, 252, 0.35);
        color: var(--text);
        font-size: 1.5rem;
        line-height: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        z-index: 10;
    }}
    .carousel-arrow:hover {{
        background: var(--sec-accent, var(--violet));
        color: var(--bg);
        transform: translateY(-50%) scale(1.08);
    }}
    .carousel-arrow-left {{ left: -16px; }}
    .carousel-arrow-right {{ right: -16px; }}
    @media (max-width: 640px) {{ .carousel-arrow {{ display: none !important; }} }}

    .carousel-nav {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }}
    .carousel-dots {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    .carousel-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: rgba(154, 139, 181, 0.35);
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        padding: 0;
    }}
    .carousel-dot.is-active {{
        width: 24px;
        border-radius: 100px;
        background: var(--sec-accent, var(--violet));
        box-shadow: 0 0 10px var(--sec-accent-soft, rgba(192, 132, 252, 0.6));
    }}
    .carousel-counter {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.15em;
        color: var(--muted-2);
    }}

    /* ═══════ TARJETAS DE PROYECTO ═══════ */
    .app-card {{
        position: relative;
        display: block;
        background: linear-gradient(180deg, rgba(20, 12, 40, 0.7), rgba(15, 10, 31, 0.9));
        border: 1px solid rgba(45, 31, 74, 0.6);
        border-radius: 20px;
        text-decoration: none !important;
        color: var(--text) !important;
        overflow: hidden;
        transition: all 0.45s cubic-bezier(0.22, 1, 0.36, 1);
        backdrop-filter: blur(10px);
        height: 100%;
    }}
    .app-card:hover {{
        transform: translateY(-8px);
        border-color: var(--sec-accent, var(--violet));
        box-shadow: 0 25px 60px rgba(168, 85, 247, 0.25);
        background: linear-gradient(180deg, rgba(29, 18, 56, 0.8), rgba(20, 12, 40, 0.95));
    }}

    .app-thumb {{
        position: relative;
        width: 100%;
        aspect-ratio: 16 / 10;
        background: #fff;
        overflow: hidden;
        border-bottom: 1px solid rgba(45, 31, 74, 0.4);
    }}
    .app-thumb img {{
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: top center;
        transition: transform 0.6s ease;
    }}
    .app-card:hover .app-thumb img {{ transform: scale(1.06); }}
    .app-thumb-placeholder {{
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #1d1238, #0f0a1f);
        font-family: 'Fraunces', serif;
        font-size: 3rem;
        color: rgba(192, 132, 252, 0.5);
    }}
    .app-thumb-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, transparent 40%, rgba(7, 5, 18, 0.7) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
        display: flex;
        align-items: flex-end;
        padding: 0.8rem;
    }}
    .app-card:hover .app-thumb-overlay {{ opacity: 1; }}
    .thumb-badge {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: rgba(255,255,255,0.9);
    }}

    .app-body {{
        padding: 1.5rem 1.6rem 1.7rem;
    }}
    .app-kicker {{
        display: block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.63rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--sec-accent, var(--violet));
        font-weight: 500;
        margin-bottom: 0.7rem;
    }}
    .app-title {{
        font-family: 'Instrument Serif', serif !important;
        font-size: 1.4rem !important;
        line-height: 1.3 !important;
        margin: 0 0 0.7rem 0 !important;
        color: var(--text) !important;
    }}
    .app-desc {{
        font-size: 0.88rem;
        line-height: 1.7;
        color: var(--muted);
        margin: 0 0 1.35rem 0;
        font-weight: 300;
    }}
    .app-link {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--text-2);
        font-weight: 500;
        transition: all 0.2s ease;
    }}
    .app-card:hover .app-link {{
        gap: 0.8rem;
        color: var(--sec-accent, var(--violet));
    }}

    /* ═══════ FOOTER ═══════ */
    .experience-footer {{
        text-align: center;
        padding-top: 3.5rem;
        margin-top: 3rem;
        border-top: 1px solid var(--border);
        position: relative;
    }}
    .footer-ornament {{
        font-family: 'Fraunces', serif;
        font-size: 1.5rem;
        color: var(--violet);
        margin-bottom: 1.4rem;
        display: block;
        letter-spacing: 0.8rem;
    }}
    .footer-text {{
        font-family: 'Instrument Serif', serif;
        font-size: 1.4rem;
        font-style: italic;
        color: var(--text);
        margin: 0 0 0.6rem 0;
    }}
    .footer-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--muted);
        margin: 0;
    }}
    .back-top {{
        display: inline-block;
        margin-top: 2.75rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--muted-2);
        text-decoration: none !important;
        transition: color 0.2s ease;
    }}
    .back-top:hover {{ color: var(--violet); }}
</style>

<!-- FONDOS ANIMADOS (se mueven al body vía JS para escapar el stacking context) -->
<div id="cosmos-bg">
    <div class="bg-cosmos"></div>
    <div class="mouse-glow" id="mouse-glow"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="aurora">
        <div class="aurora-blob aurora-1"></div>
        <div class="aurora-blob aurora-2"></div>
        <div class="aurora-blob aurora-3"></div>
    </div>
    <div class="stars"></div>
    <div class="stars-2"></div>
    <canvas class="particle-canvas" id="particle-canvas"></canvas>
    <div class="grid-overlay"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star s2"></div>
    <div class="shooting-star s3"></div>
</div>

<!-- Barra de progreso (fuera del wrapper, z-index positivo) -->
<div class="scroll-progress" id="scroll-bar"></div>

<!-- SIDE NAV -->
<nav class="side-nav">
    <a href="#inicio" class="side-nav-dot-wrap is-active" data-sec="inicio">
        <span class="side-nav-label">Inicio</span>
        <span class="side-nav-dot"></span>
    </a>
    <a href="#llms" class="side-nav-dot-wrap" data-sec="llms">
        <span class="side-nav-label">LLMs</span>
        <span class="side-nav-dot"></span>
    </a>
    <a href="#tactil" class="side-nav-dot-wrap" data-sec="tactil">
        <span class="side-nav-label">Táctil</span>
        <span class="side-nav-dot"></span>
    </a>
    <a href="#iot" class="side-nav-dot-wrap" data-sec="iot">
        <span class="side-nav-label">IoT</span>
        <span class="side-nav-dot"></span>
    </a>
    <a href="#final" class="side-nav-dot-wrap" data-sec="final">
        <span class="side-nav-label">Final</span>
        <span class="side-nav-dot"></span>
    </a>
</nav>

<!-- CONTENEDOR PRINCIPAL -->
<div class="experience-wrap">
    <!-- HERO -->
    <section id="inicio" class="hero-grid">
        <div class="portrait-wrap">
            <div class="orbit-ring"></div>
            <div class="portrait-frame">
                <div class="portrait-inner">
                    {portrait_html}
                </div>
            </div>
            <div class="floating-chip chip-1"><strong>EAFIT</strong> Diseño Interactivo</div>
            <div class="floating-chip chip-2"><strong>20 años</strong> Medellín</div>
            <div class="floating-chip chip-3"><strong>2026</strong> Multimodales</div>
            <div class="portrait-caption">Juan Pablo<span class="star">✦</span>Parte 2 · 2026</div>
        </div>
        <div>
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
            <div class="chips-mobile">
                <span class="chip"><strong>EAFIT</strong> Diseño Interactivo</span>
                <span class="chip"><strong>20 años</strong> Medellín</span>
                <span class="chip"><strong>2026</strong> Interfaces Multimodales</span>
            </div>
            <div class="hero-stats">
                <div>
                    <span class="stat-num" style="color: var(--violet);">9</span>
                    <span class="stat-label">Proyectos</span>
                </div>
                <div>
                    <span class="stat-num" style="color: var(--pink);">3</span>
                    <span class="stat-label">Categorías</span>
                </div>
                <div>
                    <span class="stat-num" style="color: var(--amber);">∞</span>
                    <span class="stat-label">Curiosidad</span>
                </div>
            </div>
        </div>
    </section>

    <!-- 01 · LLMs (grid) -->
    <section id="llms" class="category-section" style="--sec-accent: var(--violet); --sec-accent-soft: rgba(192, 132, 252, 0.14);">
        <span class="bg-number bg-number-left" aria-hidden="true">01</span>
        <div class="cat-head">
            <span class="section-num">01</span>
            <h2 class="cat-title">Aplicaciones con LLMs</h2>
            <p class="cat-desc">Modelos de lenguaje e IA generativa aplicados a la comprensión de texto y de imágenes.</p>
            <span class="cat-count">2 aplicaciones</span>
        </div>
        {render_grid(sec1_cards)}
    </section>

    <!-- 02 · TÁCTILES (grid) -->
    <section id="tactil" class="category-section" style="--sec-accent: var(--pink); --sec-accent-soft: rgba(244, 114, 182, 0.14);">
        <span class="bg-number bg-number-right" aria-hidden="true">02</span>
        <div class="cat-head align-right">
            <span class="section-num">02</span>
            <h2 class="cat-title">Interacción con interfaces táctiles</h2>
            <p class="cat-desc">Tableros digitales que combinan dibujo a mano con interpretación inteligente en tiempo real.</p>
            <span class="cat-count">4 aplicaciones</span>
        </div>
        {render_grid(sec2_cards)}
    </section>

    <!-- 03 · IoT (carrusel) -->
    <section id="iot" class="category-section" style="--sec-accent: var(--amber); --sec-accent-soft: rgba(251, 191, 36, 0.14);">
        <span class="bg-number bg-number-left" aria-hidden="true">03</span>
        <div class="cat-head">
            <span class="section-num">03</span>
            <h2 class="cat-title">Sistemas con internet de las cosas</h2>
            <p class="cat-desc">Puentes entre el mundo físico y digital: voz, sensores simulados y protocolos MQTT.</p>
            <span class="cat-count">3 aplicaciones</span>
        </div>
        {render_carousel("carousel-iot", sec3_cards)}
    </section>

    <!-- FOOTER -->
    <footer id="final" class="experience-footer">
        <span class="footer-ornament">✦ ✦ ✦</span>
        <p class="footer-text">Hecho con curiosidad desde Medellín</p>
        <p class="footer-sub">Juan Pablo · EAFIT · Interfaces Multimodales · Parte 2 · 2026</p>
        <a href="#inicio" class="back-top">↑ Volver arriba</a>
    </footer>
</div>
"""

# Fix de indentación para st.markdown
html_content = "\n".join(line.lstrip() for line in html_content.split("\n"))

st.markdown(html_content, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# JAVASCRIPT (vía components.html → SÍ se ejecuta)
# ═══════════════════════════════════════════════════════════════
components.html(
    """
<script>
(function () {
    function setup() {
        const win = window.parent;
        const doc = win.document;

        const probe = doc.getElementById('scroll-bar');
        if (!probe) { setTimeout(setup, 400); return; }
        if (probe.dataset.jsReady === 'true') return;
        probe.dataset.jsReady = 'true';

        // ── 0. Mover fondos al body del padre ──────────────
        // Esto escapa el stacking context de Streamlit y permite
        // que los z-index negativos de los fondos se vean.
        const bg = doc.getElementById('cosmos-bg');
        if (bg && bg.parentNode !== doc.body) {
            doc.body.insertBefore(bg, doc.body.firstChild);
        }

        // ── 1. Scroll progress bar ──────────────────────────
        function updateProgress() {
            const scrollTop = win.scrollY || doc.documentElement.scrollTop;
            const docHeight = doc.documentElement.scrollHeight - win.innerHeight;
            const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
            probe.style.width = pct + '%';
        }
        win.addEventListener('scroll', updateProgress, { passive: true });
        doc.addEventListener('scroll', updateProgress, { passive: true });
        updateProgress();

        // ── 2. Side nav: click + IntersectionObserver ──────
        const sectionIds = ['inicio', 'llms', 'tactil', 'iot', 'final'];
        const navLinks = doc.querySelectorAll('.side-nav-dot-wrap');

        function setActive(id) {
            navLinks.forEach(link => {
                link.classList.toggle('is-active', link.dataset.sec === id);
            });
        }

        navLinks.forEach(link => {
            if (link.dataset.clickBound === 'true') return;
            link.dataset.clickBound = 'true';
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const id = link.dataset.sec;
                setActive(id);
                const target = doc.getElementById(id);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        if (!win.__navObserverSetup) {
            win.__navObserverSetup = true;
            const IO = win.IntersectionObserver || IntersectionObserver;
            const observer = new IO((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) setActive(entry.target.id);
                });
            }, { rootMargin: '-35% 0px -60% 0px', threshold: 0 });

            sectionIds.forEach(id => {
                const el = doc.getElementById(id);
                if (el) observer.observe(el);
            });
        }

        // ── 3. Carruseles ──────────────────────────────────
        doc.querySelectorAll('.carousel-wrap').forEach(wrap => {
            if (wrap.dataset.carouselBound === 'true') return;
            wrap.dataset.carouselBound = 'true';

            const track = wrap.querySelector('.carousel-track');
            if (!track) return;
            const prev = wrap.querySelector('.carousel-arrow-left');
            const next = wrap.querySelector('.carousel-arrow-right');
            const dots = wrap.querySelectorAll('.carousel-dot');
            const slides = track.querySelectorAll('.carousel-slide');
            const counter = wrap.querySelector('.carousel-counter');

            const step = () => {
                const s = slides[0];
                return s ? s.offsetWidth + 28 : 400;
            };

            if (prev) prev.addEventListener('click', () =>
                track.scrollBy({ left: -step(), behavior: 'smooth' }));
            if (next) next.addEventListener('click', () =>
                track.scrollBy({ left: step(), behavior: 'smooth' }));

            const updateDots = () => {
                const sl = track.scrollLeft;
                let closest = 0, minDist = Infinity;
                slides.forEach((s, i) => {
                    const d = Math.abs(s.offsetLeft - track.offsetLeft - sl);
                    if (d < minDist) { minDist = d; closest = i; }
                });
                dots.forEach((d, i) => d.classList.toggle('is-active', i === closest));
                if (counter) {
                    counter.textContent =
                        String(closest + 1).padStart(2, '0') + ' / ' +
                        String(slides.length).padStart(2, '0');
                }
            };
            track.addEventListener('scroll', updateDots, { passive: true });
            dots.forEach((d, i) => d.addEventListener('click', () => {
                const s = slides[i];
                if (s) track.scrollTo({
                    left: s.offsetLeft - track.offsetLeft,
                    behavior: 'smooth'
                });
            }));
            updateDots();
        });

        // ── 4. Mouse glow + parallax ───────────────────────
        const glow = doc.getElementById('mouse-glow');
        const orb1 = doc.querySelector('.orb-1');
        const orb2 = doc.querySelector('.orb-2');
        if (glow && !glow.dataset.bound) {
            glow.dataset.bound = 'true';
            win.addEventListener('mousemove', (e) => {
                glow.style.setProperty('--mx', e.clientX + 'px');
                glow.style.setProperty('--my', e.clientY + 'px');
                const x = e.clientX / win.innerWidth - 0.5;
                const y = e.clientY / win.innerHeight - 0.5;
                if (orb1) {
                    orb1.style.setProperty('--px', (x * 70) + 'px');
                    orb1.style.setProperty('--py', (y * 70) + 'px');
                }
                if (orb2) {
                    orb2.style.setProperty('--px', (-x * 70) + 'px');
                    orb2.style.setProperty('--py', (-y * 70) + 'px');
                }
            }, { passive: true });
        }

        // ── 5. Canvas de partículas flotantes ──────────────
        const canvas = doc.getElementById('particle-canvas');
        if (canvas && !canvas.dataset.bound) {
            canvas.dataset.bound = 'true';
            const ctx = canvas.getContext('2d');

            function resize() {
                canvas.width = win.innerWidth;
                canvas.height = win.innerHeight;
            }
            resize();
            win.addEventListener('resize', resize);

            const palette = [
                '192, 132, 252',
                '244, 114, 182',
                '251, 191, 36',
                '255, 255, 255',
            ];
            const count = Math.min(110, Math.max(50,
                Math.floor((win.innerWidth * win.innerHeight) / 16000)));
            const parts = [];
            for (let i = 0; i < count; i++) {
                parts.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    r: Math.random() * 1.7 + 0.4,
                    vx: (Math.random() - 0.5) * 0.25,
                    vy: -Math.random() * 0.35 - 0.08,
                    color: palette[Math.floor(Math.random() * palette.length)],
                    baseAlpha: Math.random() * 0.45 + 0.15,
                    phase: Math.random() * Math.PI * 2,
                });
            }

            let t = 0;
            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                t += 0.035;
                for (let i = 0; i < parts.length; i++) {
                    const p = parts[i];
                    p.x += p.vx;
                    p.y += p.vy;
                    if (p.y < -10) { p.y = canvas.height + 10; p.x = Math.random() * canvas.width; }
                    if (p.x < -10) p.x = canvas.width + 10;
                    if (p.x > canvas.width + 10) p.x = -10;

                    const tw = Math.sin(t + p.phase) * 0.35 + 0.65;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(' + p.color + ', ' + (p.baseAlpha * tw) + ')';
                    ctx.fill();
                }
                requestAnimationFrame(draw);
            }
            draw();
        }
    }

    setTimeout(setup, 300);
    setTimeout(setup, 900);
    setTimeout(setup, 1800);
    setTimeout(setup, 3000);
})();
</script>
""",
    height=0,
)
