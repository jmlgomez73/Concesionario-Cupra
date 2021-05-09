from google.appengine.ext import ndb
from model.coche import Coche

class Extras(ndb.Model):
    aire = ndb.BooleanProperty()
    rueda = ndb.BooleanProperty()
    android = ndb.BooleanProperty()
    camara = ndb.BooleanProperty()
    techo = ndb.BooleanProperty()
    sonido = ndb.BooleanProperty()
    total = ndb.FloatProperty()
    clave_coche = ndb.KeyProperty(kind = Coche)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id_extra"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe = id).get()


