""" API """
from flask import Flask, redirect
from flask import request, Response
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

@app.route("/checksize", methods=["POST"])
def checksize():
    """ Comprueba disponibilidad de un tamaño de pizza"""
    tamano = request.form['p7']
    if tamano=="S":
        mensaje = "No diponible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin':'*'})
    mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin':'*'})
