#WERKT NIET

from rdfalchemy import rdfSubject
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph

import sys
sys.path.append('../')                          
from model.bibo import Article, Issue, Periodical

graph = rdfSubject.db = ConjunctiveGraph()
graph.parse('../data/capitalclass97.ttl', format="n3")
print(len(graph)) #84 triples

mapper()

a = Article()
for article in a.ClassInstances():
    print a.title
    print a.resUri
    #print '\t', a.title # werkt niet
    #print '\t', a.summary[1:10], '...'
    #for c
