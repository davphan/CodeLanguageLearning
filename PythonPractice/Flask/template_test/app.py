# Use for starting HTML page!

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello/<userInput>")
def start(userInput):
  return render_template("hello.html", input = userInput)


if __name__ == "__main__":
  app.run(debug = True)