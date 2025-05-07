from flask import Flask,url_for,render_template
import sqlite3


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


db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"



@app.route("/sqlite/delete/<int:id>")
def testDelete(id):
    abrirConexion()
    #insertamos de forma segura
    db.execute("DELETE FROM usuarios WHERE id=?", (id,))
    db.commit()
    cerrarConexion()
    return f"Se borro el id {id} en la tabla usuarios."

@app.route("/sqlite")
def mostrarUsuarios():
    abrirConexion()
    cursor = db.execute("SELECT COUNT (usuario) AS cantidad FROM usuarios; ")
    res = cursor.fetchone()
    c = res['cantidad']
    cerrarConexion()
    return f"hay {c} registros en la tabla de usuarios"

@app.route("/crearUsuario/<string:nombre>/<string:email>")
def testCrear(nombre,email):
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?);"
    cursor.execute(consulta, (nombre, email))
    db.commit()
    cerrarConexion()
    return f"Se Registro agregado ({nombre})"


@app.route("/crearUsuario")
def testCrearif():
    nombre = "Pedro"
    email = "Pedro@etec.uba.ar"
    if nombre == "Pedro":
        abrirConexion()
        cursor = db.cursor()
        consulta = "INSERT INTO usuarios(usuario, email) VALUES (?, ?);"
        cursor.execute(consulta, (nombre, email))
        db.commit()
        cerrarConexion()  
        return f"Registro agregado ({nombre})"
    else:
        return "Ya esta agregado el usuario"
    

@app.route("/sqlite/usuario/<int:id>")
def seleccionindividual(id):
    conexion = abrirConexion()
    db = conexion.cursor()
    cursor = db.execute("SELECT * FROM usuarios WHERE id=? ", (id,))
    resultado = db.fetchone()
    cerrarConexion()
    fila = dict(resultado)
    return str(fila) 



@app.route("/sqlite/modif/<string:nombre>/<string:email>")
def modifemail(nombre,email):
    abrirConexion()
    cursor = db.cursor()
    consulta = "UPDATE usuarios SET email = ? WHERE usuario = ?;"
    cursor.execute(consulta, (email, nombre))
    db.commit()
    cerrarConexion()
    return f"Se modifico el email de usuario ({email})"


@app.route("/mostrarUsuario/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, direccion, telefono FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    direccion = None
    telefono = None
    if res != None:
        usuario=res["usuario"]
        email=res["email"]
        direccion=res["direccion"]
        telefono=res["telefono"]
    return render_template("Templates.html", id=id, usuario=usuario, email=email, direccion=direccion, telefono=telefono)    

@app.route("/mostrar-planilla-usuario/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email FROM usuarios WHERE id = ?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario=res["usuario"]
        email=res["email"]
    return render_template("Templates.html", id=id, usuario=usuario, email=email)   

@app.route("/mostrar-usuarios-full")   
def datos_ planilla():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario FROM usuarios ")
    res =  