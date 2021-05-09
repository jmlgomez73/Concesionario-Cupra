#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from model.extras import Extras
import time
from model.configuraciones import Configuracion

class BorrarHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        extra = Extras.recupera(self.request)
        configuracion = Configuracion.query(Configuracion.extras == extra.key)

        extra.key.delete()
        time.sleep(1)
        configuracion.get().key.delete()
        time.sleep(1)
        return self.redirect("/configuracion/listado_user")

app = webapp2.WSGIApplication([
    ('/configuracion/borrar', BorrarHandler)
], debug=True)