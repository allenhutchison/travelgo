#!/usr/bin/python

from google.appengine.ext import db


class Person(db.Model):
  user = db.UserProperty()
  phone = db.PhoneNumberProperty()
  #Friends, other people you might take a trip with

class LocationType(db.Model):
  name = db.StringProperty(required=True)

class Location(db.Model):
  name = db.StringProperty(required=True)
  location_type = db.ReferenceProperty(LocationType)
  geopt = db.GeoPtProperty()

class Ratings(db.Model):
  user = db.ReferenceProperty(Person)
  location = db.ReferenceProperty(Location)
  rating = db.RatingProperty()  

class Event(db.Model):
  name = db.StringProperty(required=True)
  start_date = db.DateProperty()
  end_date = db.DateProperty()
  organizer = db.ReferenceProperty(Person)
  location = db.ReferenceProperty(Location)
