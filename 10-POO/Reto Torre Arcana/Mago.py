from Personaje import Personaje
class Mago(Personaje):
    
    def __init__(self, nombre, vida, dano_basico):
        super().__init__(nombre, 50, 8)
        self.mana = 30
        
    def habilidad_especial(self, objetivo):
        if not self.esta_vivo():
            print(self.nombre, " no puede lanzar hechizos porque esta muerto")
        elif self.mana < 15:
            print("No tienes suficiente maná")
        else:
            print(self.nombre, " lanza una BOLA DE FUEGO a ",objetivo.nombre)
            objetivo.recibir_dano(20)
            self.mana -= 15
            
    def mostrar_estado(self):
        super().mostrar_estado()
        print("Maná disponible: ",self.mana) 

    