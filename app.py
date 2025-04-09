
from flask import Flask,url_for


app = Flask(__name__)


@app.route("/")
def principal():
    return """
        <a href="/hola">hola</a> 
        <a href="/chau">chau</a>
        <br> 
        <a href="/maquina">maquina</a>
        <br>
        """


@app.route("/")
def main():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/Minion.png")

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar_Dado</a>
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