#!/usr/bin/python

from google.appengine.ext import db
from google.appengine.api import users

class Trip(db.Model):
	name = db.StringProperty(required=True)
	start_date = db.DateProperty()
	end_date = db.DateProperty()
	organizer = db.UserProperty()