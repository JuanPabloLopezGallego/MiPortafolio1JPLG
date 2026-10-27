import base64
import html
from functools import lru_cache
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Portafolio · Juan Pablo · Parte 2",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSET_DIR = Path(__file__).resolve().parent
IMAGE_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif",
}


@lru_cache(maxsize=32)
def image_data_uri(filename):
    """Return a local image as a data URI, or an empty string when it is missing."""
    image_path = ASSET_DIR / filename
    mime_type = IMAGE_MIME_TYPES.get(image_path.suffix.lower())
    if not mime_type:
        return ""

    try:
        image_data = image_path.read_bytes()
    except OSError:
        return ""

    encoded = base64.b64encode(image_data).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


SECTIONS = [
    {
        "id": "llms",
        "number": "01",
        "title": "Aplicaciones con LLMs",
        "count": "2 aplicaciones",
        "filter": "LLMs",
        "grid": "two",
        "projects": [
            {
                "kicker": "NLP · Procesamiento",
                "title": "Procesamiento de Lenguaje",
                "description": "Explora cómo la IA comprende, analiza y genera lenguaje natural en español.",
                "url": "https://procesamientolenguajejplg-dpcdtmrteadz4zxvzn8adh.streamlit.app/",
                "image": "LLM1.PNG",
            },
            {
                "kicker": "Computer Vision",
                "title": "Visión artificial",
                "description": "Modelos de visión por computadora que reconocen imágenes, objetos y patrones.",
                "url": "https://visionapp-8whsafj8pj5hdiuow4yjyb.streamlit.app/",
                "image": "LLM2.PNG",
            },
        ],
    },
    {
        "id": "tactil",
        "number": "02",
        "title": "Interacción con interfaces táctiles",
        "count": "4 aplicaciones",
        "filter": "Táctiles",
        "grid": "two",
        "projects": [
            {
                "kicker": "Visión + GPT",
                "title": "Tablero inteligente",
                "description": "Dibuja un boceto y deja que la IA lo interprete, lo describa o lo resuelva.",
                "url": "https://tablerotuneado-dqjtotfrqskiyeosh6youa.streamlit.app/",
                "image": "Tablero3.PNG",
            },
            {
                "kicker": "Matemáticas · GPT",
                "title": "Tablero de matemáticas",
                "description": "Dibuja una operación o ecuación y la IA la resuelve paso a paso con LaTeX.",
                "url": "https://tablerotuneado-ez8ftd2kuoia7yoh7cpdhe.streamlit.app/",
                "image": "Tablero4.PNG",
            },
            {
                "kicker": "OCR · Números",
                "title": "Tablero que lee números",
                "description": "Escribe un número a mano y la IA lo reconoce e interpreta al instante.",
                "url": "https://tactilnumeros-kdpcwepxhzeer6zvu3cq6x.streamlit.app/",
                "image": "Tablero1.PNG",
            },
            {
                "kicker": "Canvas · Personalizable",
                "title": "Tablero para dibujar",
                "description": "Un lienzo libre con herramientas y colores personalizables para crear.",
                "url": "https://tableropersonalizado-nkqwmc7lntrdxrnqmo7nl6.streamlit.app/",
                "image": "Tablero2.PNG",
            },
        ],
    },
    {
        "id": "iot",
        "number": "03",
        "title": "Sistemas con internet de las cosas",
        "count": "3 aplicaciones",
        "filter": "IoT",
        "grid": "three",
        "projects": [
            {
                "kicker": "Voz · Control",
                "title": "Control de voz",
                "description": "Interactúa con la aplicación usando únicamente tu voz, sin tocar el teclado.",
                "url": "https://ctrlvoice-4zw5fqi5pmuizke4vdecw7.streamlit.app/",
                "image": "IOT3.PNG",
            },
            {
                "kicker": "Sensor · MQTT",
                "title": "Wokwi a Streamlit",
                "description": "Un sensor simulado en Wokwi envía datos a Streamlit a través de MQTT.",
                "url": "https://lectormqtt-t59niwifyecackdckk82fx.streamlit.app/",
                "image": "IOT1.PNG",
            },
            {
                "kicker": "Control · MQTT",
                "title": "Streamlit a Wokwi",
                "description": "Controla dispositivos simulados en Wokwi desde una interfaz en Streamlit.",
                "url": "https://appawokwicmqtt-spyylhsrmng4sdf5fncrty.streamlit.app/",
                "image": "IOT2.PNG",
            },
        ],
    },
]


