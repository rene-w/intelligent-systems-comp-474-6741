#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:53:26 2024

@author: rene
Note: You need to download the glove.6B.50d.txt from
https://nlp.stanford.edu/projects/glove/
"""
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

texts = [
    'Google search engine',  
    'Apple mobile devices', 
    'delicious Pizza food', 
    'tasty Burger meal', 
    'Python programming language',
    'Italian Pasta dish' 
]
labels = [0, 0, 1, 1, 0, 1]  # 0 for Technology, 1 for Food

embeddings_index = {}
with open('glove.6B.50d.txt', 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = vector

def get_average_vector(text):
    # Split the text into words
    words = text.split()
    # Retrieve vectors for each word and calculate the average
    vectors = np.array([embeddings_index.get(word.lower(), np.zeros(50)) for word in words])
    if len(vectors) == 0:
        return np.zeros(50)  # Return an all-zero vector if there are no words
    return np.mean(vectors, axis=0)

def get_vector(text):
    return embeddings_index.get(text.lower(), np.zeros(50))  # 50-dimensional vectors

X_train = np.array([get_average_vector(text) for text in texts])


model = Sequential([
    Dense(32, activation='relu', input_dim=50),  # Input layer matches vector size
    Dense(1, activation='sigmoid')  # Binary output
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, np.array(labels), epochs=30, verbose=1)

new_texts = ['I like Spaghetti', 'Tesla makes electric cars']
new_X = np.array([get_average_vector(text) for text in new_texts])

predictions = model.predict(new_X)
print(predictions)  # Closer to 0 indicates Technology, closer to 1 indicates Food
