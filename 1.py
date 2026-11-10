# Sistema de objetos extraviados en un museo
# Definición de funciones.
def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1. Registrar objeto encontrado.")
    print("2. Mostrar objetos pendientes de entrega.")
    print("3. Buscar objetos por palabra clave.")
    print("4. Entregar objeto a su propietario.")
    print("5. Mostrar resumen por sala y estado.")
    print("6. Salir.")

def solicitar_entero(mensaje,minimo,maximo):
    while True:
        try:
            entero = int(input(mensaje))
            if maximo > minimo:
                if entero >= minimo and  entero <= maximo:
                    break
                else:
                    print(f"¡Valor ingresado inválido! Debe ingresar un valor entre {minimo} y {maximo}.")
            elif maximo <= minimo:
                if entero >= minimo:
                    break
                else:
                    print(f"¡Valor ingresado inválido! Debe ingresar un valor mayor o igual a {minimo}.")
        except ValueError:
            print("¡Valor ingresado inválido! Debe ingresar un valor entero.")
    return entero

def normalizar_texto(texto):
    aceptado = False
    contador = 0
    for caracter in texto:
        if caracter == " ":
            contador = contador + 1
    if contador != len(texto):
        aceptado = True
    
    if aceptado:
        texto = texto.strip()
        texto = texto.lower()
    else:
        print("No puede ingresar un texto vacío.")
    return aceptado,texto

def registrar_objeto(objetos,salas):
    largo_min = 5
    validado = False
    aceptado = False
    while not validado:
        while not aceptado:
            descripcion = input("Ingrese la descripción del objeto: ")
            if len(descripcion) >= largo_min:
                aceptado,descripcion = normalizar_texto(descripcion)
            else:
                print("¡Descripción inválida! Debe tener al menos 5 caracteres.")
                while len(descripcion) < largo_min:
                    descripcion = input("Ingrese la descripción del objeto: ")
                    aceptado,descripcion = normalizar_texto(descripcion)
            validado = True
    
    aceptado = False
    validado = False
    while not validado:
        while not aceptado:
            sala = input("Ingrese la sala donde se perdió (Historia, Ciencia, Arte): ").lower()
            if sala in salas:
                aceptado,sala = normalizar_texto(sala)
            else:
                print("La sala ingresada no existe.")
                while sala not in sala:
                    sala = input("Ingrese la sala donde se perdió: ").lower()
                    aceptado,sala = normalizar_texto(sala)
            validado = True
    
    aceptado = False
    validado = False
    largo_fecha = 10
    while not validado:
        while not aceptado:
            fecha = input("Ingrese la fecha en la que se perdió el objeto: ")
            if len(fecha) >= largo_fecha:
                contador = fecha.count("-")
                if contador == 2:
                    aceptado,fecha = normalizar_texto(fecha)
                else:
                    print("¡Fecha inválida! Debe seguir el formato DD-MM-AAAA.")
            else:
                print("¡Fecha inválida! Debe tener al menos 10 caracteres.")
                while len(descripcion) < largo_min:
                    descripcion = input("Ingrese la descripción del objeto: ")
                    aceptado,descripcion = normalizar_texto(descripcion)
            validado = True
    identificador = 100 + len(objetos)

    datos = {
        "ID":identificador,
        "descripción":descripcion,
        "sala":sala,
        "fecha":fecha,
        "estado":"PENDIENTE",
        "receptor":"NINGUNO"
    }
    objetos.append(datos)

def mostrar_pendientes(objetos):
    if len(objetos) > 0:
        for indice in range(len(objetos)):
            if objetos[indice]["estado"] == "PENDIENTE":
                print(f"ID: {objetos[indice]["ID"]}")
                print(f"Descripción del objeto: {objetos[indice]["descripción"]}")
                print(f"Sala: {objetos[indice]["sala"]}")
                print(f"Fecha: {objetos[indice]["fecha"]}")
    else:
        print("No se han registrado objetos perdidos pendientes.")

