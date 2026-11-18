from Personaje import Personaje
class Guerrero(Personaje):
    
    def __init__(self, nombre, vida, dano_basico):
        super().__init__(nombre, 70, 12)
        self.cargas = 2
        
    def habilidad_especial(self, objetivo):
        if not self.esta_vivo():
            print(self.nombre, "no puede atacar porque esta muerto")
            
        elif self.cargas < 1:
            print("No te quedan cargas")
            
        else: 
            print(self.nombre, "realiza un GOLPE PODEROSO contra ", objetivo.nombre)
            objetivo.recibir_dano(24)
            self.cargas -= 1
            
    def mostrar_estado(self):
        super().mostrar_estado()
        print("Cargas disponibles: ", self.cargas)
        