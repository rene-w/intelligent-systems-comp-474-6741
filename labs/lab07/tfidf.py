#!/usr/bin/env python3
# -*- coding: utf-8 -*-

documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# print the details
print("Vocabulary:\n", tfidf_vectorizer.get_feature_names())
print("Matrix shape: ", tfidf_matrix.shape)
print("Tf-idf vectors:\n", tfidf_matrix.toarray())
import pandas as pd
df_idf = pd.DataFrame(tfidf_vectorizer.idf_, index=tfidf_vectorizer.get_feature_names(),columns=["idf_weights"])
print("Idf weights:\n", df_idf.sort_values(by=['idf_weights']))

# compute the cosine similarity matrix
from sklearn.metrics.pairwise import cosine_similarity
similarity_scores = cosine_similarity(tfidf_matrix)
print("Cosine similarity matrix:\n", similarity_scores)

# search for the doc using cosine similarity
search_doc = "The dog is bright"
search_tfidf_vector = tfidf_vectorizer.transform([search_doc])
print("Search tf-idf vector: ", search_tfidf_vector.toarray())

similar_docs = cosine_similarity(search_tfidf_vector, tfidf_matrix)
print("Cosine search scores:", similar_docs)
