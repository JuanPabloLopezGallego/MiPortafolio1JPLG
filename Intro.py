import streamlit as st
import os
import time
import glob
import cv2
import numpy as np
import pytesseract

from PIL import Image
from gtts import gTTS
from googletrans import Translator


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="EasyTranslate",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

TEMP_FOLDER = "temp"

if not os.path.exists(TEMP_FOLDER):
    os.makedirs(TEMP_FOLDER)

translator = Translator()


# ============================================================
# IDIOMAS
# ============================================================

LANGUAGES = {
    "🇪🇸 Español": {"translation": "es", "tesseract": "spa"},
    "🇺🇸 English": {"translation": "en", "tesseract": "eng"},
    "🇫🇷 Français": {"translation": "fr", "tesseract": "fra"},
    "🇩🇪 Deutsch": {"translation": "de", "tesseract": "deu"},
    "🇮🇹 Italiano": {"translation": "it", "tesseract": "ita"},
    "🇵🇹 Português": {"translation": "pt", "tesseract": "por"},
    "🇳🇱 Nederlands": {"translation": "nl", "tesseract": "nld"},
    "🇷🇺 Русский": {"translation": "ru", "tesseract": "rus"},
    "🇺🇦 Українська": {"translation": "uk", "tesseract": "ukr"},
    "🇵🇱 Polski": {"translation": "pl", "tesseract": "pol"},
    "🇨🇿 Čeština": {"translation": "cs", "tesseract": "ces"},
    "🇸🇰 Slovenčina": {"translation": "sk", "tesseract": "slk"},
    "🇭🇺 Magyar": {"translation": "hu", "tesseract": "hun"},
    "🇷🇴 Română": {"translation": "ro", "tesseract": "ron"},
    "🇹🇷 Türkçe": {"translation": "tr", "tesseract": "tur"},
    "🇬🇷 Ελληνικά": {"translation": "el", "tesseract": "ell"},
    "🇸🇪 Svenska": {"translation": "sv", "tesseract": "swe"},
    "🇩🇰 Dansk": {"translation": "da", "tesseract": "dan"},
    "🇫🇮 Suomi": {"translation": "fi", "tesseract": "fin"},
    "🇳🇴 Norsk": {"translation": "no", "tesseract": "nor"},
    "🇮🇳 हिन्दी": {"translation": "hi", "tesseract": "hin"},
    "🇧🇩 বাংলা": {"translation": "bn", "tesseract": "ben"},
    "🇮🇩 Bahasa Indonesia": {"translation": "id", "tesseract": "ind"},
    "🇻🇳 Tiếng Việt": {"translation": "vi", "tesseract": "vie"},
    "🇹🇭 ไทย": {"translation": "th", "tesseract": "tha"},
    "🇰🇷 한국어": {"translation": "ko", "tesseract": "kor"},
    "🇯🇵 日本語": {"translation": "ja", "tesseract": "jpn"},
    "🇨🇳 简体中文": {"translation": "zh-cn", "tesseract": "chi_sim"},
    "🇹🇼 繁體中文": {"translation": "zh-tw", "tesseract": "chi_tra"},
    "🇸🇦 العربية": {"translation": "ar", "tesseract": "ara"},
    "🇮🇱 עברית": {"translation": "iw", "tesseract": "heb"}
}

LANGUAGE_LIST = list(LANGUAGES.keys())


# ============================================================
# ACENTOS
# ============================================================

ACCENTS = {
    "🌎 Predeterminado": "com",
    "🇺🇸 Estados Unidos": "com",
    "🇬🇧 Reino Unido": "co.uk",
    "🇨🇦 Canadá": "ca",
    "🇦🇺 Australia": "com.au",
    "🇮🇳 India": "co.in",
    "🇮🇪 Irlanda": "ie",
    "🇿🇦 Sudáfrica": "co.za"
}


