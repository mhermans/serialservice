NOTAS Serial service
====================

Data-wringling scripts:
-----------------------
Met SPIN - SPARQL Inferencing Notation?

Overerving language van taal Periodical


RDFAlchemy remarks
------------------

"title" as a property is tricky, use dictionary notation DC['title'] (something with unicode, cf. mailinglist)

    DONT: title = DC.title
    DO: title = DC['title']

When instantiating rdfSubjects by URI, do not forget the '<' & '>'. Eg:
    
    a = Article('<http://stableid.example.com/article>')

RDF types do not get assigned automaticly? Default behaviour or bug?

Inheritance works?

@property -> uitzoeken hoe dat werkt

Bestaande projecten:

* Bruce D'arcus' persoonlijke site (overal die kerel!)
* Shabti
* django-foaf
* Een mysterieze "bibliosite" door Philip Cooper

TODO
------

DONE ***rdf:type bij initialiseren***. Initialiseren via uri geeft geen rdf:type, itt. via Bnode. init subclassen? Andere oplossing: patchen

DONE ***Unicode probleem***. Genshi verwacht unicode intern http://genshi.edgewall.org/wiki/GenshiFaq#WhydoesGenshiraiseaUnicodeDecodeErrorwhenItrytorendernon-ASCIIstrings Het handigste is als dit bij input zeker unicode is (rdflib of rdfaclchemy); ook rekening houden met python3 aanpassingen. Snap het niet echt, maar als je je terminal redirection vermijd (ascii default), werkt alles blijkbaar.

DONE ***Manier om items te sorteren***. Issue instances zouden een articles-property moeten hebben, en Periodical instances een issues-property die een gesorteerde lijst van artikels, resp. issues deient terug te geven. Cf. http://groups.google.com/group/rdfalchemy-dev/browse_thread/thread/ad9363b7f1b275c2 Mogelijkheden:

    Met een rdf:Seq oplossen
    Met een property per article ...
        + ... rdfMultiple subclassen zodat i.articles in volgorde teruggeeft
        + ... aparte functie order(someList) die voor personen, issues, articles, ed. logisch volgordes geeft.
        (telkens sorteren op pg-nummer->gaat niet altijd (bv. electr tijdschrift) -> custom prop).

DONE ***Sorteerfunctie***. "If you need variables, functions, or classes for use in multiple templates, you can put definitions in lib/helpers.py. Those definitions will be available in your templates in the h variable." -> hier die sorteerfunctie. Nope, __lt__ en __gt__ overriden geeft ook sorteerfunctie.

***sequence properties registreren***:

    ov:numberOfItems
    ov:itemSeqNumber


***Issue title genreren***. Een template-functie schrijven die een mooie issue-title genereerd.

***Date localisation***. Babel gebruiken om datum van YYYY-MM-DD naar lokaal formaat te krijgen. Eerst kijken of het naar python datatime objects gemapt wordt.

***Valid XHTML+RDFa*** genereren

***Link naar RDF** Link header? <head>? RDFa?

***Basic html submission form*** 

Url pattern
-----------

    Article info: http://serials.progsite.org/serials/sampol/16/04/5
        -> about: http://serials.progsite.org/serials/sampol/16/04/5#id

    Article info: http://serials.progsite.org/nlr/0/56/3 (nu volume)
        -> about http://serials.progsite.org/nlr/0/56/3#id

    http://who.progsite/entities/imavo
        (in controller: entity-class opvragen -> ander template laden (zelfde routing)

    http://who.progsite/entities/freddy-de-pauw
        -> about http://who.progsite/entities/freddy-de-pauw#id
        
De #id urls als resUri/identifier gebruiken, maakt locUrl overbodig, en geeft een httprange-14 zinnige oplossing...

Principles:
----------

* Open data/content http://opendefinition.org/
* Open standards (W3C)
* Open source (github)

Thanks to:

* http://plugins.learningjquery.com/expander/index.html
* Various sites for demonstrating css-tricks
* COLOURlovers http://www.colourlovers.com/palette/804447/know_thy_enemy
* http://www.pengoworks.com/workshop/jquery/autocomplete.htm
* http://www.coldfusionjedi.com/index.cfm/2009/2/22/Using-jQuery-to-add-form-fields--with-validation

Various
-------

* de rdf/rss van Ingentaconnect is heel proper http://api.ingentaconnect.com/content/brill/hm/latest?format=rss gebruikten rss:items -> Seq voor volgorde articles
* http://workaround.org/pylons/pylons-cheatsheet.html
* http://www.rexx.com/~dkuhlman/pylons_quick_site.html
* http://www.malsup.com/jquery/form/
* Een wordl per issue zou wel leuk zijn...
