import re 
import string 
import nltk

nltk.download('wordnet')
with open('corpus_depresion_kaplan.txt', 'r', encoding='utf-8') as input_file:
    texto = input_file.read()
    texto = texto.lower()
    ttranslator = str.maketrans('', '', string.punctuation)
    texto = re.sub('\d', '', texto)
    texto = re.sub('\s+', " ", texto)
    texto = re.sub('[áéíóúü]', lambda x: x.group(0).replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u'), texto)
    
    lematizador = nltk.stem.WordNetLemmatizer()
    texto = " ".join([lematizador.lemmatize(palabra) for palabra in texto.split()])
    with open('texto_depresion_kaplan_preprocesado_corpus.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(texto)

    


