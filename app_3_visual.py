import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Configuración de la página (Título de la pestaña y el icono)
st.set_page_config(page_title="Generador de Blogs IA", page_icon="✍️")

# 2. Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Título principal en la interfaz
st.title("🤖 Asistente de Redacción con Gemini")
st.markdown("Escribe un tema y la IA generará un artículo de blog por ti.")

# 3. Verificación de API Key
if not API_KEY:
    st.error("❌ No se encontró la API Key en el archivo .env")
    st.stop()

# 4. Inicializar cliente (se usa caché para no reconectar en cada clic)
@st.cache_resource
def get_client():
    return genai.Client(api_key=API_KEY)

client = get_client()

# 5. Configuración del modelo (System Instruction)
configuration = types.GenerateContentConfig(
    max_output_tokens=3000,
    system_instruction="""
    Eres un asistente académico especializado en Inteligencia Artificial y redacción técnica.
    Responde de forma clara, concisa y bien estructurada con formato Markdown.
    """
)

# 6. Interfaz de Usuario
# Área de texto para que el usuario escriba
tema_usuario = st.text_area(
    "¿Sobre qué quieres escribir hoy?", 
    value="Las ventajas de usar microservicios",
    height=100
)

# Botón para ejecutar
if st.button("Generar Artículo 🚀"):
    if not tema_usuario:
        st.warning("Por favor escribe un tema primero.")
    else:
        # Spinner de carga mientras la IA piensa
        with st.spinner("Gemini está escribiendo tu artículo..."):
            try:
                prompt = f"Escribe una publicación de blog detallada sobre: {tema_usuario}"
                
                # Llamada al modelo
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    config=configuration,
                    contents=prompt
                )
                
                # Mostrar el resultado
                st.success("¡Artículo generado!")
                st.markdown("---") # Línea separadora
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")

# Pie de página
st.markdown("---")
st.caption("Desarrollado con Google Gemini y Streamlit")
