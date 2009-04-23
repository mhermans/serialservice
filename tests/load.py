#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace
import sys
sys.path.append('/home/maarten/workdir/serialservice/utils/')
from mapping import Article, Issue, Periodical
g = ConjunctiveGraph = rdfSubject.db
nlr = Periodical("<http://rdf.freebase.com/rdf/en.new_left_review>")
nlr.title = "New Left Review"
#nlr.resUri = "http://freebase.com"
nlr.issn = "0028-6060"

nlr56 = Issue("<tag:new-left-review-issue-56,2009-04-23>")
nlr56.periodical = nlr
nlr56.number = 56
#nlr56.title = "New Left Review 56 March-April 2009"

a1 = Article("<tag:obama-at-manassas,2009-04-23>")
a1.title = "Obama at Manassas"
a1.creators = ["Mike Davis"]
a1.summary = "Does Obama’s victory signal a political turning point comparable to 1980 or 1932? Mike Davis maps county-level changes, from below—minority-majority demographics, subprime suburbs, white-collar financial worries—catalysed by the 2008 campaign. From above, realignment of American capital behind the Silicon President."
a1.issue = nlr56

a2 = Article("<tag:freedoms-triumph,2009-04-23>")
a2.creators = ["Dylan Riley"]
a2.title = "Freedom's Triumph?"
a2.summary = "Reviving its classical definition, ‘rule of the propertyless’, Luciano Canfora recasts the story of democracy in Europe as one of successive defeats, with lessons from Louis Napoleon on the use of suffrage as legitimation for oligarchic rule. Dylan Riley assesses a remarkable historical polemic from the Italian philologist."
a2.issue = nlr56

a3 = Article("<tag:giovanni-arrighi,2009-04-22>")
a3.title = "Giovanni Arrighi: The Winding Paths of Capital"
a3.ivrs = ["David Harvey"]
a3.ives = ["Giovani Arrighi"]
a3.summary = "The author of Long Twentieth Century and Adam Smith in Beijing, interviewed by David Harvey, on dispossession and development, capitalist crises, China’s future. The political education of a teenage factory-manager, via African liberation struggles and autonomia operaia; and influences—Braudel, Gramsci, Smith, Marx—in Arrighi’s work."
a3.issue = nlr56

a4 = Article("<tag:feminism-capitalism,2009-04-22>")
a4.creators = ["Nancy Fraser"]
a4.title = "Feminism, Capitalism and the Cunning of History"
a4.summary = "Do feminism and neoliberalism share a secret affinity? Nancy Fraser on the co-option of gender politics by the ‘new spirit’ of post-Fordist capitalism, and subordination of its radical critique to a World Bank agenda. Might a neo-Keynesian shift offer prospects for socialist-feminist renewal?"
a4.issue = nlr56

a5 = Article("<tag:colletti-on,2009-04-23>")
a5.creators = ["Geoff Mann"]
a5.title = "Colletti on the Credit Crunch"
a5.summary = "What political opportunities arise from the current financial crisis? In a critical response to Robin Blackburn’s essay in NLR 50, Geoff Mann proposes the insights of Marx’s theory of value as a starting point for thinking beyond capitalist social relations—as Blackburn’s measures, he argues, do not."
a5.issn = nlr56


a6 = Article("<tag:value-theory,2009-04-23>")
a6.creators = ["Robin Blackburn"]
a6.title = "Value Theory and the Chinese Worker"
a6.summary = "In answer to Mann, Blackburn explores the paradoxes of fictitious capital, underwritten by super-exploitation of China’s producers. A public-utility credit system, democratic forms of nationalization and mechanisms to socialize investment as steps towards financial dual power."
a6.issue = nlr56

print(g.serialize(format="n3"))
g.remove((None,None,None)) # remove all triples/clean graph
