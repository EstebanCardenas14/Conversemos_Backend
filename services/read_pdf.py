import PyPDF2
from googletrans import Translator
import nltk
import re


# Abre el archivo PDF
with open('C:\\Users\\crist\\Downloads\\2022_KAPLAN_SYNOPSIS OF PSYCHIATRY.pdf', 'rb') as pdf_file:
    # Crea un objeto PdfReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Inicializa una variable para almacenar el texto relevante
    texto_relevante = ""
    inicio = 21
    fin = len(pdf_reader.pages) - 331
    page_text = "" 
    
    # Recorre las páginas del PDF
    for page_num in range(inicio, fin):
        # Extrae el texto de la página actual
        page = pdf_reader.pages[page_num]
        page_text += page.extract_text()

        patron = r"(?i)depression|depressive disorders|depressives(\w+)"
        secciones = re.split(patron, page_text)

        # Verifica si la página contiene información sobre la depresión
        #if page_text.lower().find("depression") !=1 or page_text.lower().find("Depressive Disorders") !=1 or page_text.lower().find("depressive disorders") !=1 or page_text.lower().find("depressives") != 1:
        #texto_relevante += page_text  # Agrega el texto de la página actual

    secciones_filtradas = []
    for seccion in secciones:
        if seccion is not None:
            secciones_filtradas.append(seccion)


    corpus = nltk.TextCollection(secciones_filtradas)

# Guarda el texto relevante en un archivo de salida
#with open('texto_depresion_kaplan.txt', 'w', encoding='utf-8') as output_file:
#    output_file.write(texto_relevante)

with open('corpus_depresion_kaplan.txt', 'w', encoding='utf-8') as output_file:
    for seccion in corpus:
       output_file.write(seccion + "\n")
    
