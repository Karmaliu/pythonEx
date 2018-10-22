from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")

def index():
  name = request.args.get("name", 'Nobody')

  if name:
    greeting = f"hello,{name}"
  else:
    greeting = "Hello World"

  return greeting

if __name__ == "__main__":
  app.run()