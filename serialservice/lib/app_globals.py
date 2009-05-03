"""The application's Globals object"""
from pylons import config

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

from rdfalchemy import rdfSubject
from rdflib import ConjunctiveGraph

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
        fn1 = "/home/maarten/workdir/serialservice/data/capitalclass97.ttl"
        fn2 = "/home/maarten/workdir/serialservice/data/dump.ttl"
        self.graph.parse(fn1, format="n3")
        self.graph.parse(fn2, format="n3")

        self.baseUrl = "http://localhost:5000/"