st.markdown(
    """
    <style>
    :root {
        --ink: #0c1916;
        --ink-soft: #142720;
        --ink-raised: #1b322a;
        --cream: #f2f0e8;
        --cream-soft: #dce2d8;
        --muted: #a9b6ac;
        --muted-deep: #73837a;
        --line: rgba(226, 236, 226, 0.15);
        --line-strong: rgba(226, 236, 226, 0.25);
        --lime: #d8f56a;
        --coral: #ff9874;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; scroll-padding-top: 82px; }
    body {
        background: var(--ink);
        color: var(--cream);
        overflow-x: hidden;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .stApp {
        background:
            radial-gradient(ellipse at 84% 28%, rgba(42, 82, 65, 0.16), transparent 34%),
            var(--ink);
        color: var(--cream);
    }
    #MainMenu, footer, div[data-testid="stToolbar"], div[data-testid="stDecoration"] {
        visibility: hidden;
    }
    header[data-testid="stHeader"] {
        height: 0;
        background: transparent;
    }
    .block-container {
        max-width: 1320px !important;
        padding: 0 clamp(22px, 5vw, 72px) 5rem !important;
    }
    .stMarkdown { margin-bottom: 0 !important; color: var(--cream); }
    a { text-decoration: none; }
    a:focus-visible, button:focus-visible, input:focus-visible {
        outline: 2px solid var(--lime) !important;
        outline-offset: 4px !important;
    }
    ::selection { background: var(--lime); color: var(--ink); }

    .portfolio-nav {
        position: sticky;
        top: 0;
        z-index: 50;
        width: 100vw;
        margin-left: calc(50% - 50vw);
        border-bottom: 1px solid rgba(242, 240, 232, 0.1);
        background: rgba(12, 25, 22, 0.86);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
    }
    .nav-inner {
        width: min(1320px, calc(100% - 10vw));
        min-height: 72px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
    }
    .nav-brand {
        display: inline-flex;
        align-items: center;
        gap: 0.8rem;
        color: var(--cream) !important;
        font-size: 0.88rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        line-height: 1.2;
        white-space: nowrap;
    }
    .nav-mark {
        display: grid;
        place-items: center;
        width: 34px;
        height: 34px;
        border: 1px solid rgba(216, 245, 106, 0.55);
        color: var(--lime);
        font-family: Georgia, serif;
        font-size: 0.83rem;
        letter-spacing: -0.08em;
    }
    .nav-brand small {
        display: block;
        margin-top: 0.22rem;
        color: var(--muted);
        font-size: 0.58rem;
        font-weight: 400;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }
    .nav-links {
        display: flex;
        align-items: center;
        gap: clamp(1.1rem, 3vw, 2.6rem);
    }
    .nav-links a {
        position: relative;
        padding: 0.65rem 0;
        color: var(--cream-soft) !important;
        font-size: 0.7rem;
        letter-spacing: 0.11em;
        text-transform: uppercase;
        transition: color 180ms ease;
    }
    .nav-links a::after {
        position: absolute;
        right: 0;
        bottom: 0;
        left: 0;
        height: 1px;
        background: var(--lime);
        content: "";
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 220ms ease;
    }
    .nav-links a:hover { color: var(--lime) !important; }
    .nav-links a:hover::after { transform: scaleX(1); }

    .hero {
        position: relative;
        isolation: isolate;
        display: flex;
        align-items: center;
        width: 100vw;
        min-height: max(720px, calc(100vh - 72px));
        margin-left: calc(50% - 50vw);
        overflow: hidden;
        background: var(--ink);
    }
    .hero::before {
        position: absolute;
        z-index: 0;
        inset: -2%;
        background-image: var(
            --hero-image,
            radial-gradient(ellipse at 74% 40%, rgba(98, 139, 89, 0.42), transparent 30%),
            radial-gradient(ellipse at 88% 74%, rgba(255, 152, 116, 0.18), transparent 27%),
            linear-gradient(130deg, #142720, #0c1916 70%)
        );
        background-position: center 42%;
        background-size: cover;
        content: "";
        animation: hero-image-enter 1.8s cubic-bezier(0.2, 0.65, 0.25, 1) both;
    }
    .hero::after {
        position: absolute;
        z-index: 1;
        inset: 0;
        background:
            linear-gradient(90deg, rgba(12, 25, 22, 0.98) 0%, rgba(12, 25, 22, 0.91) 31%, rgba(12, 25, 22, 0.55) 59%, rgba(12, 25, 22, 0.15) 100%),
            linear-gradient(0deg, rgba(12, 25, 22, 0.78) 0%, transparent 42%);
        content: "";
        pointer-events: none;
    }
    .hero-monogram {
        position: absolute;
        z-index: 1;
        right: clamp(3rem, 13vw, 13rem);
        bottom: -0.12em;
        color: rgba(216, 245, 106, 0.1);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-size: clamp(16rem, 34vw, 34rem);
        letter-spacing: -0.13em;
        line-height: 0.8;
        pointer-events: none;
        user-select: none;
    }
    .hero-inner {
        position: relative;
        z-index: 3;
        width: min(1320px, calc(100% - 10vw));
        margin: 0 auto;
        padding: clamp(7rem, 12vh, 10rem) 0 clamp(6rem, 11vh, 9rem);
    }
    .hero-copy { max-width: 690px; }
    .hero-edition, .hero-kicker, .profile-caption, .filter-kicker,
    .section-num, .section-count, .project-kicker, .project-action,
    .footer-sub {
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
    }
    .hero-edition {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 0 0 2.2rem;
        color: var(--lime);
        font-size: 0.67rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        animation: rise-in 680ms 80ms both;
    }
    .hero-edition::before {
        width: 30px;
        height: 1px;
        background: var(--lime);
        content: "";
    }
    .hero-kicker {
        margin: 0 0 1.1rem;
        color: var(--cream-soft);
        font-size: 0.69rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        animation: rise-in 680ms 140ms both;
    }
    .hero-name {
        margin: 0 0 1.45rem;
        color: var(--cream);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-weight: 400;
        letter-spacing: -0.055em;
        line-height: 0.9;
    }
    .hero-name > span {
        display: block;
        margin-bottom: 0.23em;
        color: var(--cream-soft);
        font-size: clamp(1.35rem, 2.3vw, 2rem);
        font-style: italic;
        letter-spacing: -0.02em;
        animation: rise-in 700ms 190ms both;
    }
    .hero-name strong {
        display: block;
        color: var(--cream);
        font-size: clamp(5rem, 10vw, 9rem);
        font-weight: 400;
        animation: rise-in 760ms 240ms both;
    }
    .hero-dot { color: var(--lime); }
    .hero-desc {
        max-width: 600px;
        margin: 0 0 2rem;
        color: var(--cream-soft);
        font-size: clamp(0.98rem, 1.2vw, 1.08rem);
        font-weight: 350;
        line-height: 1.8;
        animation: rise-in 720ms 330ms both;
    }
    .hero-desc strong { color: var(--cream); font-weight: 650; }
    .hero-cta {
        display: inline-flex;
        align-items: center;
        gap: 1.2rem;
        padding: 0.75rem 0;
        border-bottom: 1px solid var(--lime);
        color: var(--lime) !important;
        font-size: 0.76rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        animation: rise-in 720ms 430ms both;
        transition: gap 180ms ease, color 180ms ease;
    }
    .hero-cta > span:last-child { color: var(--cream); font-size: 1.2rem; font-weight: 400; }
    .hero-cta:hover { gap: 1.65rem; color: var(--cream) !important; }

    .profile-brief {
        display: grid;
        grid-template-columns: minmax(0, 1.1fr) minmax(320px, 0.9fr);
        gap: clamp(2rem, 7vw, 7rem);
        padding: clamp(3.5rem, 7vw, 6.5rem) 0;
        border-bottom: 1px solid var(--line);
    }
    .profile-caption {
        margin: 0 0 1.5rem;
        color: var(--muted);
        font-size: 0.66rem;
        letter-spacing: 0.17em;
        text-transform: uppercase;
    }
    .profile-caption span { padding: 0 0.5rem; color: var(--lime); }
    .profile-note {
        display: flex;
        align-items: flex-start;
        gap: 0.9rem;
        max-width: 660px;
        margin: 0;
        padding-left: 1rem;
        border-left: 2px solid var(--coral);
        color: var(--cream-soft);
        font-size: 0.98rem;
        line-height: 1.75;
    }
    .profile-note-mark { color: var(--coral); }
    .profile-note strong { color: var(--cream); font-weight: 650; }
    .profile-facts {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        align-content: center;
        gap: 1.25rem;
    }
    .profile-fact { margin: 0; }
    .profile-fact strong {
        display: block;
        margin-bottom: 0.38rem;
        color: var(--lime);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-size: 1.5rem;
        font-weight: 400;
    }
    .profile-fact span {
        display: block;
        color: var(--muted);
        font-size: 0.7rem;
        line-height: 1.5;
    }

    .filter-intro {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 2rem;
        margin: clamp(4rem, 8vw, 7rem) 0 0.8rem;
    }
    .filter-kicker {
        margin: 0;
        color: var(--muted);
        font-size: 0.68rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    div[data-testid="stRadio"] { margin-bottom: 1rem; }
    div[data-testid="stRadio"] > label { display: none !important; }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        display: flex;
        flex-wrap: wrap;
        gap: clamp(1.2rem, 3vw, 2.7rem);
        border-bottom: 1px solid var(--line);
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        min-height: 46px;
        margin: 0 !important;
        padding: 0.75rem 0 0.8rem !important;
        border-bottom: 1px solid transparent;
        border-radius: 0 !important;
        background: transparent !important;
        color: var(--muted) !important;
        cursor: pointer;
        transition: color 180ms ease, border-color 180ms ease;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label:hover,
    div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) {
        border-bottom-color: var(--lime) !important;
        color: var(--lime) !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] > label p,
    div[data-testid="stRadio"] div[role="radiogroup"] > label span {
        color: inherit !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .section-head {
        display: flex;
        align-items: center;
        gap: 1.1rem;
        margin: clamp(4rem, 7vw, 6.2rem) 0 1.8rem;
        padding-bottom: 1.2rem;
        border-bottom: 1px solid var(--line);
        scroll-margin-top: 100px;
    }
    .section-num {
        display: inline-grid;
        place-items: center;
        min-width: 42px;
        height: 34px;
        border: 1px solid rgba(216, 245, 106, 0.36);
        color: var(--lime);
        font-size: 0.72rem;
        letter-spacing: 0.08em;
    }
    .section-title {
        flex: 1;
        margin: 0;
        color: var(--cream);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-size: clamp(1.65rem, 3vw, 2.45rem);
        font-weight: 400;
        letter-spacing: -0.025em;
        line-height: 1.1;
    }
    .section-count {
        color: var(--muted-deep);
        font-size: 0.62rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        white-space: nowrap;
    }
    .project-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: clamp(1.4rem, 3vw, 2.7rem);
        margin-bottom: clamp(3.8rem, 7vw, 6.5rem);
    }
    .project-grid--three { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .project-card {
        display: flex;
        min-width: 0;
        flex-direction: column;
        overflow: hidden;
        border: 1px solid var(--line);
        background: rgba(20, 39, 32, 0.62);
        color: var(--cream) !important;
        text-decoration: none !important;
        animation: rise-in 620ms cubic-bezier(0.2, 0.65, 0.25, 1) both;
        animation-delay: calc(var(--card-index, 0) * 70ms);
        transition: border-color 220ms ease, background 220ms ease, transform 220ms ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        border-color: rgba(216, 245, 106, 0.64);
        background: rgba(27, 50, 42, 0.92);
    }
    .project-media {
        position: relative;
        aspect-ratio: 16 / 9;
        overflow: hidden;
        border-bottom: 1px solid var(--line);
        background:
            radial-gradient(circle at 52% 48%, rgba(216, 245, 106, 0.12), transparent 22%),
            linear-gradient(145deg, #1b322a, #101d19);
    }
    .project-media img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center top;
        transition: transform 650ms cubic-bezier(0.2, 0.65, 0.25, 1), filter 350ms ease;
    }
    .project-card:hover .project-media img { transform: scale(1.04); }
    .thumb-placeholder {
        display: grid;
        width: 100%;
        height: 100%;
        place-items: center;
        color: rgba(216, 245, 106, 0.62);
        font-family: Georgia, serif;
        font-size: 2.2rem;
    }
    .media-arrow {
        position: absolute;
        right: 1rem;
        bottom: 1rem;
        display: grid;
        width: 36px;
        height: 36px;
        place-items: center;
        border: 1px solid rgba(242, 240, 232, 0.52);
        background: rgba(12, 25, 22, 0.72);
        color: var(--cream);
        font-size: 1rem;
        transition: color 180ms ease, border-color 180ms ease, transform 180ms ease;
    }
    .project-card:hover .media-arrow {
        transform: translate(2px, -2px);
        border-color: var(--lime);
        color: var(--lime);
    }
    .project-copy {
        display: flex;
        flex: 1;
        flex-direction: column;
        align-items: flex-start;
        padding: clamp(1.2rem, 2vw, 1.7rem);
    }
    .project-kicker {
        margin: 0 0 0.8rem;
        color: var(--lime);
        font-size: 0.61rem;
        letter-spacing: 0.17em;
        text-transform: uppercase;
    }
    .project-title {
        margin: 0 0 0.7rem;
        color: var(--cream);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-size: clamp(1.35rem, 2vw, 1.7rem);
        font-weight: 400;
        letter-spacing: -0.015em;
        line-height: 1.18;
    }
    .project-desc {
        flex: 1;
        margin: 0 0 1.35rem;
        color: var(--muted);
        font-size: 0.87rem;
        line-height: 1.65;
    }
    .project-action {
        display: inline-flex;
        align-items: center;
        gap: 0.65rem;
        margin-top: auto;
        color: var(--cream-soft);
        font-size: 0.63rem;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        transition: gap 180ms ease, color 180ms ease;
    }
    .project-card:hover .project-action { gap: 0.95rem; color: var(--lime); }

    .portfolio-footer {
        width: 100vw;
        margin-left: calc(50% - 50vw);
        padding: 4rem 1.5rem 2.5rem;
        border-top: 1px solid var(--line);
        text-align: center;
    }
    .footer-ornament {
        display: block;
        margin-bottom: 1rem;
        color: var(--lime);
        font-family: Georgia, serif;
        font-size: 1.2rem;
        letter-spacing: 0.65rem;
        animation: soft-glow 3.8s ease-in-out infinite;
    }
    .footer-text {
        margin: 0 0 0.75rem;
        color: var(--cream);
        font-family: "Iowan Old Style", "Palatino Linotype", Georgia, serif;
        font-size: 1.35rem;
        font-style: italic;
    }
    .footer-sub {
        margin: 0;
        color: var(--muted);
        font-size: 0.61rem;
        letter-spacing: 0.16em;
        line-height: 1.8;
        text-transform: uppercase;
    }

    @keyframes rise-in {
        from { opacity: 0; transform: translate3d(0, 20px, 0); }
        to { opacity: 1; transform: translate3d(0, 0, 0); }
    }
    @keyframes hero-image-enter {
        from { transform: scale(1.06); }
        to { transform: scale(1); }
    }
    @keyframes soft-glow {
        0%, 100% { opacity: 0.72; }
        50% { opacity: 1; }
    }

    @media (max-width: 900px) {
        .hero { min-height: 760px; }
        .hero-inner { width: min(100% - 9vw, 760px); }
        .hero::after {
            background:
                linear-gradient(90deg, rgba(12, 25, 22, 0.97) 0%, rgba(12, 25, 22, 0.83) 50%, rgba(12, 25, 22, 0.42) 100%),
                linear-gradient(0deg, rgba(12, 25, 22, 0.83) 0%, transparent 52%);
        }
        .profile-brief { grid-template-columns: 1fr; gap: 2.3rem; }
        .profile-facts { max-width: 720px; }
        .project-grid--three { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    @media (max-width: 620px) {
        .block-container { padding: 0 20px 3rem !important; }
        .nav-inner { width: calc(100% - 40px); min-height: 66px; gap: 1rem; }
        .nav-mark { display: none; }
        .nav-brand { font-size: 0.78rem; }
        .nav-brand small { font-size: 0.51rem; }
        .nav-links { gap: 0.85rem; }
        .nav-links a { font-size: 0.56rem; letter-spacing: 0.06em; }
        .hero { min-height: 780px; }
        .hero-inner { width: calc(100% - 42px); padding: 100px 0 78px; }
        .hero-edition { margin-bottom: 1.8rem; font-size: 0.56rem; letter-spacing: 0.1em; }
        .hero-kicker { font-size: 0.59rem; letter-spacing: 0.13em; }
        .hero-name strong { font-size: clamp(4.25rem, 16vw, 6rem); }
        .hero-desc { font-size: 0.94rem; line-height: 1.72; }
        .hero-monogram { right: 0.5rem; bottom: 0; font-size: 72vw; }
        .profile-brief { padding: 3.5rem 0; }
        .profile-note { font-size: 0.9rem; }
        .profile-facts { grid-template-columns: 1fr; gap: 1rem; }
        .profile-fact {
            display: flex;
            align-items: baseline;
            gap: 0.8rem;
            padding-top: 0.8rem;
            border-top: 1px solid var(--line);
        }
        .profile-fact strong { min-width: 74px; margin: 0; font-size: 1.2rem; }
        .filter-intro { margin-top: 3.5rem; }
        div[data-testid="stRadio"] div[role="radiogroup"] { gap: 0.95rem; }
        div[data-testid="stRadio"] div[role="radiogroup"] > label { min-height: 42px; }
        div[data-testid="stRadio"] div[role="radiogroup"] > label p,
        div[data-testid="stRadio"] div[role="radiogroup"] > label span {
            font-size: 0.62rem !important;
            letter-spacing: 0.04em;
        }
        .section-head { gap: 0.7rem; margin-top: 3.7rem; }
        .section-num { min-width: 36px; height: 31px; font-size: 0.64rem; }
        .section-title { font-size: 1.5rem; }
        .section-count { display: none; }
        .project-grid, .project-grid--three { grid-template-columns: 1fr; gap: 1.2rem; }
        .project-copy { padding: 1.2rem; }
        .project-title { font-size: 1.45rem; }
        .portfolio-footer { padding: 3.4rem 1.25rem 2.2rem; }
        .footer-sub { max-width: 320px; margin: 0 auto; font-size: 0.56rem; }
    }
    @media (prefers-reduced-motion: reduce) {
        html { scroll-behavior: auto; }
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: 0.01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


hero_image = image_data_uri("yo.png")
hero_style = f" style=\"--hero-image: url('{hero_image}')\"" if hero_image else ""
hero_fallback = (
    '<div class="hero-monogram" aria-hidden="true">JP</div>' if not hero_image else ""
)

st.markdown(
    f"""
    <nav class="portfolio-nav" aria-label="Navegación principal">
        <div class="nav-inner">
            <a class="nav-brand" href="#inicio" aria-label="Juan Pablo, inicio">
                <span class="nav-mark" aria-hidden="true">JP</span>
                <span>Juan Pablo<small>Interfaces Multimodales</small></span>
            </a>
            <div class="nav-links">
                <a href="#llms">LLMs</a>
                <a href="#tactil">Táctiles</a>
                <a href="#iot">IoT</a>
            </div>
        </div>
    </nav>

    <section class="hero" id="inicio"{hero_style}>
        {hero_fallback}
        <div class="hero-inner">
            <div class="hero-copy">
                <p class="hero-edition">Segunda parte · Portafolio 2026</p>
                <p class="hero-kicker">Interfaces Multimodales</p>
                <h1 class="hero-name">
                    <span>Hola, soy</span>
                    <strong>Juan Pablo</strong>
                </h1>
                <p class="hero-desc">
                    Tengo <strong>20 años</strong> y estudio <strong>Diseño Interactivo</strong>
                    en <strong>EAFIT</strong>. Esta es la <strong>segunda parte</strong> de mi
                    portafolio para la materia de <strong>Interfaces Multimodales</strong>, donde
                    reunimos los proyectos más recientes del semestre: desde modelos de lenguaje
                    hasta integraciones con hardware y visión por computadora.
                </p>
                <a class="hero-cta" href="#proyectos">
                    <span>Explorar aplicaciones</span><span aria-hidden="true">↓</span>
                </a>
            </div>
        </div>
    </section>

    <section class="profile-brief" aria-label="Perfil de Juan Pablo">
        <div>
            <p class="profile-caption">Juan Pablo <span>✦</span> Parte 2 · 2026</p>
            <p class="profile-note">
                <span class="profile-note-mark" aria-hidden="true">✦</span>
                <span>Esta es la <strong>segunda parte</strong> del portafolio. Reúne las actividades
                más recientes del curso, incluyendo las integraciones con hardware y los tableros
                interactivos.</span>
            </p>
        </div>
        <div class="profile-facts">
            <p class="profile-fact"><strong>EAFIT</strong><span>Diseño Interactivo</span></p>
            <p class="profile-fact"><strong>20 años</strong><span>Medellín</span></p>
            <p class="profile-fact"><strong>2026</strong><span>Interfaces Multimodales</span></p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="filter-intro" id="proyectos"><p class="filter-kicker">Explorar por sección</p></div>',
    unsafe_allow_html=True,
)
selected_filter = st.radio(
    "Filtrar aplicaciones por sección",
    options=["Todas", "LLMs", "Táctiles", "IoT"],
    index=0,
    horizontal=True,
    label_visibility="collapsed",
    key="portfolio_section_filter",
)

