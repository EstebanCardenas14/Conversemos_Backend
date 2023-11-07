import fitz
import tabula
import camelot
import pandas as pd


file_path = 'files/pdfs/dsm5-manualdiagnsticoyestadisticodelostrastornosmentales-161006005112.pdf'
pdf = fitz.open(file_path)
page_number = 205
page_number2 = 238
text = ""
for page in range(page_number, page_number2):
    page3 = pdf[page]
    text += page3.get_text()



# Guardar el texto en un archivo
with open('files/extract_data/texto_dsm5.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)