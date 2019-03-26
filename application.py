from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is Nomad Cycling Club official website running on Azure. Site is currently under constructions.."