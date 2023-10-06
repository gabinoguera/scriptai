import openai
import os
from script_estructura_articulos_v2 import generated_prompt

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Configurar la clave de API de OpenAI
openai.api_key = os.getenv('API_GPT_KEY')

prompt = f"""Escribe un artículo para el blog siguiendo la estructura proporcionada: {generated_prompt}.
Hazlo de manera atractiva, dinámica y que capture la atención de los usuarios interesados en buscar su próxima carrera universitaria.
Asegúrate de incluir fuentes de información relevantes y confiables.
No inventes información; respalda tus afirmaciones con datos históricos o estadísticos verificables.
Incluye etiquetas HTML en tu respuesta 
"""

try:
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    #model="gpt-4",
    messages=[
        {"role": "system", "content": "Eres copywritter profesional especializado en educación"},
        {"role": "user", "content": prompt}],
        max_tokens=12000,
        temperature=0.3,
        n=1,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
  )
except Exception as e:
  print("Error al realizar la solicitud a la API de OpenAI:", str(e))
  exit()

# Establecer el cuerpo de la solicitud con el título y el estado del post(en este caso lo verás en "draft" pero puedes cambiarlo si lo prefieres a "publish" para su publicación automática)
data = {
    'title': "<H1></H1>",
    'content': response['choices'][0]['message']['content'],
    'status': 'draft'
}

# Guardar el contenido de 'data' en un archivo de texto
with open('resultante.txt', 'w', encoding='utf-8') as file:
    file.write(data['content'])

print("Proceso completado. El resultado se ha guardado en 'resultante.txt'.")



# Verificar el estado de la respuesta
#if response.status_code == 201:
 #   print('Post creado correctamente')
#else:
#    print('Error al crear el post')
