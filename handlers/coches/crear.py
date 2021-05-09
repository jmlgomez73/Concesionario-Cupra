#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.coche import Coche
import time

class CrearHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        valores_plantilla = {
            "usr": users.get_current_user(),
            "login_out_url": users.create_logout_url("/")
        }

        self.response.write(self.jinja.render_template("crear.html", **valores_plantilla))

    def post(self):
        modelo = self.request.get("edModelo", "")
        str_ano = self.request .get("edAno", "")
        cv = self.request.get("edCv", "")
        motor = self.request.get("edMotor", "")
        precio = self.request.get("edPrecio", "")
        foto = ""

        try:
            ano = int(str_ano)
            precio = float(precio)
            cv = int(cv)
        except ValueError:
            ano = 0

        if  modelo == "Ateca":
            foto = "ateca2021.jpg"
        elif modelo == "Born":
            foto = "born.jpg"
        elif modelo == "Formentor":
            foto = "formentor.jpg"
        elif modelo == "Leon":
            foto = "leon.jpeg"
        elif modelo == "Leon e-racer":
            foto = "leon_e_racer.jpg"
        elif modelo == "Tavascan":
            foto = "tavascan.jpg"

        if(not(modelo) or not(ano) or not(cv) or not(motor) or not(precio) or not(foto)):
            return self.redirect("/")
        else:
            coche = Coche(modelo=modelo, ano=ano, cv=cv, motor=motor, foto=foto, precio=precio)
            coche.put()
            time.sleep(1)
            return self.redirect("/coches/listado")

app = webapp2.WSGIApplication([
    ('/coches/crear', CrearHandler)
], debug=True)