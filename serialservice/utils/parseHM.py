from rdflib import ConjunctiveGraph
g = ConjunctiveGraph()
g.parse('../data/hm_17_1.rss')
#len(g)
import sys
sys.path.append('../')
from model.namespaces import *
from model.bibo import Article

from rdfalchemy import rdfSubject

nsm = g._get_namespace_manager()
nsm.bind('prism', 'http:prism.com') 
print g.serialize()
#PRISM2 = Namespace('http://prismstandard.org/namespaces/basic/2.0/')
for s, p, o in g.triples((None, RDF.type, RSS.item)):
    g.add((s, p, BIBO.Article))
    g.remove((s, p, o))



rdfSubject.db = g

l = list(Article.ClassInstances())
a = l[1]
print a.title
print a.creators
print a.sPg
