# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:33:46 2021

@author: Reethu Navale
"""
import requests
from prettytable import PrettyTable

#SPARQL printing the subject, predicate and object
query_var = 'SELECT ?subject ?predicate ?object WHERE { ?subject ?predicate ?object} LIMIT 25'

#Using the post method to query on Apache Fuseki Server
#Make sure you give the right IP and port address details correctly and the server should be running
#Here Lab4_Demo is the dataset name which I have created and uploaded my knowlegde graph
response = requests.post('http://localhost:3030/Lab4_Demo/sparql',
       data={'query': query_var})

res = response.json()
#Prints the response of the SPARQL query
print(res)

#Lets try printing the values from the json output
print("\nPrinting the values of subject predicate and object")
'''
print("---------------------------------------------------------------")
for row in res['results']['bindings']:
    print("Subject: ",row['subject']['value'])
    print("Predicate: ",row['predicate']['value'])
    print("Object: ",row['object']['value'])
    print("")
'''
t = PrettyTable(['Subject', 'Predicate','Object'])
t.align['Subject'] = "l"
t.align['Predicate'] = "l"
t.align['Object'] = "l"
for row in res['results']['bindings']:
    t.add_row([row['subject']['value'],row['predicate']['value'],row['object']['value']])
print(t)