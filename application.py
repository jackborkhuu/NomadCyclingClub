from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
 #   return "Hello, this is Nomad Cycling Club official website running on Azure. Site is currently under constructions.."
    name = request.args.get("name", "World")
    return f'Hello, {name}!'