import openai
import pandas as pd
import os

# Leemos el archivo CSV que subimos al entorno de Colab(el encoding que me ha funcionado es Latin pero se puede probar con utf-8)

#df = pd.read_csv('diplomados_edicion.csv', encoding='latin-1')
#df = pd.read_csv('question.csv', encoding='utf-8')

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Configurar la clave de API de OpenAI
openai.api_key = os.getenv('API_GPT_KEY')

#Keyword semilla
keyword= "diplomatura marketing digital"

#for i, row in df.iterrows():
    #question = row["title"]
    #messages.append({"role": "user", "content": question})


prompt = f"""Crea la estructura de un artículo para un blog especializado en cursos de marketing digital. 
El artículo debe seguir esta estructura:

- URL:
- Palabra clave (Keyword):
- Título principal (H1):
- Subtítulo (H2):
- Subtítulo (H2):
- Subtítulo (H2):
- Subtítulo (H2):
- Subtítulo (H2):

Asegúrate de que el contenido del artículo sea coherente y relevante para la palabra clave "{keyword}". 
Proporciona información valiosa y útil para los lectores. Evita incluir conclusiones en este paso, solo estructura el artículo.
"""

try:
  response = openai.ChatCompletion.create(
    #model="gpt-3.5-turbo-16k",
    model="gpt-4",
    messages=[
    { "role": "system", "content": "Eres un experto copywritter. Tu tarea es crear las estructuras de articulos para blog segun las indicaciones de {response}" },
    { "role": "user", "content": prompt} ],
    max_tokens=3000,
    temperature=0.5,
    n=1,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
except Exception as e:
  print("Error al realizar la solicitud a la API de OpenAI:", str(e))
  exit()

# Obtener el resultado del proceso
result = response['choices'][0]['message']['content']

# Crear un archivo de texto y guardar el resultado (.txt)
#with open('resultante.txt', 'w', encoding='utf-8') as file:
 #   file.write(result.replace('\n', ''))
#print("Proceso completado. El resultado se ha guardado en 'resultante.txt'.")

# Almacena el resultado en una variable
generated_prompt = result.replace('\n', '')

# Imprime el resultado
print("Resultado:")
print(generated_prompt)