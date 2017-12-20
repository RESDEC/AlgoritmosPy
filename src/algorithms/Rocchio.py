from __future__ import print_function
import pandas as pd

from science_concierge.science_concierge import ScienceConcierge
from src.config import configuration

file_path = configuration.FILE_PATH_EXAMPLE_CONTENT  # Path of example data for content algorithms
df = pd.read_csv(file_path, encoding='utf-8')
docs = list(df.abstract)  # provide list of abstracts
titles = list(df.title)  # titles
# select weighting from 'count', 'tfidf', or 'entropy'
recommend_model = ScienceConcierge(stemming=True, ngram_range=(1, 1),
                                   weighting='entropy',
                                   norm=None,
                                   n_components=100, n_recommend=100,
                                   verbose=True)

recommend_model.fit(docs)  # input list of documents or abstracts
index = recommend_model.recommend(likes=[100],
                                  dislikes=[])  # input list of like/dislike index (here we like title[10000])
docs_recommend = [titles[i] for i in index[0:10]]  # recommended documents

print ("Documentos recomendados a partir de las especificaciones de Rocchio:\n")
for d in docs_recommend:
    print ("- " + d)