# ============================================================
# ESTILOS MEJORADOS (CSS)
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    :root {
        --primary: #2563eb;
        --primary-gradient: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        --surface-bg: #f8fafc;
        --card-bg: #ffffff;
        --border-color: #e2e8f0;
        --text-main: #0f172a;
        --text-muted: #64748b;
    }

    .stApp {
        background-color: #f1f5f9;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer { visibility: hidden; }

    /* --- HERO BANNER --- */
    .hero-container {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        color: #ffffff;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff !important;
        margin-bottom: 0.5rem;
        letter-spacing: -0.03em;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #94a3b8 !important;
        margin-bottom: 1.25rem;
        font-weight: 400;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 6px 16px;
        border-radius: 50px;
        font-size: 0.85rem;
        color: #cbd5e1;
    }

    /* --- TARJETAS PASO A PASO --- */
    .step-card {
        background: #ffffff;
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .step-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }

    .step-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .step-title {
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.4rem;
        font-size: 1rem;
    }

    .step-desc {
        color: #64748b;
        font-size: 0.875rem;
        line-height: 1.4;
    }

    /* --- TABS & UPLOADER --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #e2e8f0;
        padding: 6px;
        border-radius: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
        color: #475569;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: var(--primary) !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* --- BOTONES PRINCIPALES --- */
    .stButton > button {
        border-radius: 12px;
        background: var(--primary-gradient);
        color: #ffffff !important;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        opacity: 0.95;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
    }

    /* --- SIDEBAR --- */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid var(--border-color);
    }

    .footer-text {
        text-align: center;
        color: var(--text-muted);
        font-size: 0.85rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def clean_filename(text):
    filename = text[:30].strip()
    if not filename:
        filename = "translation"
    filename = "".join(
        c for c in filename if c.isalnum() or c in (" ", "_", "-")
    ).replace(" ", "_")
    return filename or "translation"


def remove_old_files(days=7):
    files = glob.glob(os.path.join(TEMP_FOLDER, "*.mp3"))
    current_time = time.time()
    maximum_age = days * 86400

    for file in files:
        try:
            if os.stat(file).st_mtime < current_time - maximum_age:
                os.remove(file)
        except Exception:
            pass


def extract_text_from_image(image_bytes, tesseract_language, use_filter=False):
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        return "", None

    original_image = image.copy()

    if use_filter:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    try:
        detected_text = pytesseract.image_to_string(image, lang=tesseract_language)
    except Exception:
        try:
            detected_text = pytesseract.image_to_string(image, lang="eng")
        except Exception:
            detected_text = ""

    return detected_text.strip(), original_image


def translate_and_create_audio(source_language, destination_language, text, tld):
    translation = translator.translate(
        text, src=source_language, dest=destination_language
    )
    translated_text = translation.text
    filename = clean_filename(translated_text)
    audio_path = os.path.join(TEMP_FOLDER, filename + ".mp3")

    speech = gTTS(
        text=translated_text,
        lang=destination_language,
        tld=tld,
        slow=False
    )
    speech.save(audio_path)

    return audio_path, translated_text


remove_old_files(7)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🌎 EasyTranslate</div>
        <div class="hero-subtitle">Traduce imágenes, carteles y documentos en segundos</div>
        <div class="hero-badge">Desarrollado por <b>Juan Pablo López Gallego</b></div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR (CONFIGURACIÓN)
# ============================================================

with st.sidebar:
    st.header("⚙️ Configuración")
    st.caption("Ajusta los parámetros de lectura y voz")
    st.divider()

    st.markdown("### 🌐 Idiomas")
    
    input_language_name = st.selectbox(
        "Idioma de la imagen",
        LANGUAGE_LIST,
        index=st.session_state.get("input_index", 0),
        key="input_language_select"
    )

    output_language_name = st.selectbox(
        "Idioma a traducir",
        LANGUAGE_LIST,
        index=st.session_state.get("output_index", 1),
        key="output_language_select"
    )

    if st.button("⇄ Intercambiar idiomas", use_container_width=True):
        input_index = LANGUAGE_LIST.index(input_language_name)
        output_index = LANGUAGE_LIST.index(output_language_name)
        st.session_state["input_index"] = output_index
        st.session_state["output_index"] = input_index
        st.rerun()

    input_language = LANGUAGES[input_language_name]["translation"]
    tesseract_language = LANGUAGES[input_language_name]["tesseract"]
    output_language = LANGUAGES[output_language_name]["translation"]

    st.divider()

    st.markdown("### 🔊 Salida de Voz")
    accent_name = st.selectbox("Acento de voz", list(ACCENTS.keys()))
    tld = ACCENTS[accent_name]

    st.divider()

    st.markdown("### 🛠️ Opciones Avanzadas")
    use_filter = st.checkbox("Mejorar contraste de imagen (OCR)", value=False)
    show_translation = st.checkbox("Mostrar texto traducido", value=True)

    st.info("💡 **Consejo:** Asegúrate de que el texto en la foto tenga buena iluminación.")


# ============================================================
# SECCIÓN: CÓMO FUNCIONA
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">📸</div>
            <div class="step-title">1. Captura</div>
            <div class="step-desc">Sube una imagen o toma una fotografía instantánea con la cámara.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">🔍</div>
            <div class="step-title">2. Detecta</div>
            <div class="step-desc">El sistema reconoce el texto automáticamente para que puedas editarlo.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">🔊</div>
            <div class="step-title">3. Escucha</div>
            <div class="step-desc">Obtén la traducción exacta en texto y escúchala con pronunciación nativa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")


# ============================================================
# SECCIÓN: CAPTURA DE IMAGEN (TABS)
# ============================================================

st.subheader("📸 Selecciona el origen de la imagen")

tab_upload, tab_camera = st.tabs(["📁 Subir Imagen desde el equipo", "📷 Usar Cámara Web"])

image_bytes = None

with tab_upload:
    uploaded_image = st.file_uploader(
        "Arrastra o selecciona una imagen",
        type=["png", "jpg", "jpeg", "webp"],
        label_visibility="collapsed"
    )
    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()

with tab_camera:
    camera_image = st.camera_input("Toma una fotografía directamente", label_visibility="collapsed")
    if camera_image is not None:
        image_bytes = camera_image.getvalue()


# ============================================================
# PROCESAMIENTO OCR Y RESULTADOS
# ============================================================

detected_text = ""

if image_bytes is not None:
    st.divider()
    col_img, col_txt = st.columns([1, 1], gap="large")

    with col_img:
        st.subheader("🖼️ Imagen Cargada")
        st.image(image_bytes, use_container_width=True)

    with col_txt:
        st.subheader("📝 Texto Detectado")
        with st.spinner("🔍 Analizando y extrayendo texto..."):
            detected_text, _ = extract_text_from_image(
                image_bytes, tesseract_language, use_filter
            )

        if detected_text:
            edited_text = st.text_area(
                "Puedes editar el texto detectado antes de traducir:",
                value=detected_text,
                height=180
            )
        else:
            st.warning("⚠️ No se detectó texto legible. Intenta con otra imagen o activa el filtro de contraste en la barra lateral.")
            edited_text = ""

    # SECCIÓN DE TRADUCCIÓN
    if edited_text.strip():
        st.divider()
        st.subheader("🌐 Traducción")
        st.caption(f"Traduciendo de **{input_language_name}** a **{output_language_name}**")

        if st.button("🚀 Traducir y Generar Audio", use_container_width=True):
            try:
                with st.spinner("✨ Traduciendo texto y generando audio..."):
                    audio_path, translated_text = translate_and_create_audio(
                        input_language, output_language, edited_text, tld
                    )

                res_col1, res_col2 = st.columns([2, 1], gap="medium")

                with res_col1:
                    if show_translation:
                        st.markdown("#### 💬 Resultado:")
                        st.success(translated_text)

                with res_col2:
                    st.markdown("#### 🔊 Reproducir:")
                    with open(audio_path, "rb") as audio_file:
                        st.audio(audio_file.read(), format="audio/mp3")

            except Exception as error:
                st.error("❌ Ocurrió un error al realizar la traducción.")
                st.caption(f"Detalle del error: {error}")


# ============================================================
# DESPLEGABLE DE IDIOMAS Y FOOTER
# ============================================================

st.divider()

with st.expander("🌍 Ver lista completa de idiomas soportados", expanded=False):
    st.write(f"Soportamos un total de **{len(LANGUAGE_LIST)} idiomas** para extracción de texto y traducción:")
    lang_cols = st.columns(4)
    for index, lang in enumerate(LANGUAGE_LIST):
        with lang_cols[index % 4]:
            st.write(lang)

st.markdown(
    """
    <div class="footer-text">
        EasyTranslate &copy; 2026 &bull; Diseñado con Streamlit por <b>Juan Pablo López Gallego</b>
    </div>
    """,
    unsafe_allow_html=True
)
