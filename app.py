
from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return """
        <a href="/hola">hola</a> 
        <a href="/chau">chau</a> 
        <a href="/maquina">maquina</a>
        """
@app.route("/hola")
def saludar():
    return "<h2>hola, Clase!</h2>"


@app.route("/chau")
def despedir():
    return "<h2>chau!</h2>"

@app.route("/maquina")
def decirte():
    return "<h2>maquina, que, sos!</h2>"