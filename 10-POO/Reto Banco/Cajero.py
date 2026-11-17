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
    
    def seleccionar_cliente(self):
        try:
            opcion = int(input("Eliga cliente: "))

            if 1 <= opcion <= len(self.clientes):
                self.operaciones(self.clientes[opcion - 1])

            else:
                print("Cliente no válido")

        except ValueError:
            print("Introduce un número válido")
    
    def operaciones(self, cliente):
        opcion = 0
        while opcion != 4:
            print("--- Hola ",cliente.nombre,", ¿Que desea realizar hoy? ---" )
            print("--------------------------------------")
            print("Efectivo disponible en cajero: ",self.efectivo,"€")
            print("--------------------------------------")
            print("1- Ingresar Dinero")
            print("2- Extraer Dinero")
            print("3- Consultar saldo")
            print("4- Volver")
            
            opcion = int(input("Eliga operación: "))
            if opcion == 1:
                self.ingresar_dinero(cliente)
            elif opcion == 2:
                self.extraer_dinero(cliente)
            elif opcion == 3:
                cliente.imprimir_saldo()
            elif opcion == 4:
                print("Volviendo al menú...")
            else:
                print("Opción no válida")
                

    
    def ingresar_dinero(self, cliente):
        cantidad = int(input("Cantidad a ingresar: "))
        
        if cantidad > 0:
            cliente.ingresar(cantidad)
            self.efectivo +- cantidad
            
            print("Ingreso realizado correctamente")
        
        else:
            print("La cantidad debe ser mayor que cero")
            
        
        
    def extraer_dinero(self, cliente):
        cantidad = int(input("Cantidad a extraer: "))
        
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero")
            
        elif cliente.saldo < cantidad:
            print("No tienes saldo suficiente")
            
        elif self.efectivo < cantidad:
            print("El cajero no tiene efectivo suficiente")
            
        else:
            cliente.extraer(cantidad)
            self.efectivo-= cantidad
            print("Extracción realizada correctamente")
        
    def consultar_efectivo(self):
        print("Efectivo disponible en el cajero: ", self.efectivo," €")