for section in SECTIONS:
    if selected_filter != "Todas" and section["filter"] != selected_filter:
        continue

    safe_id = html.escape(section["id"], quote=True)
    safe_number = html.escape(section["number"])
    safe_title = html.escape(section["title"])
    safe_count = html.escape(section["count"])
    st.markdown(
        f"""
        <div class="section-head" id="{safe_id}">
            <span class="section-num">{safe_number}</span>
            <h2 class="section-title">{safe_title}</h2>
            <span class="section-count">{safe_count}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = []
    for index, project in enumerate(section["projects"]):
        project_image = image_data_uri(project["image"])
        safe_title = html.escape(project["title"])
        if project_image:
            media_content = (
                f'<img src="{project_image}" alt="{safe_title}" loading="lazy">'
            )
        else:
            media_content = '<div class="thumb-placeholder" aria-hidden="true"><span>◇</span></div>'

        safe_kicker = html.escape(project["kicker"])
        safe_description = html.escape(project["description"])
        safe_url = html.escape(project["url"], quote=True)
        cards.append(
            f"""
            <a class="project-card" href="{safe_url}" target="_blank"
               rel="noopener noreferrer" style="--card-index: {index};">
                <div class="project-media">
                    {media_content}
                    <span class="media-arrow" aria-hidden="true">↗</span>
                </div>
                <div class="project-copy">
                    <p class="project-kicker">{safe_kicker}</p>
                    <h3 class="project-title">{safe_title}</h3>
                    <p class="project-desc">{safe_description}</p>
                    <span class="project-action">Abrir aplicación →</span>
                </div>
            </a>
            """
        )

    grid_class = "project-grid project-grid--" + section["grid"]
    st.markdown(
        f'<div class="{grid_class}">{"".join(cards)}</div>',
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <div class="portfolio-footer" role="contentinfo">
        <span class="footer-ornament" aria-hidden="true">✦ ✦ ✦</span>
        <p class="footer-text">Hecho con curiosidad desde Medellín</p>
        <p class="footer-sub">Juan Pablo · EAFIT · Interfaces Multimodales · Parte 2 · 2026</p>
    </div>
    """,
    unsafe_allow_html=True,
)
