from Cajero import cajero
class main:

    def __init__(self):
        self.cajero = cajero()
        
    def menu(self):
        opcion = 0
        while opcion != 2:
            print("Bienvenido al Cajero Poligonero")
            print("---Eliga la Opción---")
            print("1- Elegir cliente")
            print("2- Salir")
            opcion = int(input("Ingrese Opción: "))
            if opcion == 1:
                self.cajero.seleccionar_cliente()
            elif opcion == 2:
                print("Hasta pronto Pobretón")
            else:
                print("Opción No válida")
                
main = main()
main.menu()