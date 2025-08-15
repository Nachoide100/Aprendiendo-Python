import random

desayuno = [
    {"nombre": "Leche desnatada", "calorias": 50, "categoria": "Lácteos"},
    {"nombre": "Yogur natural", "calorias": 70, "categoria": "Lácteos"},
    {"nombre": "Huevos revueltos", "calorias": 200, "categoria": "Proteínas"},
    {"nombre": "Tostadas de pan integral", "calorias": 100, "categoria": "Cereales"},
    {"nombre": "Fruta fresca", "calorias": 50, "categoria": "Vegetales"}
]

comida = [
    {"nombre": "Pollo asado", "calorias": 300, "categoria": "Proteínas"},
    {"nombre": "Pescado a la plancha", "calorias": 250, "categoria": "Proteínas"},
    {"nombre": "Ensalada de atún", "calorias": 200, "categoria": "Vegetales"},
    {"nombre": "Arroz integral", "calorias": 150, "categoria": "Cereales"},
    {"nombre": "Judías verdes", "calorias": 50, "categoria": "Vegetales"}
]

cena = [
    {"nombre": "Sopa de verduras", "calorias": 100, "categoria": "Vegetales"},
    {"nombre": "Ensalada mixta", "calorias": 150, "categoria": "Vegetales"},
    {"nombre": "Tortilla de patatas", "calorias": 250, "categoria": "Proteínas"},
    {"nombre": "Queso fresco", "calorias": 100, "categoria": "Lácteos"},
    {"nombre": "Frutos secos", "calorias": 150, "categoria": "Vegetales"}
]

def mostrar_alimentos(): #función que mueste los alimentos disponibles para cada comida
    print("\nAlimentos disponibles para el desayuno: ")
    for i in desayuno: #bucle que recorra la lista desayuno imprimiendo el diccionario en su interior
        print(f" - {i["nombre"]} ({i["calorias"]} calorías, {i["categoria"]})") #cada i es un diccionario individual dentro de la lista
    for i in comida: #""
        print(f" - {i["nombre"]} ({i["calorias"]} calorías, {i["categoria"]})")
    for i in cena: #""
        print(f" - {i["nombre"]} ({i["calorias"]} calorías, {i["categoria"]})")
def agregar_alimento(): #función que permite añadir un alimentos a cualquiera de las listas
    while True: #bucle que permite al usuario añadir tantos alimentos como desea
        respuesta = input("¿Quiere añadir algún alimento a la lista de desayuno, comida o cena? (s/n)")
        if respuesta == "s": #condición de que la respuesta sea afirmativa para proseguir
            print("Opciones disponibles: \n1. Desayuno\n2. Comida\n3. Cena")
            lista = input("¿A qué lista quieres añadir el alimento? (1-3): ") #variables que almacenan los datos introducidos por el usuario
            nombre = input("Introduce el nombre del alimento: ")
            calorias = int(input("Introduce las calorías del alimento: "))
            print("Opciones disponibles: \n1. Proteínas\n2. Lácteos\n3. Cereales\n4. Vegetales")
            categorias = ['Proteínas', 'Lácteos', 'Cereales', 'Vegetales'] #creación de una nueva lista con las distintas categorías
            categoria = categorias[int(input("¿A qué categoría?: ")) - 1] #-1 porque el índice empieza en 0
            
            nuevo = {"nombre": nombre, "calorias": calorias, "categoria": categoria} #creación de un nuevo diccionario que almacene los datos
            #condiciones segun la eleccion del usuario que añaden ese nuevo diccionario con los datos a la lista que haya elegido
            if lista == '1': 
               desayuno.append(nuevo)
            elif lista == '2':
               comida.append(nuevo)
            elif lista == '3':
               cena.append(nuevo)
        if respuesta != "s":
            break

def limites_caloricos(): #función que establece los límites calóricos de cada comida
    limite_desayuno = int(input("Introduce el número máximo de calorías para el desayuno: ")) #se solicitan por teclado
    limite_comida = int(input("Introduce el número máximo de calorías para la comida: "))
    limite_cena = int(input("Introduce el número máximo de calorías para la cena: "))
    return limite_desayuno, limite_comida, limite_cena #la función devuelve esos datos

def generar_menu(lista, limite, usados): #función que genera el menú aleatorio
    intentos = 0 #variable que registrará el número de intenos 
    while intentos < 500: #bucle que intentará hasta 500 veces generar un menú válido
        seleccion = random.sample(lista, min(3, len(lista))) #función que elegira 3 alimentos y en caso de que no haya tres pues los que haya
        total = sum(a["calorias"] for a in seleccion) #variable que almacena el total de calorias de los alimentos que aparezcan
        if total <= limite and all(a["nombre"] not in usados for a in seleccion): #condicion de que las calorías no superen el límite y los alimentos que salgan no hayan salido
           for a in seleccion: 
               usados.add(a["nombre"]) #añade los alimentos a la lista de usados
           return seleccion, total
        intentos += 1 #va sumando un intento cada vez que genera un menú
    return[], 0 #para el caso en el que no sea capaz de generar ninguno
def mostrar_menu(nombre_comida, items, total, limite): #función que muestra el menú resultante con sus características
    print(f"\n{nombre_comida.capitalize()} con un total de {total} calorías (máximo de {limite})")
    for a in items: 
        print(f"- {a["nombre"]} ({a["calorias"]} calorías)")

def main(): 
    while True: #bucle principal hasta que el usuario diga que está satisfecho con el programa
        mostrar_alimentos() #muestra las opciones
        agregar_alimento() #permite añadir algún alimento
        limite_desayuno, limite_comida, limite_cena = limites_caloricos()

        usados = set() #creación de un conjunto vacío en el que vamos añadiendo los alimentos ya usados

        desayuno_menu, cal_d = generar_menu(desayuno, limite_desayuno, usados) #creación de un menu para cada comida
        comida_menu, cal_c = generar_menu(comida, limite_comida, usados)
        cena_menu, cal_cn = generar_menu(cena, limite_cena, usados)

        print("\nMenú diario:") #impresión del menu al usuario
        mostrar_menu("desayuno", desayuno_menu, cal_d, limite_desayuno)
        mostrar_menu("comida", comida_menu, cal_c, limite_comida)
        mostrar_menu("cena", cena_menu, cal_cn, limite_cena)

        if input("¿Estás satisfecho con este menú? (s/n): ").lower() == 's': #condición que sale del bucle en caso de que el usuario este conforme
            break

main()