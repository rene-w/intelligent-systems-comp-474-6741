#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np 
from sklearn.cluster import KMeans

documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# use k-means to cluster the dataset
kmeans = KMeans(n_clusters=2)
kmeans.fit(tfidf_matrix)
print(kmeans.labels_)
