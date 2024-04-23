from flask import Flask, redirect, url_for
app = Flask(__name__)

# Routing
@app.route("/hello/")
def hello_world():
  return "Hello World"

@app.route("/hello/<name>")
def hello_name(name):
  """Prints Hello <name>. Example of using Path Parameters.

  Args:
      name (any): path parameter returned in return string.

  Returns:
      String: string formated as "Hello <name>!"
  """
  return f"Hello {name}!"

@app.route("/number/<int:favNum>")
def favNumber(favNum):
  """Prints "My favorite number is <favNum>". Example of setting type to path parameter.

  Args:
      favNum (int): input integer

  Returns:
      String: output string
  """

  return f"My favorite number is {favNum}"

@app.route("/floaters/<num>")
def favNumEver(num):
  """Example for redirect(), url_for(), and try/except. If an int, redirects to
     the url with function favNumber(). If a float, returns and string, and if
     anything else, returns a different string.

  Args:
      num (any): input.

  Returns:
      string: output strign depending on input type (int, float, or other).
  """

  try:
    floatedNum = float(num)
    if floatedNum % 1 == 0:
      print("its an int")
      return redirect(url_for("favNumber", favNum = num))
    else:
      return f"My favorite EVER number is not an integer, but {num}!"
  except ValueError:
    return f"This isn't a number, but i love {num}"




if __name__ == "__main__":
  app.run(debug = True)