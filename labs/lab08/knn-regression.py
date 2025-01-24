# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:43:19 2021

@author: Reethu Navale
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

dataset = np.array([[135,0,5,3],[90,123,2,5],[159,2,1,1]])
#print(X.shape)

X = dataset[:,0:3]
print(X)

# Encode labels: 0="Location", 1="Definition"
y = dataset[:, 3]
print(y)

clf = KNeighborsRegressor(2)
clf.fit(X, y)

predict = clf.predict([[109,5,3]])
print('Predicted rating = ', predict)
