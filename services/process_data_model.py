import gensim
import nltk
import json
import unicodedata
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

nltk.download('punkt')
text_file = open("files/clean_data/texto_depresion_kaplan_preprocesado.txt", "r", encoding="utf-8") 
sentences = nltk.sent_tokenize(text_file.read())
words = [nltk.word_tokenize(sentence) for sentence in sentences]
print('words',words)
dictionary = gensim.corpora.Dictionary(words)
corpus = [dictionary.doc2bow(word, allow_update=True) for word in words]
print('corpus', corpus)
lda_model = gensim.models.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=10)
print('lda_model', lda_model.print_topics()) 


print('-----------------')

# Cargar los datos desde el archivo JSON
# Cargar los datos desde el archivo JSON
with open("datos_depresion_procesado.json", "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

# Separar los textos y categorías del diccionario cargado
textos = data["textos"]
categorias = [texto["categoria"] for texto in textos]
textos = [texto["texto"] for texto in textos]

# Crear un vectorizador y ajustarlo a los textos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

# Entrenar un clasificador Naive Bayes
clf = MultinomialNB()
clf.fit(X, categorias)

# Textos de prueba
test_texts = ["Sentimientos de tristeza, ganas de llorar, vacío o desesperanza. Arrebatos de enojo, irritabilidad o frustración, incluso por asuntos de poca importancia.",
              "Es causada por una combinación de factores genéticos, biológicos, ambientales y psicológicos.",
              "LLa depresión es una enfermedad que se caracteriza por una tristeza persistente y por la pérdida de interés en las actividades",
              "Los antidepresivos son medicamentos que se dirigen a los desequilibrios qu ayudan  a mejorar el estado de ánimo, el sueño, el apetito y la concentración. También pueden reducir los sentimientos de ansiedad, de culpa y de desesperanza."
            ]

# Transformar los textos de prueba
test_X = vectorizer.transform(test_texts)

# Predecir categorías para los textos de prueba
test_categories = clf.predict(test_X)
print(test_categories)

# Calcular la precisión en función de las categorías reales
accuracy = accuracy_score(categorias, clf.predict(X))
print(f"Precisión del modelo: {accuracy}")

user_question = "Explicame que es la depresion"
user_question_X = vectorizer.transform([user_question])
predicted_category = clf.predict(user_question_X)[0]
print(f"La pregunta pertenece a la categoría {predicted_category}")
