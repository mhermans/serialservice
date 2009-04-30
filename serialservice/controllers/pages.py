import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from serialservice.lib.base import BaseController, render

import sys
sys.path.append('/home/maarten/workdir/serialservice/utils/')
from mapping import Periodical, Issue, Article


log = logging.getLogger(__name__)

class PagesController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/pages.mako')
        # or, return a response
        return 'Hello World'

    def serials(self):
        
        c.periodicals = Periodical.ClassInstances()
        c.title = "Serials"
        c.bodySection = "serials"
        return render('base.xml')

    def periodical(self, shortTitle):
        s = shortTitle
        
        c.periodical = Periodical.get_by(shortTitle=s)
        c.issues = Issue.filter_by(periodical=c.periodical.resUri)
        
        c.title = c.periodical.title        
        c.bodySection = "periodical"
        return render('base.xml')
















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

        alist = Article.filter_by(issue=i.resUri)
        
        c.issue = i
        c.articles = alist
        c.title = i.periodical.title 
        c.bodySection = "issue"
        return render("base.xml")










