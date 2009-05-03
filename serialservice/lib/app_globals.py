"""The application's Globals object"""
import os
from pylons import config

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

from rdfalchemy import rdfSubject
from rdflib import ConjunctiveGraph, Literal

from serialservice.model.bibo import Article, Person
from serialservice.model.namespaces import BIBO


import unicodedata

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """
    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))

        self.graph = rdfSubject.db = ConjunctiveGraph()
        fn1 = os.path.join(config['pylons.paths']['data'], 'capitalclass97.ttl')
        fn2 = os.path.join(config['pylons.paths']['data'], 'dump.ttl')
        self.graph.parse(fn1, format="n3")
        self.graph.parse(fn2, format="n3")
       
        for a in Article.ClassInstances():
            makers = []
            for c in a.creators:
                personSlug = '-'.join(unicodedata.normalize('NFKD', c).encode('ascii','ignore').split()).lower()
                uri = ''.join(['<', "http://localhost:5000/entities/", personSlug, '>'])
                p = Person(uri)
                p.name = c
                makers.append(p)
            a.makers = makers
            ies = a.ives
            irs = a.ivrs

            a.ives = []
            a.ivrs = []

            for ie in ies:
                personSlug = '-'.join(unicodedata.normalize('NFKD', ie).encode('ascii','ignore').split()).lower()
                uri = ''.join(['<', "http://localhost:5000/entities/", personSlug, '>'])
                p = Person(uri)


                p.name = ie
                a.ives = a.ives + [p]

            for ir in irs:
                personSlug = '-'.join(unicodedata.normalize('NFKD', ir).encode('ascii','ignore').split()).lower()
                uri = ''.join(['<', "http://localhost:5000/entities/", personSlug, '>'])
                p = Person(uri)
                p.name = ir
                a.ivrs = a.ivrs + [p]

        for s, p, o in self.graph.triples((None, BIBO.interviewer, None)):
            if isinstance(o, Literal):
                self.graph.remove((s, p, o))

        for s, p, o in self.graph.triples((None, BIBO.interviewee, None)):
            if isinstance(o, Literal):
                self.graph.remove((s, p, o))

        fn3 = os.path.join(config['pylons.paths']['data'], 'convert.ttl')
        f = open(fn3, 'rw')
        self.graph.serialize(fn3)
        f.close()
        self.baseUrl = "http://localhost:5000/"
