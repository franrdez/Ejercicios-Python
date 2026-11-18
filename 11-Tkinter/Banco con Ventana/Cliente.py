class cliente:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0
        
    def ingresar(self, saldo):
        self.saldo += saldo
        
    def extraer(self, saldo):
        self.saldo -= saldo
        
    def devolver_saldo(self):
        return self.saldo
    
    def imprimir_saldo(self):
        print(self.nombre, " tiene depositado en su cuenta ", self.saldo, "€")