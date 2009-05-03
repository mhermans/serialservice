import logging

from pylons import request, response, session, tmpl_context as c, app_globals
from pylons.controllers.util import abort, redirect_to
from pylons import config

from serialservice.lib.base import BaseController, render

from serialservice.model.bibo import Periodical, Issue, Article

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def index(self):
        c.issues = Issue.ClassInstances()
        c.title = "Serials Service"
        c.bodySection = "new"
        c.baseUrl = "http://localhost:5000/" #XXX c.baseUrl zouden in g.baseUrl moeten zitten, niet telken opnieuw definieren
        #return config['pylons.paths']['templates']
        #return config['app_conf']['cache_dir']
        #return config['global_conf']
        #return app_globals.baseUrl #equivalent aan:
        #return config['pylons.app_globals'].baseUrl
        return render('base.xml')

    def serials(self):
        
        c.periodicals = Periodical.ClassInstances()
        c.title = "Serials"
        c.bodySection = "serials"
        c.baseUrl = "http://localhost:5000/"

        return render('base.xml')

    def periodical(self, shortTitle):
        s = shortTitle
        
        c.periodical = Periodical.get_by(shortTitle=s)
        c.issues = Issue.filter_by(periodical=c.periodical.resUri)
        
        c.title = c.periodical.title        
        c.bodySection = "periodical"
        c.baseUrl = "http://localhost:5000/"
        return render('base.xml')

    def volume(self, shortTitle, volume):
        s = shortTitle       
        c.volume = volume

        c.periodical = Periodical.get_by(shortTitle=s)
        c.issues = Issue.filter_by(periodical=c.periodical.resUri) #XXX filter on volume does not work!
        c.title = ' '.join([c.periodical.title, ':', 'volume', c.volume])
        c.bodySection = "volume"
        c.baseUrl = "http://localhost:5000/"
        return render("base.xml")

    def issue(self, shortTitle, volume, number):
        s = shortTitle
        v = volume
        n = number


        #via globals: g.graph = rdfSubject.db
        #zie serialservice/lib/app_globals.py.

        p = Periodical.get_by(shortTitle=s)
        i = Issue.filter_by(periodical=p.resUri)
        
        #XXX controleer fatsoenlijk op 1 resultaat
        i = list(i)
        if len(i) == 1:
            i = list(i)[0]

        c.articles = Article.filter_by(issue=i.resUri)

        c.contributors = []

        for a in Article.filter_by(issue=i.resUri):
            for cr in a.creators:
                c.contributors.append(cr)
            for ivr in a.ivrs:
                 c.contributors.append(ivr)        
            for ive in a.ives:
                 c.contributors.append(ive)        

        c.issue = i
        c.title = i.periodical.title 
        c.bodySection = "issue"
        c.baseUrl = "http://localhost:5000/"
        return render("base.xml")

    def submit(self):
        c.title = "Submit data" 
        c.bodySection = "submit"
        c.baseUrl = "http://localhost:5000/"
        return render("base.xml")
