""" Persistencia """
def guardar_pedido(nombre,apellidos):
    """ Funcion guardad pedido """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
