""" Pruebas Persistencia """
import persistencia
def test_guardar_pedido():
  """ Prueba general """
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        persistencia.guardar_pedido("Pedro", "Gil de Diego")
        file.close()
