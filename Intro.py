import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Mi primera página web en streamlit")
 image = Image.open('Primera.PNG')
 st.image(image, width=190)
 st.write("Primer trabajo realizado en streamlit") 
 url = "https://miprimerapagina-5gzdhzssqjm77bzqcehwe5.streamlit.app/"
 st.write(f"Mi primera página: [Enlace]({url})")

 st.subheader("OCR")
 image = Image.open('OCD.PNG')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan textos en Imágenes.") 
 url = "https://reconocertextojplg-6juwyccehm7tzvrc4olrgc.streamlit.app/#lector-de-texto"
 st.write(f"OCR: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de texto a voz")
 image = Image.open('Voxlab.PNG')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de texto a voz") 
 url = "https://imm1copiajplg-zdpnlzjgnlatk4cbll7wlj.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("OCR + Texto a audio")
 image = Image.open('OCRTraductor.PNG')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como esta aplicación detecta textos en imágenes, traduce, y finalmente genera texto y audio") 
 url = "https://traductorextranjeros-jk7eekmjpdskckeba6x8mk.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Voz a texto")
 image = Image.open('VoxTranslate.PNG')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que escucha lo que dices, lo traduce y lo convierte en texto") 
 url = "https://traductorjplg-9zcgnf8wypri8t5yksyfsg.streamlit.app/"
 st.write(f"Voz a texto [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

