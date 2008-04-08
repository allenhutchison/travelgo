#!/usr/bin/python

import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp

from models import Trip

class MainPage(webapp.RequestHandler):
  def get(self):
		pass
	


def main():
	application = webapp.WSGIApplication([('/', MainPage)],
																				debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()


