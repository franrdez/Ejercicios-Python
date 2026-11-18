from Mago import Mago
from Guerrero import Guerrero
from Personaje import Personaje

class Main:

    def __init__(self):

        self.personajes = [
            Mago("Gandalf", 50, 8),
            Guerrero("Conan", 70, 12)
        ]

        self.guardian = Personaje("Guardian de Piedra", 60, 10)
    
    def seleccionar_personaje(self):

        print("--- ELIGE TU PERSONAJE ---")

        for i in range(len(self.personajes)):
            print(i + 1, "-", self.personajes[i].nombre)

        try:
            opcion = int(input("Elige personaje: "))

            if 1 <= opcion <= len(self.personajes):
                return self.personajes[opcion - 1]

            else:
                print("Personaje no válido")
                return None

        except ValueError:
            print("Debes introducir un número")
            return None
        
    def combate(self, personaje):

        opcion = 0

        while personaje.esta_vivo() and self.guardian.esta_vivo() and opcion != 4:

            print("\n--- TORRE ARCANA ---")
            print("1 - Atacar")
            print("2 - Habilidad especial")
            print("3 - Consultar estado")
            print("4 - Salir")

            opcion = input("Elige una opción: ")

            turno = False

            if opcion == "1":

                personaje.atacar(self.guardian)
                turno = True

            elif opcion == "2":

                vida_guardian = self.guardian.vida

                personaje.habilidad_especial(self.guardian)

                if self.guardian.vida < vida_guardian:
                    turno = True

            elif opcion == "3":

                personaje.mostrar_estado()
                self.guardian.mostrar_estado()

            elif opcion == "4":

                print("Has decidido abandonar la torre")

            else:

                print("Opción no válida")

            if turno and self.guardian.esta_vivo():

                print("\n¡El guardián contraataca!")
                self.guardian.atacar(personaje)
        
    
    def resultado(self, personaje):
        print("\n--- FIN DE LA PARTIDA ---")

        if not personaje.esta_vivo():
            print("¡Has sido derrotado por el guardián!")

        elif not self.guardian.esta_vivo():
            print("¡Enhorabuena! Has superado la Torre Arcana.")

        else:
            print("Has abandonado la Torre Arcana.")

        print("\nEstado final:")
        personaje.mostrar_estado()
        self.guardian.mostrar_estado()
        
    def iniciar(self):
        personaje = self.seleccionar_personaje()
        
        if personaje is not None:
            self.combate(personaje)
            self.resultado(personaje)


juego = Main()
juego.iniciar()