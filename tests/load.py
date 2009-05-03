#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rdfalchemy import rdfSubject, rdfSingle, rdfMultiple
from rdfalchemy.orm import mapper
from rdflib import ConjunctiveGraph, Namespace, URIRef
import sys
sys.path.append('/home/maarten/workdir/serialservice/utils/')
from mapping import Article, Issue, Periodical, Book
g = ConjunctiveGraph = rdfSubject.db

BIBO = Namespace('http://purl.org/ontology/bibo/')

    #############
    #   NLR 56  #
    #############

nlr = Periodical("<http://rdf.freebase.com/rdf/en.new_left_review>")
nlr.title = "New Left Review"
nlr.issn = "0028-6060"
nlr.shortTitle = "nlr"
nlr.homepage = URIRef("http://www.newleftreview.org/")

nlr56 = Issue("<tag:new-left-review-issue-56,2009-04-23>")
nlr56.periodical = nlr
nlr56.number = 56
nlr56.volume = 2
nlr56.title = "New Left Review 56 March-April 2009"
nlr56.pubdate = "2009-03-09"
nlr56.coverImg = URIRef("http://www.newleftreview.org/assets/images/NLR56cover.gif")

a1 = Article("<tag:obama-at-manassas,2009-04-23>")
a1.title = "Obama at Manassas"
a1.creators = ["Mike Davis"]
a1.abstract = "Does Obama’s victory signal a political turning point comparable to 1980 or 1932? Mike Davis maps county-level changes, from below—minority-majority demographics, subprime suburbs, white-collar financial worries—catalysed by the 2008 campaign. From above, realignment of American capital behind the Silicon President."
a1.issue = nlr56

a2 = Article("<tag:freedoms-triumph,2009-04-23>")
a2.creators = ["Dylan Riley"]
a2.title = "Freedom's Triumph?"
a2.abstract = "Reviving its classical definition, ‘rule of the propertyless’, Luciano Canfora recasts the story of democracy in Europe as one of successive defeats, with lessons from Louis Napoleon on the use of suffrage as legitimation for oligarchic rule. Dylan Riley assesses a remarkable historical polemic from the Italian philologist."
a2.issue = nlr56

a3 = Article("<tag:giovanni-arrighi,2009-04-22>")
a3.title = "Giovanni Arrighi: The Winding Paths of Capital"
a3.ivrs = ["David Harvey"]
a3.ives = ["Giovani Arrighi"]
a3.abstract = "The author of Long Twentieth Century and Adam Smith in Beijing, interviewed by David Harvey, on dispossession and development, capitalist crises, China’s future. The political education of a teenage factory-manager, via African liberation struggles and autonomia operaia; and influences—Braudel, Gramsci, Smith, Marx—in Arrighi’s work."
a3.issue = nlr56

a4 = Article("<tag:feminism-capitalism,2009-04-22>")
a4.creators = ["Nancy Fraser"]
a4.title = "Feminism, Capitalism and the Cunning of History"
a4.abstract = "Do feminism and neoliberalism share a secret affinity? Nancy Fraser on the co-option of gender politics by the ‘new spirit’ of post-Fordist capitalism, and subordination of its radical critique to a World Bank agenda. Might a neo-Keynesian shift offer prospects for socialist-feminist renewal?"
a4.issue = nlr56

a5 = Article("<tag:colletti-on,2009-04-23>")
a5.creators = ["Geoff Mann"]
a5.title = "Colletti on the Credit Crunch"
a5.abstract = "What political opportunities arise from the current financial crisis? In a critical response to Robin Blackburn’s essay in NLR 50, Geoff Mann proposes the insights of Marx’s theory of value as a starting point for thinking beyond capitalist social relations—as Blackburn’s measures, he argues, do not."
a5.issue = nlr56


a6 = Article("<tag:value-theory,2009-04-23>")
a6.creators = ["Robin Blackburn"]
a6.title = "Value Theory and the Chinese Worker"
a6.abstract = "In answer to Mann, Blackburn explores the paradoxes of fictitious capital, underwritten by super-exploitation of China’s producers. A public-utility credit system, democratic forms of nationalization and mechanisms to socialize investment as steps towards financial dual power."
a6.issue = nlr56

