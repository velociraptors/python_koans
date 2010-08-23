"""Stuff to make the app go."""
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template

class MainPage(webapp.RequestHandler):
    """Make the welcome page happen."""
    def get(self):
        path = './templates/index.html'
        template_values = {}
        self.response.out.write(template.render(path, template_values))

APP = webapp.WSGIApplication([('/', MainPage)], debug=True)

util.run_wsgi_app(APP)
