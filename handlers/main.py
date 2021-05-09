#!/usr/bin/env python

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.coche import Coche

class MainHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.jinja = jinja2.get_jinja2(app=self.app)

    def get(self):
        usr = users.get_current_user()
        coches = Coche.query()
        admin = False
        if users.is_current_user_admin():
            admin = True

        if usr:
            login_out_url = users.create_logout_url("/")
            self.response.write(self.jinja.render_template("index.html", usr = usr, login_out_url = login_out_url, coches = coches, admin = admin))
        else:
            login_out_url = users.create_login_url("/")
            self.response.write(self.jinja.render_template("index.html", usr = usr, login_out_url = login_out_url, coches = coches, admin = admin))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
