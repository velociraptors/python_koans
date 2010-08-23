"""A placeholder."""
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('this is a placeholder')

APP = webapp.WSGIApplication([('/', MainPage)], debug=True)

util.run_wsgi_app(APP)
