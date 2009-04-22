#! /usr/bin/env python

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace, Literal, BNode, URIRef

BIBO = Namespace('http://purl.org/ontology/bibo/')
DC = Namespace('http://purl.org/dc/elements/1.1/')
OV = Namespace('http://open.vocab.org/terms/')
PRISM = Namespace('http://prismstandard.org/namespaces/basic/2.0/')
RDFS =  Namespace('http://www.w3.org/2000/01/rdf-schema#')
FOAF = Namespace('http://xmlns.com/foaf/0.1/')

class Periodical(rdfSubject):
    rdf_type = BIBO.Periodical
    title = rdfSingle(DC['title'])
    issn = rdfSingle(BIBO.issn)
    #publisher = rdfSingle(DC.publisher)
    #publisher = rdfSingle(DC.publisher,range_type=FOAF.Organization)
    #label = rdfSingle(RDFS.label)
    #issues = rdfMultiple(

class Issue(rdfSubject):
    rdf_type = BIBO.Issue
    number = rdfSingle(PRISM.number)
    periodical = rdfSingle(DC.isPartOf, range_type=BIBO.Periodical)

class Article(rdfSubject):
    rdf_type = BIBO.Article
    title = rdfSingle(DC['title'])
    creators = rdfMultiple(DC.creator)
    summary = rdfSingle(DC.summary)
    sPg = rdfSingle(PRISM.startingPage)
    ePg = rdfSingle(PRISM.endingPage)
    #auStr = rdfSingle(OV.authorString)
    issue = rdfSingle(DC.isPartOf, range_type=BIBO.Issue)

#class Journal(Periodical):
#    rdf_type = BIBO.Journal

graph = rdfSubject.db = ConjunctiveGraph()
graph.parse('/home/maarten/workdir/serialservice/data/capitalclass97.ttl', format="n3")


mapper()

a = Article()
for article in a.ClassInstances():
    if article.title != None:
        print article.title
        print '\t', 'By', ' and '.join(article.creators)
        #for c in article.creators:
        #    print "\t", "Author;", c 
        print '\t', article.summary[0:30], '...'
        print '\t', 'Pages', '-'.join([str(article.sPg), str(article.ePg)])
        print '\t', article.issue[DC.isPartOf][DC.title], article.issue.number #periodical link werkt niet...
        print '\n'

j = Periodical.get_by(issn="0309-8168")
print j.title

