#!/usr/bin/python

from google.appengine.ext import db
from google.appengine.api import users

class Event(db.Model):
	"""An event is the container that everything else lives in. It could be a concert
	or a vacation. It could include one person or many."""
  name = db.StringProperty(required=True)
  start_date = db.DateProperty()
  end_date = db.DateProperty()
  organizer = Person()
	location = Location()
	#acl or privacy setting

class Location(db.Model):
	"""Could be any kind of location, like a hotel, a park, a city, or a country.
	Really anything"""
  name = db.StringProperty(required=True)
  kind = LocationType(db.Model)
  #lat and lng are both needed here.
  #rating (would be derived from another class for user votes.)

class LocationType(db.Model):
	"""Used in place of an enum in the Locaiton. This way we can add new location
	types from the web interface later"""
	name = db.StringProperty(required=True)

class Person(db.Model):
	user = db.UserProperty()
	#phone
  #Friends, other people you might take a trip with

class Ratings(db.Model):
	user = Person()
	location = Location()
	#vote whatever the right thing is here