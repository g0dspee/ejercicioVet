import os
import random


mascotas = {}

def fin():
    input("Presione enter para continuar...")
    os.system('cls')

def ingresarId():
    while True:
        try:
            idMascota = input("Ingrese ID de la mascota (5 caracteres numéricos): ")
            if len(idMascota) != 5:
                print("El código debe tener 5 caracteres")
            elif not idMascota.isnumeric():
                print("El código debe ser numérico")
            elif idMascota in mascotas:
                print("El ID ya está registrado.")
            else:
                return idMascota
        except ValueError:
            print("Por favor, ingrese un dato válido.")
    fin()



def ingresarNombre(texto): #función unificada para ingresar nombre de mascota y dueño
    while True:
        try:
            nombre = input(f"Ingrese el {texto} de la mascota: ").strip()
            if nombre:
                return nombre
            else:
                print(f"El {texto} no puede estar vacío.")
        except ValueError:
            print("Por favor, ingrese un dato válido.")
    fin()


def ingresarTipoMascota():
    while True:
        try:
            tipoMascota = input("Ingrese el tipo de mascota (Perro o Gato): ").strip().capitalize()
            if tipoMascota in ['Perro', 'Gato']:
                return tipoMascota
            else:
                print("Error, ingrese una opción válida.")
        except ValueError:
            print("Por favor, ingrese un dato válido.")
    fin()

def registroMascotas():
    idMascota = ingresarId()
    nombreMascota = ingresarNombre("nombre")
    duenno = ingresarNombre("nombre del dueño")
    tipoMascota = ingresarTipoMascota()
    datosMascota = {'nombre': nombreMascota, 'duenno': duenno, 'tipo': tipoMascota}
    mascotas[idMascota] = datosMascota
    print("Mascota registrada exitosamente.")
    fin()

def listarRegistros():
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        print("REGISTROS:")
        for idMascota, datosMascota in mascotas.items():
            print(f"ID Mascota: {idMascota} - Nombre: {datosMascota['nombre']} - Dueño: {datosMascota['duenno']} - Tipo de mascota: {datosMascota['tipo']}")
    fin()

def buscarId():
    idMascota = input("Ingrese el ID de la mascota que desea buscar: ")
    if idMascota in mascotas:
        datosMascota = mascotas[idMascota]
        print(f"ID Mascota: {idMascota} - Nombre: {datosMascota['nombre']} - Dueño: {datosMascota['duenno']} - Tipo de mascota: {datosMascota['tipo']}")
    else:
        print(f"No se encontró la mascota con ID {idMascota}")
    fin()

def reporteMascota():
    while True:
        try:
            tipoMascota = input("¿Reportes de 1.Perros 2.Gatos? ")
            if tipoMascota == '1':
                tipoMascotaElegido = 'Perro'
                break
            elif tipoMascota == '2':
                tipoMascotaElegido = 'Gato'
                break
            else:
                print("Error, ingrese una opción válida.")
        except ValueError:
            print("Por favor, ingrese un dato válido.")
    print(f"\nREPORTES DE {tipoMascotaElegido.upper()}:\n")
    numMascotas = 0
    for idMascota, datosMascota in mascotas.items():
        if datosMascota['tipo'] == tipoMascotaElegido:
            numVacunasFaltantes = random.randint(1, 10)
            print(f"ID Mascota: {idMascota}")
            print(f"Nombre: {datosMascota['nombre']}")
            print(f"Tipo: {datosMascota['tipo']}")
            print("Dueño de la Mascota:")
            print(f"Sr/a: {datosMascota['duenno']}")
            print(f"A su mascota le faltan {numVacunasFaltantes} vacunas\n")
            numMascotas += 1
    print(f"Hay en total {numMascotas} {tipoMascotaElegido}s Registrados\n")
    fin()

def menu():
    while True:
        opcion = input(f"Bienvenido a la clínica Yasha. Ingrese una opción:\n1. Grabar/Registrar Mascota\n2. Listar Todos los registros\n3. Buscar Mascota\n4. Imprimir Reportes por tipo mascota\n5. Salir\n").strip()
        if opcion == '1':
            registroMascotas()
        elif opcion == '2':
            listarRegistros()
        elif opcion == '3':
            buscarId()
        elif opcion == '4':
            reporteMascota()
        elif opcion == '5':
            print("Hasta luego.")
            break
        else:
            print("Error, ingrese una opción válida.\n")

menu()