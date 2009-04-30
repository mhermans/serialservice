from rdflib import ConjunctiveGraph
g = ConjunctiveGraph()
g.parse('hm_17_1.rss')
#len(g)
from rdflib import RDF
from rdflib import Namespace
RSS = Namespace("http://purl.org/rss/1.0/")
BIBO = Namespace("http://purl.org/ontology/bibo/")
PRISM1 = Namespace("http://prismstandard.org/namespaces/1.2/basic/")
nsm = g._get_namespace_manager()
nsm.bind('prism', 'http:prism.com') 
print g.serialize()
#PRISM2 = Namespace('http://prismstandard.org/namespaces/basic/2.0/')
for s, p, o in g.triples((None, RDF.type, RSS.item)):
    g.add((s, p, BIBO.Article))
    g.remove((s, p, o))


from rdfalchemy import rdfSubject

rdfSubject.db = g

import sys
sys.path.append('/home/maarten/workdir/serialservice/utils/')
from mapping import Article

l = list(Article.ClassInstances())
a = l[1]
print a.title
print a.creators
print a.sPg