heinsohn2008 = Book("<urn:isbn:9783492251242>")
heinsohn2008.creators = ["Gunnar Heinsohn"]
heinsohn2008.title = u"Söhne und Weltmacht: Terror im Aufstieg und Fall der Nationen"
heinsohn2008.isbn = "9783492251242"
heinsohn2008.publisher = "Piper"
heinsohn2008.pubdate = "2008"
heinsohn2008.citation = "Gunnar Heinsohn, Söhne und Weltmacht: Terror im Aufstieg und Fall der Nationen, Piper: Munich 2008, €9.20, paperback,189 pp, 978 3 492 25124 2."

a7 = Article("<tag:goran-therborn-on-heinsohn,2009-04-25>")
a7.title = u"Göran Therborn on Heinsohn, Söhne und Weltmacht"
a7.creators = [u"Göran Therborn"]
a7.abstract = "Political demography of the Mid-East youth bulge as threat to Western power."
a7.issue = nlr56
a7.reviewOf = [heinsohn2008]

guha2007 = Book("<urn:isbn:9780230016545>")
guha2007.creators = ["Ramachandra Guha"]
guha2007.title = "India after Gandhi: The History of the World’s Largest Democracy"
guha2007.publisher = "Macmillan"
guha2007.pubdate = "2007"
guha2007.isbn = "9780230016545"
guha2007.citation = "Ramachandra Guha, India after Gandhi: The History of the World’s Largest Democracy, Macmillan: London 2007, £25, hardback, 900 pp, 978 0 230 01654 5."

a8 = Article('<tag:sumit-sarkar-on-guha,2009-04-25>')
a8.title = "Sumit Sarkar on Guha, India after Gandhi"
a8.creators = ["Sumit Sarkar"]
a8.abstract = "The subcontinental giant as ‘unnatural nation’ in the first history of the post-Independence era."
a8.issue = nlr56
a8.reviewOf = [guha2007]


groys2008 = Book('<tag:urn:isbn:9780262072922>')
groys2008.creators = ["Boris Groys"]
groys2008.publisher = "MIT Press"
groys2008.pubdate = "2008"
groys2008.isbn = "9780262072922"
groys2008.citation = "Boris Groys, Art Power, MIT Press: Cambridge 2008, $22.95, hardback, 190 pp, 978 0 262 07292 2."

a9 = Article('<tag:barry-schwabsky-on-groys,2009-04-25>')
a9.creators = ["Barry Schwabsky"]
a9.title = "Barry Schwabsky on Groys, Art Power"
a9.abstract = "Essays on aesthetics and politics, founded on the disconcerting insights of late-Soviet conceptualism."
a9.issue = nlr56
a9.reviewOf = [groys2008]

    #####################
    #   SAMPOL 16(04)   #
    #####################

sampol = Periodical('<urn:issn:1372-0740>')
sampol.title = "Samenleving en Politiek"
sampol.issn = "1372-0740"
sampol.publisher = "Stichting Gerrit Kreveld"
sampol.shortTitle = "sampol"
sampol.homepage = URIRef("http://stichtinggerritkreveld.be.res7.mijnpreview.com/ECMS_CLIENT_SGK/pages/showpage.php?id=13")


sampol16_4 = Issue('<tag:sampol-issue-16-04,2009-04-26>')
sampol16_4.number = 4
sampol16_4.volume = 16
sampol16_4.pubdate = "2009-04-01"
sampol16_4.title = "Samenleving & Poltiek jaargang 16, 2009, nr.4 (april)"
sampol16_4.periodical = sampol

