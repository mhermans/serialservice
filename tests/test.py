#! /usr/bin/env pyton
# -*- coding: utf-8 -*-
import unittest, sys

sys.path.append('../utils')
from mapping import Article, Issue, Periodical

from rdfalchemy import rdfSubject 
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph

class TestBasicMapping(unittest.TestCase):

    def setUp(self):
        self.graph = rdfSubject.db

    def testMapAssertions(self):
        self.expectedMapping = {
            'http://purl.org/ontology/bibo/Article': Article, 
            'http://purl.org/ontology/bibo/Issue': Issue, 
            'http://purl.org/ontology/bibo/Periodical': Periodical
        }

        self.assertEqual(self.expectedMapping, mapper())

    def testUnitMapping(self):
        self.assertEqual(0, len(self.graph))
        a = Article()
        self.assertEqual(1, len(self.graph)) # bnode--rdf:type-->bibo:article
        a.title = "Testtitle"
        self.assertEqual(2, len(self.graph)) # bnode--rdf:type-->bibo:article
        #self.assertEqual(0, list(self.graph.triples((None, None, None))))
    
    def testInitiationAndAssignment(self):
        a = Article()

    def tearDown(self):
        self.graph.remove((None, None, None))
        self.assertEqual(0, len(self.graph))

class TestSomething(unittest.TestCase):
    
    def setUp(self):
        self.graph = rdfSubject.db

    def testUriInitialization(self):
        self.assertEqual(0, len(self.graph))
        a = Article("<tag:test-article,2009-04-25>")
        self.assertEqual(0, len(self.graph)) #XXX bug? waarom geen rdf:type bibo:Article (bnode initialisatie wél)
    
    def tearDown(self):
        self.graph.remove((None, None, None))
        self.assertEqual(0, len(self.graph))

class TestLoadDataMapping(unittest.TestCase):

    def setUp(self):
        self.graph = rdfSubject.db

    def testLoad(self):
        self.graph.parse("/home/maarten/workdir/serialservice/data/capitalclass97.ttl", format="n3")
        self.assertEqual(85, len(self.graph))

    def tearDown(self):
        self.graph.remove((None, None, None))

if __name__ == "__main__":
    unittest.main()   
