import mysql.connector
from Cliente import cliente

class cajero:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", password="", database="banco"
        )
        
        self.cursor = self.conexion.cursor()
        self.efectivo = self.cargar_efectivo()
        self.clientes = self.cargar_clientes()

    def cargar_efectivo(self):
        self.cursor.execute("SELECT efectivo FROM cajero WHERE id = 1")
        resultado = self.cursor.fetchone()
        return float(resultado[0]) if resultado else 0.0

    def cargar_clientes(self):
        self.cursor.execute("SELECT id, nombre, saldo FROM clientes")
        filas = self.cursor.fetchall()
        lista_clientes = []
        for fila in filas:
            lista_clientes.append(cliente(nombre=fila[1], saldo=fila[2], id_cliente=fila[0]))
        return lista_clientes

    def actualizar_bd(self, cliente):
        self.cursor.execute(
            "UPDATE clientes SET saldo = %s WHERE id = %s",
            (cliente.saldo, cliente.id)
        )
        self.cursor.execute(
            "UPDATE cajero SET efectivo = %s WHERE id = 1",
            (self.efectivo,)
        )
        self.conexion.commit()

    def ingresar_dinero(self, cliente, cantidad):
        if cantidad > 0:
            cliente.ingresar(cantidad)
            self.efectivo += cantidad
            self.actualizar_bd(cliente)
            return "Ingreso realizado correctamente"
        else:
            return "La cantidad debe ser mayor que cero"
        
    def extraer_dinero(self, cliente, cantidad):
        if cantidad <= 0:
            return "La cantidad debe ser mayor que cero"
            
        elif cliente.saldo < cantidad:
            return "No tienes saldo suficiente"
            
        elif self.efectivo < cantidad:
            return "El cajero no tiene efectivo suficiente"
            
        else:
            cliente.extraer(cantidad)
            self.efectivo -= cantidad
            self.actualizar_bd(cliente)
            return "Extracción realizada correctamente"
        
    def consultar_efectivo(self):
        return self.efectivo

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()