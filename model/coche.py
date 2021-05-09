from google.appengine.ext import ndb


class Coche(ndb.Model):
    modelo = ndb.StringProperty(required = True)
    cv = ndb.IntegerProperty()
    ano = ndb.IntegerProperty()
    motor = ndb.StringProperty()
    foto = ndb.BlobProperty()
    precio = ndb.FloatProperty(required = True)


    @staticmethod
    def recupera(req):

        try:
            key = req.GET["key"]
        except KeyError:
            key = ""

        if key:
            clave = ndb.Key(urlsafe = key)
            coche = clave.get()
            return coche
        else:
            print("ERROR: coche no encontrado")