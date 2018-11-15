#http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

lista = []

@app.route("/")
def index():
    return render_template("index.html", lista=lista)

@app.route("/nome/<meunome>")
def hello(meunome):
    return "<h1> eu nao acredito</h1>" + meunome

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/formsave", methods=['POST'])
def formsave():
    lista.append(request.form['txtnome'])
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

