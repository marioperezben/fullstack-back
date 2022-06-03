""" API """ 
from flask import Flask, redirect
from flask import request
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza", methods=["POST"])
def hello_post():
    """ Funcion hello post """ 
    nombre = request.form['p1']
    apellido = request.form['p2']
    guardar_pedido(nombre,apellido)
    print("Nombre: " + nombre + " Apellido: " + apellido)
    return redirect("http://localhost:8088/Entrega_final/solicita_pedido.html")
