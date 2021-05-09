from google.appengine.ext import ndb
from model.extras import Extras

class Configuracion(ndb.Model):
    email = ndb.StringProperty(required = True)
    extras = ndb.KeyProperty(kind = Extras)