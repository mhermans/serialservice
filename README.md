Serialservice
=============

***Keywords***: RDF, Python, ORM, Pylons, bibliographic data.

About
-----

This is an experimental project. Its aim is evaluating the feasibility of running a standard Python web framework (Pylons) on top of RDF-data/a triplestore. Focus:

* Robustness of the RDF-Python ORM;
* Managing RDF-data (versioning, inferencing, manipulation);
* Easy data-entry and conversion to other/syndication formats.

If succesfull, it will provide a serial (alerting) service for progressive periodicals and an article metadata index.

Current state
-------------

* Proof of concept works: RDF data is loaded in memory; mapped to python classes and navigated using Pylons & Genshi templates.
* Site-layout: XHTML, CSS, ...
* Dynamic data-entry forms (autocomplete with backend)

Installation and Setup
----------------------

Reqs:

* [Python](http://www.python.org) (2.5 tested)
* [RDFAlchemy](http://www.openvest.com/trac/wiki/RDFAlchemy) (svn version tested)
* [RDFlib](http://www.rdflib.net/)
* [Genshi](http://genshi.edgewall.org/)
* [Pylons](http://pylonshq.com/)

This should work:

    $ svn checkout http://www.openvest.com/svn/public/rdfalchemy/trunk  rdfalchemy
    $ cd rdfalchemy
    $ python setup.py install #This will also install the correct verion of RDFlib
    $ easy_install genshi
    $ easy_install pylons

Then in the serialsservice-folder run:
    
    $ paster serve --reload development.ini 
    
Browse to http://localhost:5000


See also
--------

* [Bibliographic ontology](http://bibliontology.com/) Ontology used.
* [Bruce d'Arcus personal site](http://bruce.darcus.name/) Similar project using RDFAlchemy + web.py; [github repository](http://github.com/bdarcus/mysite/)
