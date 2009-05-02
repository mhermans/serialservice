Serialservice
=============

***Keywords***: RDF, Pylons, bibliographic data.

About
-----

This is an experimental project. Its aim is evaluating the feasibility of running a standard Python web framework (Pylons) on top of RDF-data/a triplestore. Focus:

* Robustness of the RDF-Python ORM;
* Managing RDF-data (versioning, inferencing, manipulation);
* Easy data-entry and conversion to other/syndication formats.

If succesfull, it will provide a serial (alerting) service for progressive periodicals and a article metadata index.

Installation and Setup
----------------------

Reqs:

* Python (2.5 tested)
* RDFAlchemy (svn version tested)
* RDFlib
* Genshi
* Pylons

This should work:

    $ svn checkout http://www.openvest.com/svn/public/rdfalchemy/trunk  rdfalchemy
    $ cd rdfalchemy
    $ python setup.py install #This will also install the correct verion of RDFlib
    $ easy_install genshi
    $ easy_install pylons

Then in the serialsservice-folder run:
    
    $ paster serve --reload development.ini 
    
Browse to http://localhost:5000
