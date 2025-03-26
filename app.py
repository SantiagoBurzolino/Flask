
from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return """
        <a href="/hola">hola</a> 
        <a href="/chau">chau</a> 
        <a href="/maquina">maquina</a>
        """

@app.route("/dado/<int:caras>")
def dado(caras):
    from random import randint
    numero = randint(1,caras)
    return f"<h2>dado de  {caras} caras, salio {numero}!</h2>"


@app.route("/hola/<string:nombre>")
def saludar_con_nombre(nombre):
    return f"<h2>hola {nombre}!</h2>"


@app.route("/chau")
def despedir():
    return "<h2>chau!</h2>"

@app.route("/maquina")
def decirte():
    return "<h2>maquina, que, sos!</h2>"