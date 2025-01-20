# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:52:29 2021

@author: Reethu Navale
"""

import rdflib
from prettytable import PrettyTable #Used for printing in table form

g = rdflib.Graph()

g.parse("Lab3_Task3.rdf")


########### SPARQL query - List all students, sorted by age
q1 = g.query(
    """SELECT ?name ?age
      WHERE {
          ?student rdf:type focu:Student ;
          foaf:age ?age ;
          foaf:givenName ?name .
       } ORDER BY ?age""" )

print("Question 1 : List all students, sorted by age")
t1 = PrettyTable(['Student Name', 'Age'])
for row in q1:
    t1.add_row([row[0],row[1]])
print(t1)

########### SPARQL query - Find all predicates and objects for a given student
name = "Joe" #You can also have input from the user
q2 = g.query(
        f"""
        SELECT ?p ?o
        WHERE {{
        ?student rdf:type focu:Student ;
        foaf:givenName '{name}' .
        ?student ?p ?o .
        }}
        """
        )

print("\nQuestion 2: Find all predicates and objects for a given student")
t2 = PrettyTable(['Predicate', 'Object'])
t2.align['Predicate'] = "l"
t2.align['Object'] = "l"
for row in q2:
    t2.add_row([row[0],row[1]])
print(t2)


########### SPARQL query - Print a count of all students by university
q3 = g.query(
        """
        SELECT ?uni (COUNT(?student) as ?count)
        WHERE {
        ?student rdf:type focu:Student ;
        focu:is_enrolled_at ?un .
        ?un rdfs:label ?uni .
        } GROUP BY ?un
        """
        )

print("\nQuestion 3: Print a count of all students by university")
t3 = PrettyTable(['University name', 'Count of Students'])
t3.align['University name'] = "l"
t3.align['Count of Students'] = "l"
for row in q3:
    t3.add_row([row[0],row[1]])
print(t3)

########### 
    
info = input('Hello, I am your smart university agent. Who are you looking for?')

q4 = g.query(
        f"""
        SELECT ?age ?uni
        WHERE {{
        ?student rdf:type focu:Student ;
        foaf:givenName '{info}' ;
        foaf:age ?age ;
        focu:is_enrolled_at ?u .
        ?u rdfs:label ?uni .
        }}
        """
        )

for i in q4:
    print(info + " is %s years old and studies at %s."%i)
