#!/usr/bin/python

import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import *

class GoPage(webapp.RequestHandler):
  def RenderTemplate(self, template, template_values):
    path = os.path.join(os.path.dirname(__file__), 'templates', template)
    self.response.out.write(webapp.template.render(path, template_values))

class MainPage(GoPage):
  def get(self):
    if users.get_current_user():
      user = users.get_current_user()
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Sign Out'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Sign In'

    template_values = {
      "user": user,
      "log_url": url,
      "log_url_linktext": url_linktext
    }
    self.RenderTemplate('index.html', template_values)


def main():
  application = webapp.WSGIApplication([('/', MainPage)],
                                        debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
