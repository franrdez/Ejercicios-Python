class cliente:
    
    def __init__(self, nombre, saldo=0, id_cliente=None):
        self.id = id_cliente
        self.nombre = nombre
        self.saldo = float(saldo)
        
    def ingresar(self, saldo):
        self.saldo += saldo
        
    def extraer(self, saldo):
        self.saldo -= saldo
        
    def devolver_saldo(self):
        return self.saldo
    
    def imprimir_saldo(self):
        print(self.nombre, " tiene depositado en su cuenta ", self.saldo, "€")