a21 = Article("<tag:wie-op-de-rem-staat,2009-04-25>")
a21.title = "Wie op de rem staat, geraakt niet vooruit"
a21.label = "Edito"
a21.creators = ["Jan de Zutter"]
a21.abstract = "Als we de peilingen mogen geloven - en dat mogen we beslist niet - krijgt links in Vlaanderen op 7 juni een oplawaai van jewelste. Aan de halte van een nieuw Vlaams bestuur moeten sp.a en Groen! een lange rij centrumrechtse, populistische, rechtse en radicaal-rechtse partijen laten voorgaan. Zoals het er nu uitziet, zal links op de volgende bus moeten wachten. Als die nog komt. Want rechts Vlaanderen zal ongetwijfeld met genoegen gebruik maken van publieke diensten om ze daarna met evenveel plezier op een streng dieet te zetten. We zien het vandaag gebeuren met de reddingsoperaties voor de banken en de steunmaatregelen voor de economie. In tegenstelling tot de VS, waar een minderheid die hard republikeinen tenminste het fatsoen had te leven naar hun mythe van de vrije markt en dus overheidssteun publiekelijk afwezen, is er in Europa amper een liberaal te vinden die niet gretig het handje uitsteekt om te kunnen eten uit de ruif van de gemeenschap. Na de maaltijd wordt er steevast semantisch nagetafeld over het onderscheid tussen de sterke overheid en de vette overheid. Voor de steunmaatregelen was een sterke overheid noodzakelijk, na de maaltijd wordt er geschamperd over de veel te vette overheid. Zo weinig respect voor de solidariteit die gewone mensen opbrengen via de publieke dienstverlening werd zelden vertoond. Een mens zou in deze discussie op z'n minst een vorm van wederkerigheid mogen verwachten."
a21.sPg = 1
a21.ePg = 3
a21.issue = sampol16_4

a22 = Article('<tag:de-efficiente-overheid,2009-04-25>')
a22.title = "De efficiënte overheid geanalyseerd"
a22.creators =["Maarten Luts", "Annie Hondeghem"]
a22.auStr = "Maarten Luts, Annie Hondeghem"
a22.abstract = u"Doordat werkgeversorganisaties, gekleurde denktanks en ook de media het efficiëntiedebat in belangrijke mate hebben weten te monopoliseren, is het debat omtrent de efficiënte overheid in een taboesfeer terechtgekomen. Willen we onze overheid werkelijk klaarstomen voor 2020, dan moeten de oogkleppen afgenomen worden en moet er dringend een gefundeerd debat plaatsvinden over de efficiënte overheid. De statistieken omtrent de overheidsomvang onderstrepen overigens de noodzaak om de personeelsaantallen van dit debat deel te laten uitmaken."
a22.sPg = 4
a22.ePg = 14
a22.issue = sampol16_4
	
a23 = Article('<tag:sociaaldemocraten-en-populisme,2009-04-25>')
a23.title = "Sociaaldemocraten en populisme. Kloven en bruggen"
a23.creators = ["Maarten Van Alstein"]
a23.abstract = "Het populisme eist in de hedendaagse politiek een belangrijke rol voor zich op. In zijn opmerkelijke essay over dit fenomeen beschrijft David Van Reybrouck het succes van populistische politici en partijen in het licht van de diploma- en cultuurkloof in onze samenleving, de nieuwe maatschappelijke breuklijn. In het populisme herkent hij de stem van laaggeschoolden van wie de betrokkenheid bij de democratie en de samenleving onder druk is komen te staan. Van Reybrouck wil deze stem ernstig nemen, en daarom pleit hij niet voor minder, maar voor meer en beter populisme. Hier wordt de vraag gesteld hoe sociaaldemocraten moeten omgaan met het betoog van David Van Reybrouck."
a23.sPg = 15
a23.ePg = 23
a23.issue = sampol16_4

a24 = Article('<tag:frank-van-massenhoven,2009-04-25>')
a24.title = "Frank Van Massenhoven: 'Word weer de regisseur van je eigen leven'"
a24.ivrs = ["Jan de Zutter"]
a24.ives = ["Frank Van Massenhoven"]
a24.abstract = "Twee jaar geleden werd hij Overheidsmanager van het Jaar en vandaag leidt hij een federale overheidsdienst met tevreden ambtenaren die hun werkuren zelf regelen, thuis kunnen werken en trots zijn op hun radicaal vernieuwde dienst. Heeft Frank Van Massenhove ontdekt hoe je overheidsdiensten de 21ste eeuw kunt inloodsen?"
a24.sPg = 24
a24.ePg = 32
a24.issue = sampol16_4
	
a25 = Article('<tag:erik-meynen,2009-04-25>')
a25.title = "Erik Meynen (Portfolio)"
a25.sPg = 33
a25.ePg = 40
a25.issue = sampol16_4
	
