from __future__ import print_function
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from src.config import configuration


def find_similar(tfidf_matrix, index, top_n=5):
    cosine_similarities = linear_kernel(tfidf_matrix[index:index + 1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]


file_path = configuration.FILE_PATH_EXAMPLE_CONTENT  # Path of example data for content algorithms
corpus = []  # Matrix to get all the values from the CSV

# Getting cols what I need form the CSV
df = pd.read_csv(file_path, encoding='utf-8')  # It'll replace with Wordpress Data
docs = list(df.abstract)  # provide list of abstracts, It'll replace with the tags
titles = list(df.title)  # titles
var = df.values  # CSV to Array

i = 0
while i < titles.__len__():
    if titles[i] and docs[i]:
        corpus.append((titles[i], docs[i]))
        # corpus.append((docs[i], titles[i]))
        doc = docs[i]
        title = titles[i]
        # print ("- ", doc)
        i += 1

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform([content for file, content in corpus])

doc = 10  # Doc to compare

print ("\nDocumentos recomendados con TIF-IDF y Coseno de Similitud a partir del titulo:")
print ("'", corpus[doc][0], "'\n")
for index, score in find_similar(tfidf_matrix, doc):
    print ("- ", score, corpus[index][0])
