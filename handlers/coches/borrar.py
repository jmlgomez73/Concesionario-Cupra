#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from model.coche import Coche
from model.configuraciones import Configuracion
from model.extras import Extras
import time

class BorrarHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        coche = Coche.recupera(self.request)
        extra = Extras.query(Extras.clave_coche == coche.key)
        try:
            configuracion = Configuracion.query(Configuracion.extras == extra.get().key)
            extra.get().key.delete()
            time.sleep(1)
            configuracion.get().key.delete()
            time.sleep(1)
        except:
            pass

        coche.key.delete()
        time.sleep(1)

        return self.redirect("/coches/listado")

app = webapp2.WSGIApplication([
    ('/coches/borrar', BorrarHandler)
], debug=True)