a26 = Article('<tag:het-beroepenhuis,2009-04-25>')
a26.title = "Het Beroepenhuis (Project in de kijker)"
a26.creators = ["Mil Kooyman"]
a26.abstract = "Er is in de voorbije regeerperiode waarschijnlijk geen toespraak geweest van minister Vandenbroucke waarin hij niet minstens een paar keer de woorden talenten en talentontwikkeling heeft laten vallen. Ondertussen is nagenoeg iedereen er van overtuigd dat de talenten van jongeren het belangrijkste criterium moet zijn voor hun studie- en beroepskeuze. Talentontwikkeling in ons onderwijs is dan ook meer dan noodzakelijk. Sinds 1999 timmert Het Beroepenhuis aan de (talenten)weg en op 4 maart 2005 gingen de deuren van het huis effectief open. Een schot in de roos."
a26.sPg = 41
a26.ePg = 43
a26.issue = sampol16_4
	
a27 = Article('<tag:politieke-peilingen,2009-04-25>')
a27.title = "Politieke peilingen in de media: fictie of frictie?"
a27.auStr = "Jaak Billiet, Nathalie Sonck"
a27.creators = ["Jaak Billiet", "Nathalie Sonck"]
a27.abstract = "Peilingen vertalen individuele opvattingen in een collectieve publieke opinie, maar indien dit op een gebrekkige en vertekende wijze gebeurt, ontstaat een misleidend beeld dat afwijkt van de werkelijke zorgen van de bevolking.  Door het rapporteren van deze peilingen in de media wordt fictie gecreëerd."
a27.sPg = 44
a27.ePg = 53
a27.issue = sampol16_4

a28 = Article('<tag:outplacement-take,2009-04-25>')
a28.title = "Outplacement: take the money and run"
a28.creators = ["Philippe Diepvents"]
a28.abstract = "'Herstel het vertrouwen' is de gemeenschappelijke titel voor de relanceplannen die de maatregelen bundelen die de federale en Vlaamse overheden zullen nemen om de effecten van de financiële crisis in ons land te temperen. Heel wat van deze maatregelen moeten nog geconcretiseerd en in de praktijk omgezet worden. De voorbije maanden was vooral de discussie rond het afschaffen van de doelgroepenvermindering, die vanuit het uitzonderlijk akkoord van de sociale partners werd overgenomen, brandend actueel. De plannen bevatten echter uiteraard nog veel meer maatregelen, die op initiatief van de politieke overheden werden genomen. Met dit artikel willen we de aandacht vestigen op een aantal elementen uit de relanceplannen die tot nog toe onder de radar bleven. Met name gaat het over die bijsturingen die te maken hebben met de regelgeving rond outplacement."
a28.sPg = 54
a28.ePg = 60
a28.issue = sampol16_4
	
a29 = Article('<tag:met-huidig-beleid,2009-04-25>')
a29.title = "Met huidig beleid raakt voedselcrisis niet opgelost!"
a29.creators = ["Thierry Kesteloot"]
a29.abstract = "Stijgende voedselprijzen en voedselrellen in vele steden in ontwikkelingslanden haalden de pers in 2008. Deze crisis ging niet onopgemerkt voorbij. De media-aandacht vertaalde zich in een buitengewone politieke belangstelling. Maar sindsdien werd de voedselcrisis opgevolgd door de financiële en economische crisis. De voedselprijzen duiken in elkaar, en staan veel lager dan één jaar geleden. Is het einde van de voedselcrisis dichterbij gekomen? Niet met het bestaande beleid, aangezien het mede aan de oorzaak van de crisis ligt."
a29.sPg = 61
a29.ePg = 69
a29.issue = sampol16_4
	
b1 = Book('<urn:isbn:9789064450624>')
b1.title = "Rooddruk voor een nieuw socialisme"
b1.creators = ["Erik De Bruyn"]
b1.publisher = "epo"
b1.isbn = "9789064450624"
b1.cover = "http://www.epo.be/covers/epo/9789064450624.jpg"
	
a210 = Article('<tag:boekbespreking-rooddruk-voor,2009-04-25>')
a210.title = "Boekbestpreking 'Rooddruk voor een nieuw socialisme'"
a210.creators = ["Luc Vanneste"]
a210.reviewOf = [b1]
a210.abstract = "Boekbespreking: Erik de Bruyn, Berchem, epo, 2009"
a210.sPg = 70
a210.epg = 72
a210.issue = sampol16_4
#sampol16_4.articles = (a21, a22, a23, a24, a25, a26, a27, a28, a29, a210)

print(g.serialize(format="n3"))
g.remove((None,None,None)) # remove all triples/clean graph
