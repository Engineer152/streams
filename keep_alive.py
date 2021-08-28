from flask import Flask, render_template,redirect,request,make_response
from flask_classful import FlaskView
from threading import Thread
import os
import mechanize
from urllib.parse import urljoin

app = Flask('')

@app.route('/')
def main():
  return '<html><head><title>LIVE TWITCH STREAM HOSTING</title></head><body bgcolor="white"  link ="cyan" vlink="red"><font color="black" size ="4"><h2>LIVE TWITCH STREAM HOSTING</h2></font>Type: the name of your streamer after the end of the url with a "/"</body></html>'

@app.route('/<streamer>',methods = ['POST', 'GET'])
def stream(streamer):
  resp = make_response(render_template('stream.html',streamer=streamer))
  resp.set_cookie('login','engineer15',domain='.twitch.tv')
  resp.set_cookie('auth-token','2rqbpqo2n2ahz9s255cxx7bgyc3mww',domain='.twitch.tv')
  return resp

# @app.route('/t/test',methods = ['POST', 'GET'])
# def test():
#   resp = make_response(redirect('http://twitch.tv'))
#   login=request.cookies.get('login')
#   auth=request.cookies.get('auth-token')
#   print(login)
#   print(auth)
#   return resp

# class GetSite(object):

#     def get_stream(self, base_url, email, password):
#         self.base_url = base_url
#         self.login_page = urljoin(self.base_url, 'login')
#         self.email = email
#         self.password = password
#         self.browser = mechanize.Browser()
#         self.browser.set_handle_robots(False)

#     def login(self):
#         self.browser.open(self.login_page)
#         # select the first (and only) form and log in
#         self.browser.select_form(nr=0)
#         self.browser.form['email'] = self.email 
#         self.browser.form['password'] = self.password 
#         self.browser.submit()
    
#     @app.route('/<streamer>',methods = ['POST', 'GET'])
#     def stream(self,streamer):
#       resp = make_response(render_template('stream.html',streamer=streamer))
#       return self.browser.resp

# base_url = r'https://twitch.tv'
# email = os.environ['twitch_user']
# password = os.environ['twitch_password']
# sd = GetSite.get_stream(base_url, email, password)
# GetSite.register(app)

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()