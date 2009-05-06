"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper, url_for

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    map.connect('mapping1', '/new', controller='pages', action='index' )
    map.connect('mapping2', '/serials', controller='pages', action='serials' )
    map.connect('mapping3', '/serials/:shortTitle', controller='pages', action='periodical' )
    map.connect('mapping4', '/serials/:shortTitle/:volume', controller='pages', action='volume')
    map.connect('mapping5', '/serials/:shortTitle/:volume/:number', controller='pages', action='issue')

    map.connect('mapping6', '/submit', controller='pages', action='submit' )
    map.connect('mapping7', '/entities/:uri', controller='pages', action='person', requirements = { 'fragment':'#id' }  )


    return map
