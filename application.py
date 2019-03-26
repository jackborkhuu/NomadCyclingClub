from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(self):
  #  return "Hello, this is Nomad Cycling Club official website running on Azure. Site is currently under constructions.."

        username = self.request.get("my_name")
        welcome_string = """<html><body>
                          Hi, this is Nomcad Cycling Club website, {}!
                          </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)