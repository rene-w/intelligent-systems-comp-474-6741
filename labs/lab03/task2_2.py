from rdflib import Graph, Literal, RDF, Namespace
from rdflib.namespace import FOAF, RDFS

g = Graph()

# Add the namespace for known prefixes to the graph
g.bind("foaf", FOAF)
g.bind("rdfs", RDFS)
g.bind("rdf", RDF)

# Command to create user defined namespaces
user = Namespace("http://example.org/")
g.bind("user", user)

# Command to add triples to graph for Joe
g.add((user.joe, RDF.type, FOAF.Person))
g.add((user.joe, FOAF.knows, user.jane))
g.add((user.joe, RDFS.label, Literal("Joe")))


# Print the graph, serialized in a specific format
print(g.serialize(format='turtle'))
