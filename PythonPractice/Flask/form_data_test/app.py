from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def init():
  return render_template("index.html")

@app.route("/result", methods = ["POST", "GET"])
def result():
  if request.methods == "POST":
    inputs = request.form
