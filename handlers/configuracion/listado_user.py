#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.configuraciones import Configuracion

class ListadoUserHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        admin = False
        if users.is_current_user_admin():
            admin = True
        email = users.get_current_user().email()
        coches = []
        extras = []
        configuraciones = Configuracion.query(Configuracion.email == email)
        for configuracion in configuraciones:
            extras.append(configuracion.extras.get())

        for extra in extras:
            coches.append(extra.clave_coche.get())


        valores_plantilla = {
            "usr": users.get_current_user(),
            "login_out_url": users.create_logout_url("/"),
            "coches": coches,
            "extras": extras,
            "admin": admin
        }

        self.response.write(jinja.render_template("listado_configuraciones.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/configuracion/listado_user', ListadoUserHandler)
], debug=True)