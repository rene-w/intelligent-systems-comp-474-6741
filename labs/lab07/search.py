#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

from sklearn.datasets import fetch_20newsgroups
cats = ['alt.atheism', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

from pprint import pprint
pprint(list(newsgroups_train.target_names))

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(newsgroups_train.data)
print(tfidf_matrix.shape)

# Search for the doc using cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
search_doc = "The dog is bright"
search_tfidf_vector = tfidf_vectorizer.transform([search_doc])
print("Search tf-idf vector: ", search_tfidf_vector.toarray())

similar_docs = cosine_similarity(search_tfidf_vector, tfidf_matrix)
print("Cosine search scores:", similar_docs)

# Get the row index of highest cosine similarity value
import numpy as np
index = np.where(similar_docs.T == np.max(similar_docs.T))
print(index[0])

# Print the document that has highest similar score to the query document 
print(newsgroups_train.data[int(index[0])])

# Sort the indexes based on similarity scores
ranking_document_index = sorted(range(len(similar_docs.T)),key=similar_docs.T.__getitem__, reverse=True)
print(ranking_document_index)

