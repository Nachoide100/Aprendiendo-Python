import random #importamos la librería random para la tirada del dado

class Dado(): #creamos la clase dado
    def __init__(self, caras = 6): #definimos el constructor con el atributo caras que en nuestro caso será igual a 6
        self._caras = caras
    @property #métodos getter y setter para el atributo
    def caras(self): 
        return self._caras
    @caras.setter
    def caras(self, new_caras):
        self._caras = new_caras
    def tirar(self): #método específico que devolverá un entero entre 1 y el número de caras(6)
        return random.randint(1, self._caras) 

class Personaje(): #creamos la clase padre personaje
    def __init__(self, nombre, vida, ataque, defensa, dado): #método constructor
        self._nombre = nombre #definimos los atributos
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa
        self._dado = dado #objeto de la clase dado
        if ataque < 0:
            raise ValueError #validamos los atributos
        if defensa < 0:
            return ValueError
    @property #métodos getter y setter para cada atributo
    def nombre(self):
            return self._nombre
    @nombre.setter
    def nombre(self, new_nombre):
            self._nombre = new_nombre
    @property
    def vida(self):
            return self._vida
    @vida.setter
    def vida(self, new_vida):
            self._vida = new_vida
    @property
    def ataque(self):
            return self._ataque
    @ataque.setter
    def ataque(self, new_ataque):
            self._ataque = new_ataque
    @property
    def defensa(self):
            return self._defensa
    @defensa.setter
    def defensa(self, new_defensa):
            self._defensa = new_defensa
    @property
    def dado(self):
            return self._dado
    @dado.setter
    def dado(self, new_dado):
            self._dado = new_dado
    def estar_vivo(self): #método específico para saber que los personajes siguen con vida
            return self._vida > 0
    def atacar(self): #método específico para atacar
            num_impactos = 0 #iniciamos un contador
            for x in range(self._ataque): #dependiendo del ataque del personaje hace más tiradas o menos
                tirada = self._dado.tirar()
                if tirada > 3: #con dado de 6 caras cuenta impacto a partir de sacar mas de un 3
                    num_impactos += 1
            return num_impactos
    def __str__(self): #definimos la salida por pantalla
            return f"{self._nombre} | Vida: {self._vida} | Ataque: {self._ataque} | Defensa: {self._defensa}"
        
            
class Barbaro(Personaje): #creamos la clase hija barbaro
    def __init__(self, nombre, vida, ataque, defensa): #definimos el constructor
        super().__init__(nombre, vida, ataque, defensa, Dado()) #heredamos atributos de la clase padre
    def defender(self, num_impactos): #método específico de la clase
        bloqueos = 0 #iniciamos el contador de bloqueos
        for x in range(self._defensa): 
            tirada = self._dado.tirar()
            if tirada > 4: #la defensa del bárbaro es a partir de 4
                bloqueos += 1
            daño = max(0, num_impactos - bloqueos) #daño resultante de los impactos que hemos podido bloquear. Maximo 0 de daño, no puede haber -2.
            self._vida -= daño #restamos el daño a la vida del personaje
        return bloqueos, daño
    def __str__(self): #definimos la salid por pantalla
        return f"Bárbaro --- {super().__str__()}"

class Momia(Personaje): #creamos la clase hija barbaro
    def __init__(self, nombre, vida, ataque, defensa): #definimos el constructor
        super().__init__(nombre, vida, ataque, defensa, Dado()) #heredamos atributos de la clase padre
    def defender(self, num_impactos): #método específico de la clase
        bloqueos = 0 #iniciamos el contador de bloqueos
        for x in range(self._defensa): 
            tirada = self._dado.tirar()
            if tirada == 6: #la defensa de la momia solo es si saca un 6
                bloqueos += 1
            daño = max(0, num_impactos - bloqueos) #daño resultante de los impactos que hemos podido bloquear. Maximo 0 de daño, no puede haber -2.
            self._vida -= daño #restamos el daño a la vida del personaje
        return bloqueos, daño
    def __str__(self): #definimos la salida por pantalla
        return f"Momia --- {super().__str__()}"
    
def jugar_partida(barbaro, momia, turnos_max): #definimos la función que contiene la lógica de la partida
    if not isinstance(turnos_max, int): #comprobamos que el número de turnos establecido es posible
        return ValueError
    for turno in range(1, turnos_max + 1): #bucle que recorre los turnos
        print(f"\n#TURNO {turno} -> B vs M")
        impactos_b = barbaro.atacar() #recogemos el número de impactos que realiza el barbaro
        bloqueos_m, daño_m = momia.defender(impactos_b) #recogemos el daño que le hace a la momia los impactos del bárbaro
        if daño_m == 0: #posibilidades después del turno de ataque del barbaro
            print(f"La momia {momia.nombre} bloqueó todos los ataques y queda con {momia.vida} puntos de vida.")
        else: 
            print(f"La momia {momia.nombre} no pudo bloquear {daño_m} impactos y queda con {momia.vida} puntos de vida.")
        if not momia.estar_vivo(): #comprobar que la momia ha quedado viva después del turno y mostrarlo porpantalla
            print(f"GANADOR BÁRBARO {barbaro.nombre}")
            break #salimos del bucle si llegamos a este punto
            print(f"--- {barbaro}")
            print(f"--- {momia}")
        print(f"\nTURNO {turno} -> M vs B") #turno de ataque de la momia
        impactos_m = momia.atacar() #recogemos los ataques de la momia
        bloqueos_b, daño_b = barbaro.defender(impactos_m) #recogemos el daño sufrido después de los ataques de la momia)
        if daño_b == 0: #evaluamos las posibilidades después del turno de la novia
            print(f"El bárbaro {barbaro.nombre} bloqueó todos los ataques y queda con {barbaro.vida} de vida")
        else:
            print(f"El bárbaro {barbaro.nombre} no pudo bloquear {daño_b} impactos y queda con {barbaro.vida} de vida")
        if not barbaro.estar_vivo(): #comprobamos si el bárbaro sigue vivo
            print(f"\n> GANADOR MOMIA {momia.nombre}")
            break #en esta situación se sale del bucle
            print(f">>> {barbaro}")
            print(f">>> {momia}")
    print("\nFIN DE LA PARTIDA") #posibilidades si salimos del bucle for y no ha habido ganador
    if barbaro.estar_vivo() and momia.estar_vivo():
        print("TABLAS")
    print(f"--- {barbaro}")
    print(f"--- {momia}")

barbaro = Barbaro("Nacho", 5, 4, 2)
momia = Momia("Miriam", 10, 2, 4)

jugar_partida(barbaro, momia, 10)