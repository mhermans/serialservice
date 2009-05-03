#! /usr/bin/env python

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple, rdfContainer
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace, Literal, BNode, URIRef

BIBO = Namespace('http://purl.org/ontology/bibo/')
DC = Namespace('http://purl.org/dc/elements/1.1/')
DCTERMS = Namespace('http://purl.org/dc/terms/')
OV = Namespace('http://open.vocab.org/terms/')
PRISM = Namespace('http://prismstandard.org/namespaces/basic/2.0/')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS =  Namespace('http://www.w3.org/2000/01/rdf-schema#')
FOAF = Namespace('http://xmlns.com/foaf/0.1/')

BASEURL = "http://localhost:5000/serials/"
import urlparse

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
        return urlparse.urljoin(BASEURL, self.shortTitle )

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

        return urlparse.urljoin(BASEURL, '/'.join([self.periodical.shortTitle, v, n]))




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
    abstract = rdfSingle(DCTERMS['abstract'])
    sPg = rdfSingle(PRISM.startingPage)
    ePg = rdfSingle(PRISM.endingPage)
    auStr = rdfSingle(OV.authorString)
    section = rdfSingle(PRISM.section)
    issue = rdfSingle(DC.isPartOf, range_type=BIBO.Issue)
    ivrs = rdfMultiple(BIBO.interviewer)
    ives = rdfMultiple(BIBO.interviewee)
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

#ADR = Namespace('http://schemas.talis.com/2005/address/schema#')
#class Publisher
#    rdf_type = FOAF.Organization
#    name = rdfSingle(FOAF.name)
#    location = rdfSingle(ADR.localityName)

mapper()



def testOutput():
    graph = rdfSubject.db = ConjunctiveGraph()
    graph.parse('/home/maarten/workdir/serialservice/data/capitalclass97.ttl', format="n3")
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

def testTemplate():


    graph = rdfSubject.db = ConjunctiveGraph()
    fn1 = "/home/maarten/workdir/serialservice/data/capitalclass97.ttl"
    fn2 = "/home/maarten/workdir/serialservice/data/dump.ttl"
    graph.parse(fn1, format="n3")
    graph.parse(fn2, format="n3")
    #p = Periodical.get_by(issn="1372-0740")
    p = Periodical.get_by(shortTitle="capclass")
    v = None
    n = 97
    i = Issue.filter_by(periodical=p.resUri)
    i = list(i)
    if len(i) == 1:
        i = list(i)[0]
    alist = Article.filter_by(issue=i.resUri)
    from genshi.template import MarkupTemplate
    from genshi.output import encode
    f = open('/home/maarten/workdir/serialservice/templates/issue.xhtml')
    t = f.read()
    f.close()
    tmpl = MarkupTemplate(t)
    #filter_by(issue=i) werkt niet i.resUri wel. Filtering via chained descriptors zou leuk zijn: filter_by(issue.number=56, issue.periodical=p)
    #print list(alist)
    stream = tmpl.generate(issue=i, articles=alist)
    #stream = encode(stream)
    html = stream.render('xhtml')
    o = file("out.html", 'w')
    o.write(html)
    o.close()


if __name__ == "__main__":
    testOutput()
    testTemplate()
    #pass
