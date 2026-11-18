from Cliente import cliente
class cajero:
    
    def __init__(self):
        self.efectivo = 500
        
        self.ana = cliente("Ana")
        self.ana.saldo = 200
        
        self.luis = cliente("Luis")
        self.luis.saldo = 800
        
        self.marta = cliente("Marta")
        self.marta.saldo = 50
        
        self.clientes = [self.ana, self.luis, self.marta]
                

    def ingresar_dinero(self, cliente, cantidad):
        
        if cantidad > 0:
            cliente.ingresar(cantidad)
            self.efectivo += cantidad
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
            return "Extracción realizada correctamente"
        
    def consultar_efectivo(self):
        return self.efectivo