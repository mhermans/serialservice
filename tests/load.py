#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace
import sys
sys.path.append('/home/maarten/workdir/serialservice/utils/')
from mapping import Article, Issue, Periodical
g = ConjunctiveGraph = rdfSubject.db
nlr = Periodical()
nlr.title = "New Left Review"
#nlr.resUri = "http://freebase.com"
nlr.issn = "0028-6060"

nlr56 = Issue()
nlr56.periodical = nlr
nlr56.number = 56
#nlr56.title = "New Left Review 56 March-April 2009"

a1 = Article()
a1.title = "Obama at Manassas"
a1.creator = ["Mike Davis"]
a1.summary = "Does Obama’s victory signal a political turning point comparable to 1980 or 1932? Mike Davis maps county-level changes, from below—minority-majority demographics, subprime suburbs, white-collar financial worries—catalysed by the 2008 campaign. From above, realignment of American capital behind the Silicon President."
a1.issue = nlr56

a2 = Article()
a2.creator = ["Dylan Riley"]
a2.title = "Freedom's Triumph?"
a2.summary = "Reviving its classical definition, ‘rule of the propertyless’, Luciano Canfora recasts the story of democracy in Europe as one of successive defeats, with lessons from Louis Napoleon on the use of suffrage as legitimation for oligarchic rule. Dylan Riley assesses a remarkable historical polemic from the Italian philologist."
a2.issue = nlr56

a3 = Article()
a3.title = "Giovanni Arrighi: The Winding Paths of Capital"
a3.ivrs = ["David Harvey"]
a3.ives = ["Giovani Arrighi"]
a3.summary = "The author of Long Twentieth Century and Adam Smith in Beijing, interviewed by David Harvey, on dispossession and development, capitalist crises, China’s future. The political education of a teenage factory-manager, via African liberation struggles and autonomia operaia; and influences—Braudel, Gramsci, Smith, Marx—in Arrighi’s work."
a3.issue = nlr56

print(g.serialize(format="n3"))
g.remove((None,None,None)) # remove all triples/clean graph
