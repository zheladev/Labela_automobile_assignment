from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory =SignedCookieSessionFactory('test')
    config = Configurator(settings=settings, session_factory=session_factory)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    
    return config.make_wsgi_app()
