"""A placeholder."""
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('this is a placeholder')

application = webapp.WSGIApplication([('/', MainPage)], debug=True)

if __name__ == '__main__':
    run_wsgi_app(application)
