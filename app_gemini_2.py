import os
from google import genai
from google.genai import types
from dotenv import load_dotenv




# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")


# 2. Inicializar el cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

texto = """ 
        Cliente: Hola, tengo un problema con mi pedido. No llegó a tiempo y necesito una solución.
        Agente nivel 1: Lamento escuchar eso. ¿Podría proporcionarme su número de pedido para que pueda verificarlo?
        Cliente: Sí, mi número de pedido es 12345.
        Agente nivel 1: Gracias por la información. Permítame revisar el estado de su pedido.
        Agente nivel 1: He verificado su pedido y veo que hubo un retraso en el envío. Lamento mucho la inconveniencia.
        Agente nivel 1: ¿Le gustaría que le ofrezca un reembolso o un nuevo envío sin costo adicional?
        Cliente: Preferiría un nuevo envío, por favor.
        """

prompt = f"""Resume la conversación entre el Cliente y el Agente nivel 1 en cuatro puntos claves: {texto}"""

configuracion = types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=300
)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")

    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=configuracion
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")


if __name__ == "__main__":
    ejecutar_consulta()
