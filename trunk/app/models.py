#!/usr/bin/python

from google.appengine.ext import db

class Event(db.Model):
	"""An event is the container that everything else lives in. It could be a concert
	or a vacation. It could include one person or many."""
  name = db.StringProperty(required=True)
  start_date = db.DateProperty()
  end_date = db.DateProperty()
  organizer = db.ReferenceProperty(Person)
	location = db.ReferenceProperty(Location)
	#acl or privacy setting

class Location(db.Model):
	"""Could be any kind of location, like a hotel, a park, a city, or a country.
	Really anything"""
  name = db.StringProperty(required=True)
  kind = db.ReferenceProperty(LocationType)
	geopt = db.GeoPtProperty()

class LocationType(db.Model):
	"""Used in place of an enum in the Locaiton. This way we can add new location
	types from the web interface later"""
	name = db.StringProperty(required=True)

class Person(db.Model):
	user = db.UserProperty()
	phone = db.PhoneNumberProperty()
  #Friends, other people you might take a trip with

class Ratings(db.Model):
	user = db.ReferenceProperty(Person)
	location = db.ReferenceProperty(Location)
  rating = db.RatingProperty()	
