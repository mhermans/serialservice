#! /usr/bin/env pyton
# -*- coding: utf-8 -*-
import unittest, sys

sys.path.append('../utils')
from mapping import Article, Issue, Periodical, Book

from rdfalchemy import rdfSubject 
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace, BNode, URIRef


DC = Namespace('http://purl.org/dc/elements/1.1/')

class TestBasicMapping(unittest.TestCase):

    def setUp(self):
        self.graph = rdfSubject.db

    def tearDown(self):
        self.graph.remove((None, None, None))
        self.assertEqual(0, len(self.graph))

    def testMapAssertions(self):
        self.expectedMapping = {
            'http://purl.org/ontology/bibo/Article': Article, 
            'http://purl.org/ontology/bibo/Issue': Issue, 
            'http://purl.org/ontology/bibo/Periodical': Periodical,
            'http://purl.org/ontology/bibo/Book' : Book
        }

        self.assertEqual(self.expectedMapping, mapper())

    def testArticleMapping(self):
        self.assertEqual(0, len(self.graph))
        a = Article()
        self.assertTrue(isinstance(list(self.graph.subjects())[0], BNode))
        self.assertEqual(1, len(self.graph)) # bnode--rdf:type-->bibo:article

        a.title = "Testtitle" # + bnode--dc:title--> "Testtitle"
        self.assertEqual(2, len(self.graph)) 
        self.assertEqual(1, len(list(self.graph.triples((None,DC['title'], None)))))
        self.assertEqual(a.title, "Testtitle")

        a.creators = ["Testcreator1", "Testcreator2"]
        #a.creators = "Testcreator" XXX hoe doe je assertRaises met assignment?

        a.abstract = "Testabstract"
        a.sPg = 1
        a.ePg = 3
        #TODO check string & int types in rdf
        a.auStr = "Author 1, author 2"
        a.section = "Testsection"
        a.ivrs = ["Testintervieuwer"]
        a.ives = [u"Testgeïntervieuwde"]
        self.assertEqual(11, len(self.graph))

        #self.assertEqual(0, list(self.graph.triples((None, None, None))))

    def testIssue(self):
        i = Issue()
        i.number = 3
        self.assertEqual(2, len(self.graph))

    def testPeriodical(self):
        p  = Periodical()
        p.title = "Periodical title"
        p.issn = "1234-4321"
        p.publisher = "Periodical publisher"
        self.assertEqual(4, len(self.graph))

    def testBook(self):
        b = Book()
        b.title = "Booktitle"
        b.creators = ["Creator1"]
        b.publisher = "Publisher"
        b.pubdate = "2008-04-03"
        b.isbn = "1234512341234"

        self.assertEqual(6, len(self.graph))


    def testUriInitialization(self):
        self.assertEqual(0, len(self.graph))
        a = Article("<tag:test-article,2009-04-25>")
        #a = Article(URIRef("tag:test-article,2009-04-25"))
        self.assertEqual(0, len(self.graph)) #XXX bug? waarom geen rdf:type bibo:Article (bnode initialisatie wél)
        #self.assertTrue(isinstance(list(self.graph.subjects())[0], URIRef))

    def testTraversal(self):
        a = Article()
        i = Issue()
        p = Periodical()
        p.title = "Periodicaltitle"
        
        a.issue = i
        i.periodical = p
        self.assertEqual(a.issue.periodical.title, "Periodicaltitle")


class TestLoadDataMapping(unittest.TestCase):

    def setUp(self):
        self.graph = rdfSubject.db

    def tearDown(self):
        self.graph.remove((None, None, None))
        self.assertEqual(0, len(self.graph))

    def testLoad(self):
        self.graph.parse("/home/maarten/workdir/serialservice/data/capitalclass97.ttl", format="n3")
        self.assertEqual(85, len(self.graph))


if __name__ == "__main__":
    unittest.main()   
