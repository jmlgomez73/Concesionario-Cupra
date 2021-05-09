#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.coche import Coche

class ListadoHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        coches = Coche.query()

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "coches": coches,
            "usr": users.get_current_user(),
            "login_out_url": users.create_logout_url("/")
        }

        self.response.write(jinja.render_template("listado.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/coches/listado', ListadoHandler)
], debug=True)