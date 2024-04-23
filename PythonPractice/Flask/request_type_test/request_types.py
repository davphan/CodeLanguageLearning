from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/start")
def init():
  return render_template("request_type.html")

@app.route("/success/<name>/<color>")
def success(name, color):
  return render_template("return.html", name = name, color = color)

@app.route("/input", methods = ["POST"])
def enter():
  name = request.form["name"]
  color = request.form["color"]
  return redirect(url_for("success", name = name, color = color))


if __name__ == "__main__":
  app.run(debug = True)