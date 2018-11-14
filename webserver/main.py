#http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nome/<meunome>")
def hello(meunome):
    return "<h1> eu nao acredito</h1>" + meunome

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

