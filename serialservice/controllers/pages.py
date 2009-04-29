import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from serialservice.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/pages.mako')
        # or, return a response
        return 'Hello World'

    def issue(self, shortTitle, volume, number):
        s = shortTitle
        v = volume
        n = number

        #via globals: g.graph = rdfSubject.db
        #zie serialservice/lib/app_globals.py.
        
        import sys
        sys.path.append('/home/maarten/workdir/serialservice/utils/')
        from mapping import Periodical, Issue, Article

        p = Periodical.get_by(shortTitle=s)
        i = Issue.filter_by(periodical=p.resUri)
        
        #XXX controleer fatsoenlijk op 1 resultaat
        i = list(i)
        if len(i) == 1:
            i = list(i)[0]

        alist = Article.filter_by(issue=i.resUri)
        
        c.issue = i
        c.articles = alist
        return render("issue.xhtml")
