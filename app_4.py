"""
Taller Práctico: Prompt Engineering
Desarrollo de aplicaciones con IA
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# -------------------------------------------------
# Cargar variables de entorno
# -------------------------------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró la API Key en el archivo .env")

# -------------------------------------------------
# Inicializar cliente Gemini
# -------------------------------------------------
client = genai.Client(api_key=API_KEY)

configuration = types.GenerateContentConfig(
    max_output_tokens=3000,
    temperature=0.2,
    system_instruction="""
Eres un asistente académico experto en Prompt Engineering.
Sigue estrictamente las instrucciones dadas.
"""
)

# =================================================
# PARTE 1 – PROMPT MAESTRO
# =================================================
prompt_parte_1 = """
Rol: Eres un Gerente de Finanzas profesional, amable pero firme.

Tarea:
Redacta un correo electrónico solicitando el pago de una factura vencida.

Contexto:
El correo será enviado a un cliente corporativo con un pago atrasado.

Tono:
Profesional, respetuoso y claro.

Formato:
Finaliza el correo con una tabla que resuma los montos adeudados.

Delimitadores:
La información del cliente está delimitada por ###.

###
Cliente: Empresa ABC
Factura: 7894
Monto adeudado: $1.250.000 COP
Fecha de vencimiento: 10 de enero de 2026
###
"""

# =================================================
# PARTE 2 – PROMPT CONDICIONAL
# =================================================
prompt_parte_2 = '''
Contexto:
Eres un asistente de triaje de correos electrónicos de soporte.

Instrucciones:
Se te proporcionará un texto delimitado por """.

SI el texto contiene una queja sobre un pago o factura:
- Clasifícalo como "URGENTE-FINANZAS"
- Extrae el número de factura si existe

SI NO, si es una duda técnica general:
- Clasifícalo como "SOPORTE-ESTÁNDAR"
- Responde: "Gracias, un técnico lo revisará"

SI NO es ninguno de los anteriores:
- Responde: "Categoría no identificada"

Texto del usuario:
""" Hola, mi factura #4502 tiene un cargo doble que no reconozco. Ayuda. """
'''


# =================================================
# PARTE 3 – FEW-SHOT PROMPTING
# =================================================
prompt_parte_3 = """
Clasifica el sentimiento de la reseña.
Responde solo con una palabra: POSITIVO, NEUTRAL o NEGATIVO.

Ejemplos:

Reseña: "Una historia inspiradora, bien escrita y muy emotiva."
Respuesta: POSITIVO

Reseña: "El libro es correcto, sin grandes sorpresas."
Respuesta: NEUTRAL

Reseña: "La trama es confusa y aburrida."
Respuesta: NEGATIVO

Ahora clasifica:

Reseña: "Este libro empezó bien pero el final fue muy apresurado y decepcionante."
"""

# =================================================
# PARTE 4 – PROMPT EVALUADOR
# =================================================
prompt_parte_4 = """

Rol:
Eres un evaluador académico de ensayos universitarios.

Condiciones:
SI el ensayo tiene menos de 100 palabras:
- Recházalo y solicita más contenido.

SI tiene 100 palabras o más:
- Evalúa Ortografía, Coherencia y Argumentación.

Formato de salida:
Devuelve únicamente un objeto JSON con:
- nota_final
- comentarios

Ensayo:
La inteligencia artificial se ha convertido en una herramienta clave en la educación moderna.
Su capacidad para personalizar el aprendizaje permite que los estudiantes avancen a su propio ritmo.
Sin embargo, también plantea desafíos éticos relacionados con la dependencia tecnológica y la privacidad
de los datos. Es fundamental que las instituciones educativas adopten la IA de manera responsable,
combinando la innovación tecnológica con una sólida formación crítica.
Su capacidad para personalizar el aprendizaje permite que los estudiantes avancen a su propio ritmo,
adaptando los contenidos a sus necesidades específicas y fomentando una mayor retención del conocimiento.
Esto democratiza el acceso a la información de calidad y permite a los docentes enfocarse en mentorías.
Sin embargo, también plantea desafíos éticos significativos relacionados con la dependencia tecnológica
excesiva y la privacidad de los datos personales de los alumnos. Es fundamental que las instituciones
educativas adopten la IA de manera responsable, estableciendo marcos regulatorios claros y combinando
la innovación tecnológica con una sólida formación crítica y humanística para los futuros profesionales.
"""
# =================================================
# FUNCIÓN PARA EJECUTAR PROMPTS
# =================================================
def ejecutar_prompt(titulo, prompt):
    print(f"\n{'='*60}")
    print(titulo)
    print(f"{'='*60}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=configuration,
        contents=prompt
    )

    print(response.text)


# =================================================
# EJECUCIÓN
# =================================================
ejecutar_prompt("PARTE 1 – PROMPT MAESTRO", prompt_parte_1)
ejecutar_prompt("PARTE 2 – PROMPT CONDICIONAL", prompt_parte_2)
ejecutar_prompt("PARTE 3 – FEW-SHOT PROMPTING", prompt_parte_3)
ejecutar_prompt("PARTE 4 – EVALUADOR ACADÉMICO", prompt_parte_4)