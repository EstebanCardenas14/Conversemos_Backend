import re
import nltk
from nltk.tokenize import sent_tokenize

# Descargar recursos necesarios si no están instalados
nltk.download('punkt')

with open('files/extract_data/texto_dsm5.txt', 'r', encoding='utf-8') as input_file:
    texto = input_file.read()

secciones = re.split(r'(\n[^\n:]+:)', texto)
secciones = [seccion.strip() for seccion in secciones if seccion.strip()]

# Imprimimos las secciones
for seccion in secciones:
    print(seccion)

# Dividir el texto en párrafos usando líneas en blanco como separadores
parrafos = re.split(r'\n\s*\n', texto)

# Inicializar una lista para almacenar los párrafos procesados
parrafos_procesados = []

for parrafo in parrafos:
    # Agregar un punto final al final del párrafo si no está presente
    if not parrafo.strip().endswith('.'):
        parrafo += '.'

    # Tokenizar el párrafo en oraciones
    oraciones = sent_tokenize(parrafo)

    # Inicializar una lista para almacenar las oraciones procesadas
    oraciones_procesadas = []

    for oracion in oraciones:
        # Tokenizar la oración en palabras
        palabras = nltk.word_tokenize(oracion)

        # Limpiar y preprocesar las palabras (eliminar caracteres no alfabéticos y dígitos)
        palabras_procesadas = [palabra for palabra in palabras if palabra.isalpha()]

        # Unir las palabras nuevamente en una oración procesada
        oracion_procesada = ' '.join(palabras_procesadas)
        oraciones_procesadas.append(oracion_procesada)

    # Unir las oraciones procesadas en un párrafo procesado
    parrafo_procesado = ' '.join(oraciones_procesadas)
    parrafos_procesados.append(parrafo_procesado)

# Unir los párrafos procesados en un solo texto
texto_procesado = '\n\n'.join(parrafos_procesados)

# Guardar el texto procesado en un nuevo archivo
with open('files/clean_data/texto_dsm5_preprocesado.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(texto_procesado)
