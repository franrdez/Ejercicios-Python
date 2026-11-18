class Personaje:
    
    def __init__(self, nombre, vida, dano_basico):
        self.nombre = nombre
        self.vida = vida
        self.dano_basico = dano_basico
        
    def atacar(self, objetivo):
        if self.esta_vivo():
            print(self.nombre, " ataca a", objetivo.nombre)
            objetivo.recibir_dano(self.dano_basico)
        else:
            print(self.nombre, " no puede atacar porque esta muerto.")
            
    
    def recibir_dano(self, cantidad):
        self.vida = max(0, self.vida - cantidad)
        
    def esta_vivo(self):
        return self.vida > 0
        
    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self.vida} HP")
        