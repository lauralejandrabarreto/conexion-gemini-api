import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv() # Load environment variables from .env fi
API_KEY = os.getenv("GENAI_API_KEY")
# Inicializar el cliente
client = genai.Client(api_key=API_KEY)
configuration = types.GenerateContentConfig(
 max_output_tokens=2048,
 system_instruction="""Eres un analista financiero qu
e reaiza predicciones sobre mercados financieros.
 Responde el valor de las acciones de empresas, oro,
plata, bitcoin, ethereum, etc. para los próximos 7 días.
Responde con un objeto JSON con el siguiente format
o:
{
 "predicciones": [
 {
 "activo": "Nombre del activo (ejemplo: 'Bitc
oin')",
 "prediccion": "Valor predicho para el día (e
jemplo: '45000 USD')",
 "fecha": "Fecha de la predicción (ejemplo:
'2024-07-01')"
 },
 {
 "activo": "Nombre del activo (ejemplo: 'Or
o')",
 "prediccion": "Valor predicho para el día (e
jemplo: '1900 USD')",
 "fecha": "Fecha de la predicción (ejemplo:
'2024-07-01')"
 }
 ]
}
 Tus respuestas deben ser siempre objetos JSON válido
s. No incluyas texto explicativo fuera del bloque de cód
igo.
"""
)
text = input("Escribe tu pregunta sobre mercados financieros: ")
response = client.models.generate_content(
 model="gemini-2.5-flash",
 config=configuration,
 contents=text
)
print(response.text)
