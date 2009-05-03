#! /usr/bin/env python


import urlparse

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple, rdfContainer
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Literal, BNode, URIRef
from namespaces import *

BASEURL = "http://localhost:5000" #XXX zet dit ergens in de config

class Periodical(rdfSubject):
    rdf_type = BIBO.Periodical
    title = rdfSingle(DC['title'])
    issn = rdfSingle(BIBO.issn)
    publisher = rdfSingle(DC['publisher'])
    shortTitle = rdfSingle(BIBO['shortTitle'])
    homepage = rdfSingle(FOAF.homepage)
    #publisher = rdfSingle(DC.publisher,range_type=FOAF.Organization)
    #label = rdfSingle(RDFS.label)
    #issues = rdfMultiple(

    @property
    def locUrl(self):
        return '/'.join([BASEURL, 'serials', self.shortTitle])

class Issue(rdfSubject):
    rdf_type = BIBO.Issue
    number = rdfSingle(PRISM.number)
    periodical = rdfSingle(DC.isPartOf, range_type=BIBO.Periodical)
    title = rdfSingle(DC['title'])
    pubdate = rdfSingle(DCTERMS.issued)
    volume = rdfSingle(PRISM.volume)
    coverImg = rdfSingle(FOAF.depiction)

    @property
    def locUrl(self):
        if not self.volume:
            v = "0"
        else:
            v = str(self.volume)

        n = str(self.number)

        return '/'.join([BASEURL, 'serials', self.periodical.shortTitle, v, n])
        
    #@property
    #def articles(self):
    #    """"Return the articles in this issue"""
        #for s, p, o in self.db.triples((None, None, None)):
        #    print s
   #     return list(self.db.subjects(predicate=DC.isPartOf, object=self.resUri))
        #return len(self.db)

    # zie http://groups.google.com/group/rdfalchemy-dev/browse_thread/thread/ad9363b7f1b275c2/92672eef06a8ac03

class Article(rdfSubject):
    rdf_type = BIBO.Article
    title = rdfSingle(DC['title'])
    creators = rdfMultiple(DC.creator)
    makers = rdfMultiple(FOAF.maker, range_type=FOAF.Person)
    abstract = rdfSingle(DCTERMS['abstract'])
    sPg = rdfSingle(PRISM.startingPage)
    ePg = rdfSingle(PRISM.endingPage)
    auStr = rdfSingle(OV.authorString)
    section = rdfSingle(PRISM.section)
    issue = rdfSingle(DC.isPartOf, range_type=BIBO.Issue)
    ivrs = rdfMultiple(BIBO.interviewer, range_type=FOAF.Person)
    ives = rdfMultiple(BIBO.interviewee, range_type=FOAF.Person)
    reviewOf = rdfMultiple(BIBO.reviewOf)

    def __lt__(self, other):
        if self.sPg < other.sPg:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.sPg > other.sPg:
            return True
        else:
            return False



#class ArticleInstance(rdfSubject)
#    accessRights

#class Journal(Periodical):
#    rdf_type = BIBO.Journal

class Book(rdfSubject):
    rdf_type = BIBO.Book
    title = rdfSingle(DC['title'])
    creators = rdfMultiple(DC.creator)
    publisher = rdfSingle(DC['publisher'])
    #publishinglocation of als property op publisher?
    pubdate = rdfSingle(DCTERMS.issued) # XXX data(time) object?
    isbn = rdfSingle(BIBO.isbn) #XXX maak IFP
    citation = rdfSingle(DCTERMS.bibliographicCitation)

#
#class Publisher
#    rdf_type = FOAF.Organization
#    name = rdfSingle(FOAF.name)
#    location = rdfSingle(ADR.localityName)

class Person(rdfSubject):
    rdf_type = FOAF.Person
    name = rdfSingle(FOAF.name)
    member = rdfMultiple(FOAF.member, range_type=FOAF.Group)

    #@property
    #def slug(self): #XXX define on __init__ ?
    #    return '-'.join(self.name.split()).lower()

    @property
    def locUrl(self):
        return '/'.join([BASEURL, 'entity', '-'.join(self.name.split()).lower()])

class EditorGroup(rdfSubject):
    rdf_type = FOAF.Group
    #name = rdfSingle(FOAF.name)
    members = rdfMultiple(FOAF.member, range_type=FOAF.Person)
    periodical = rdfSingle(FOAF.makes, range_type=BIBO.Periodical)




mapper()



def testOutput():
    graph = rdfSubject.db = ConjunctiveGraph()
    graph.parse('../data/capitalclass97.ttl', format="n3")
    #graph.parse('/home/maarten/workdir/serialservice/data/nlr57.rdf')
    #print(len(graph))
    #for s, p, o in graph.triples((None, None, None)):
    #    print p

    a = Article()
    for article in a.ClassInstances():
        if article.title != None: #Waar komt dat ene blanco artikel van?
            print article.title
            print '\t', 'By', ' and '.join(article.creators)
            #for c in article.creators:
            #    print "\t", "Author;", c
            print '\t', article.abstract[0:30], '...'
            print '\t', 'Pages', '-'.join([str(article.sPg), str(article.ePg)])
            print '\t', article.issue.periodical.title, 'nummer', article.issue.number
            print '\t', ''.join(['ISSN: ', article.issue.periodical.issn, '.']), 'Uitgever:', article.issue.periodical.publisher
            print '\n'
    
    #a = Article()
    #for article in a.ClassInstances():
    #    print article.title
    #    print '\t', article._ppo()
    #    print '-'*40


    #j = Periodical.get_by(issn="0309-8168")
    #print j.title


if __name__ == "__main__":
    testOutput()
