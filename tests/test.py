
import unittest
import sys
sys.path.append('../utils')

from mapping import Article, Issue, Periodical
from rdfalchemy import rdfSubject 
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph

class TestBasicMapping(unittest.TestCase):

    def setUp(self):
        self.graph = ConjunctiveGraph = rdfSubject.db

    def testMapAssertions(self):
        self.expectedMapping = {
            'http://purl.org/ontology/bibo/Article': Article, 
            'http://purl.org/ontology/bibo/Issue': Issue, 
            'http://purl.org/ontology/bibo/Periodical': Periodical
        }

        self.assertEqual(self.expectedMapping, mapper())

    def testUnitMapping(self):
        a = Article
        a.sPg = 3


    def tearDown(self):
        self.graph = None

class TestLoadDataMapping(unittest.TestCase):

    def setUp(self):
        self.graph = ConjunctiveGraph = rdfSubject.db

    def testLoad(self):
        self.graph.parse("/home/maarten/workdir/serialservice/data/capitalclass97.ttl", format="n3")
        self.assertEqual(85, len(self.graph))

    def tearDown(self):
        self.graph = None

if __name__ == "__main__":
    unittest.main()   
