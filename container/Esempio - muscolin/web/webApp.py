from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))

@app.route("/corsi")
def corsi():
    elencoCorsi=requests.get("http://xxx.xxx.xxx.xxx:5000/corsi").json()
    return(render_template("corsi.html",elencoCorsi=elencoCorsi))

@app.route("/sedi")
def sedi():
    return(render_template("sedi.html"))
