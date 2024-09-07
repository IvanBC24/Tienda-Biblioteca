
class Ventas:
    def __init__(self):
        self.total_ventas = 0

    def vender_libro(self, precio):
        self.total_ventas += precio

    def mostrar_total_ventas(self):
        return f"Total de ventas: ${self.total_ventas:.2f}"
