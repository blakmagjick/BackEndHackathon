from peewee import *
import os
import datetime
from playhouse.db_url import connect

DATABASE = connect('sqlite:///attendees.sqlite')

class BaseModel(Model):
    class Meta:
        database = DATABASE 

class Attendees(BaseModel):
    name = CharField()
    phone = CharField()
    address = CharField()
    city = CharField()
    state = CharField()
    country = CharField()
    postalZip = IntegerField(default=11111)
    email = CharField()
    Company = CharField()
    companyFunded = FloatField()
    userID = CharField()
    team = IntegerField(default=0)
    paid = BooleanField()
    date = CharField()
    title = CharField()

def initialize():
    DATABASE.connect()
    DATABASE.close()