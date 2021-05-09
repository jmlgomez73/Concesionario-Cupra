#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.extras import Extras
import time

class ModificarHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)

        extra = Extras.recupera(self.request)
        print(extra)
        coche = extra.clave_coche.get()
        admin = False
        if users.is_current_user_admin():
            admin = True
        valores_plantilla = {
            "usr": users.get_current_user(),
            "login_out_url": users.create_logout_url("/"),
            "coche": coche,
            "extra": extra,
            "admin": admin
        }

        if valores_plantilla["usr"]:
            self.response.write(jinja.render_template("modificar_configuracion.html", **valores_plantilla))
        else:
            return self.redirect("/")

    def post(self):
        extras = Extras.recupera(self.request)

        edAire = self.request.get("edAire", "")
        edRueda = self.request .get("edRueda", "")
        edAndroid = self.request.get("edAndroid", "")
        edCamara = self.request.get("edCamara", "")
        edTecho = self.request.get("edTecho", "")
        edSonido = self.request.get("edSonido", "")
        total = self.request.get("total", "")

        aire = rueda = android = camara = techo = sonido = False

        if edAire:
            aire = bool(edAire)
        if edRueda:
            rueda = bool(edRueda)
        if edAndroid:
            android = bool(edAndroid)
        if edCamara:
            camara = bool(edCamara)
        if edTecho:
            techo = bool(edTecho)
        if edSonido:
            sonido = bool(edSonido)
        if total:
            try:
                total = float(total)
            except ValueError:
                total = 0

        extras.aire = aire
        extras.rueda = rueda
        extras.android = android
        extras.camara = camara
        extras.techo = techo
        extras.sonido = sonido
        extras.total = total
        extras.put()
        time.sleep(1)
        return self.redirect("/configuracion/listado_user")


app = webapp2.WSGIApplication([
    ('/configuracion/modificar', ModificarHandler)
], debug=True)