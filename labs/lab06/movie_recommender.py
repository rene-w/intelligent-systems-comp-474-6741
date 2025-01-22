#!/usr/bin/env python3
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# helper functions
def getMovieIdx(title):
    return movietags.loc[movietags['title']==title].index[0]
def getMovieTitle(id):
    return movietags[movietags.index == id]["title"].values[0]

# read the movie & tag files
movies = pd.read_csv("ml-latest-small/movies.csv",header=0)
tags = pd.read_csv("ml-latest-small/tags.csv",header=0,na_filter=False)

# group the tags by movie
groupedtags = tags.groupby(["movieId"])['tag'].apply(','.join).reset_index()
# merge the movie and tag dataframes
movietags = pd.merge(movies, groupedtags, on='movieId', how='inner')

# create the feature vectors, using a simple tag count
cv = CountVectorizer()
count_matrix = cv.fit_transform(movietags['tag']) 

# compute the cosine similarity
similarity_scores = cosine_similarity(count_matrix)

# start recommending something
movieTitle = 'Toy Story (1995)'
movieId = getMovieIdx(movieTitle)
similar_movies = list(enumerate(similarity_scores[movieId]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

i=0
print("Top 5 similar movies to "+movieTitle+" are:\n")
for movie in sorted_similar_movies:
    if movie[1] > 0.1:
        print("{0}. {1} ({2:2.2f})".format(i+1, getMovieTitle(movie[0]), movie[1]))
    i=i+1
    if i>=5:
        break
