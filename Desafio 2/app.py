from flask import Flask

app = Flask("__name__")

@app.route("/")
def home():
    return "<h1>Olá Flask estou rodando no servidor </h1>"