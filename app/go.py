#!/usr/bin/python

import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import *

class GoPage(webapp.RequestHandler):
  def RenderTemplate(self, template):
    path = os.path.join(os.path.dirname(__file__), 'templates', template)
    self.response.out.write(webapp.template.render(path, self.template_values))
  
  def CheckUser(self):
    user = users.get_current_user()
    if user != None:
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Sign out'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Sign in'
    
    self.template_values['user'] = user
    self.template_values['log_url'] = url
    self.template_values['log_url_linktext'] = url_linktext

class MainPage(GoPage):
  def get(self):
    self.template_values = {}
    self.CheckUser()
    self.RenderTemplate('index.html')

def main():
  application = webapp.WSGIApplication([('/', MainPage)],
                                        debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
