# Few Shot prompting
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

# Definimos el contexto con ejemplos (Few-Shot)
# Esto enseña al modelo a responder en un formato muy específico
texto = """ 
    Eres un traductor de lenguaje natural a comandos SQL.
    
    Ejemplo 1:
    Usuario: "Dame todos los usuarios de Bogotá"
    Salida: SELECT * FROM usuarios WHERE ciudad = 'Bogotá';
    
    Ejemplo 2:
    Usuario: "Cuenta cuántos productos cuestan más de 100"
    Salida: SELECT COUNT(*) FROM productos WHERE precio > 100;
    
    Ejemplo 3:
    Usuario: "Lista los nombres de empleados contratados en 2023"
    Salida: SELECT nombre FROM empleados WHERE fecha_contratacion >= '2023-01-01';
    
    Ahora responde a la siguiente petición: 
    """
    
peticion_usuario = 'Usuario: "Busca el correo de la persona llamada Juan Perez"'
        


# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=texto + peticion_usuario
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print("-" * 30)
    print(response.text)
    
  