def buscar_objetos(objetos):
    if len(objetos)> 0:
        validado = False
        aceptado = False
        largo_min = 3
        while not validado:
            while not aceptado:
                palabra = input("Ingrese palabra clave a buscar: ")
                if len(palabra) >= largo_min:
                    aceptado,palabra = normalizar_texto(palabra)
                else:
                    print(f"¡Palabra inválida! Debe tener al menos {largo_min} caracteres.")
                    while len(palabra) < largo_min:
                        palabra = input("Ingrese la descripción del objeto: ")
                        aceptado,palabra = normalizar_texto(palabra)
                validado = True
        contador = 0
        for indice in range(len(objetos)):
            if palabra in objetos[indice]["descripción"]:
                contador = contador + 1
                print(f"Coincidencia {contador}")
                print(f"ID: {objetos[indice]["ID"]}")
                print(f"Descripción del objeto: {objetos[indice]["descripción"]}")
                print(f"Sala: {objetos[indice]["sala"]}")
                print(f"Fecha: {objetos[indice]["fecha"]}")
    else:
        print("No se han registrado objetos pérdidos.")

def entregar_objeto(objetos):
    if len(objetos) > 0:
        mensaje = "Ingrese el identificador del objeto: "
        identificador = solicitar_entero(mensaje,100,0)
        aceptado = False
        validado = False
        largo_min = 3
        while not validado:
            while not aceptado:
                nombre = input("Ingrese el nombre del receptor: ")
                if len(nombre) >= largo_min:
                    aceptado,nombre = normalizar_texto(nombre)
                else:
                    print(f"¡Nombre inválido! Debe tener al menos {largo_min} caracteres.")
                    while len(nombre) < largo_min:
                        nombre = input("Ingrese el nombre del receptor: ")
                        aceptado,nombre = normalizar_texto(nombre)
                validado = True

        encontrado = False
        lugar = 0
        for indice in range(len(objetos)):
            if objetos[indice]["ID"] == identificador:
                encontrado = True
                lugar = indice

        if encontrado:
            if objetos[lugar]["estado"] == "PENDIENTE":
                objetos[lugar]["estado"] = "ENTREGADO"
                objetos[lugar]["receptor"] = f"{nombre.title()}"
            else:
                print("Lo sentimos, el objeto figura como entregado.")
        else:
            print("No se encontraron coincidencias.")
    else:
        print("No se han registrado objetos pérdidos.")

def mostrar_resumen(objetos,salas):
    if len(objetos) > 0:
        for sala in salas:
            total_entregados = 0
            total_pendientes = 0
            total = 0
            print(f"Sala: {sala}")
            for indice in range(len(objetos)):
                if objetos[indice]["sala"] == sala:
                    if objetos[indice]["estado"] == "PENDIENTE":
                        total_pendientes = total_pendientes + 1
                    elif objetos[indice]["estado"] == "ENTREGADO":
                        total_entregados = total_entregados + 1

            total = total_entregados + total_pendientes
            if total > 0:
                entregas = total_entregados/total
                entregas = entregas * 100
            else:
                entregas = 0
            print(f"Total pendientes: {total_pendientes}")
            print(f"Total entregados: {total_entregados}")
            print(f"Porcentaje de entrega: {entregas}%")
    else:
        print("No se han registrado objetos pérdidos.")

# ciclo principal
salas = ["historia","ciencia","arte"]
objetos = []
menu = True
while menu:
    mostrar_menu()
    mensaje = "Seleccione opción: "
    decision = solicitar_entero(mensaje,1,6)
    if decision == 1:
        registrar_objeto(objetos,salas)
    elif decision == 2:
        mostrar_pendientes(objetos)
    elif decision == 3:
        buscar_objetos(objetos)
    elif decision == 4:
        entregar_objeto(objetos)
    elif decision == 5:
        mostrar_resumen(objetos,salas)
    elif decision == 6:
        break