from threading import Thread
from flask import Flask, jsonify, redirect, render_template
import json

app = Flask('')

@app.route("/")
def index():

  return render_template("index.html")

@app.route('/api')
def api():

  with open("data/bots.json", "r") as f:

    api = json.load(f)

  return jsonify(api)

@app.route("/examples")
def examples():

  return render_template("examples.html")

@app.route("/mobile")
def mobile():
  
  return render_template("mobile/index.html")

@app.route("/mobile/examples")
def mobile_examples():
  
  return render_template("mobile/examples.html")

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
