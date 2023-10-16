import pickle
import os.path


NOMBRE_ARCHIVO = "peajes-tp4.csv"
NOMBRE_ARCHIVO_BINARIO = "archivo_binario.dat"
V_PAISES_PATENTE = "Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otro"
V_PAISES_CABINA = "Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay"
V_TRANSPORTE = 'Motocicletas', 'Automóviles', 'Camiones'


class Ticket:
    def __init__(self, registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km):
        self.registro_id = registro_id
        self.patente = patente
        self.pais_patente = self.obtener_pais_patente()
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia_km = distancia_km

    def __str__(self):
        return (f"ID: {self.registro_id} - Patente: {self.patente} - País Patente: {self.pais_patente} - Tipo de "
                f"vehiculo: {self.tipo_vehiculo} - Forma de pago: {self.forma_pago} - Pais de la cabina: "
                f"{self.pais_cabina} - Distancia en km: {self.distancia_km}")

    def datos(self):
        return f"ID: {self.registro_id} - Patente: {self.patente} - Pais patente: {self.obtener_pais_patente()} - " \
               f"Tipo de vehículo: {self.tipo_vehiculo} - Forma de pago: {self.forma_pago} - " \
               f"País de la cabina: {self.pais_cabina} - Distancia en km: {self.distancia_km}"

    def obtener_pais_patente(self):
        """
        Esta función devuelve el nombre del pais correspondiente para el string (self) patente.
        :return: <str> (ej.: "Argentina")
        """
        v = [2] * len(self.patente)
        # pais_patente = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros"]
        m_paises = [
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1]
        ]
        # Se crea un arreglo del mismo tamaño del string patente, donde cada posición indica si es letra o número.
        # 0: Letra - 1: Número - 2: Default
        for i in range(len(self.patente)):
            if "A" <= self.patente[i] <= "Z":
                v[i] = 0
            elif "0" <= self.patente[i] <= "9":
                v[i] = 1
        # Comparamos el vector creado con el formato de patente para cada pais, alojado en v_paises.
        for i in range(len(m_paises)):
            if v == m_paises[i]:
                return V_PAISES_PATENTE[i]
        return V_PAISES_PATENTE[6]


def mostrar_menu() -> None:
    print(" ")
    print("-" * 100)
    print(f'{" " * 40}Menú de opciones:')
    print("-" * 100 + "\n")
    print("1. Crear el archivo binario desde 'peajes-tp4.csv'.")

    print("2. Cargar por teclado los datos de un ticket.")

    print("3. Mostrar todos los datos guardados.")

    print("4. Buscar por patente y mostrar la cantidad de registros encontrados.")

    print("5. Buscar por código de identificación de ticket. Se muestra el primero encontrado.")

    print("6. Mostrar tabla: cantidad de vehículos y las respectivas cabinas donde pasaron.")

    print("7. Totalizar tickets por tipos de vehiculo y tickets por pais de cabina.")

    print("8. Mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del archivo "
          "binario. \n   Mostrar los tickets que superen el promedio en forma ascendente.")

    print("9. Salir\n")

    print("-" * 100)


def str_to_ticket(linea):
    """
    Esta función recibe el string de cada registro del archivo binario y retorna el objeto Ticket.
    :param linea: <str> registro de un archivo binario.
    :return: <Ticket> (ticket)
    """
    token = linea.strip()
    token = token.split(",")
    registro_id = int(token[0])
    patente = token[1]
    tipo_vehiculo = int(token[2])
    forma_pago = int(token[3])
    pais_cabina = int(token[4])
    distancia_km = int(token[5])
    ticket = Ticket(registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
    return ticket


def revisar_sin_registros(v_tickets):
    if not v_tickets:
        print("\n", " " * 34, "-" * 3, "No hay registros", "-" * 3)
        return True

    return False


def validar_entero_positivo(mensaje):
    numero = input(mensaje)
    while not numero.isdigit() or numero == '0':
        numero = input('¡Error! El valor debe ser un número entero positivo: ')
    return int(numero)


def validar_rango(minimo, maxim, mensaje):
    """
    Solicita al usuario un valor dentro de un rango específico y verifica su elección.

    :param minimo: El número de inicio del rango (inclusive).
    :param maxim: El número final del rango (inclusive).
    :param mensaje: El mensaje a mostrar al usuario antes de solicitar la entrada.
    :return: Un entero válido dentro del rango especificado.
    """
    error = '¡Error! El valor debe ser entre {} y {}. {}'.format(minimo, maxim, mensaje)
    numero = input(mensaje)
    while (not numero.isnumeric()) or (int(numero) < minimo or int(numero) > maxim):
        numero = input(error)
    return int(numero)


# Punto 1
def confirmar_datos():
    """
    Esta función verifica si existe un archivo grabado previamente para arrojar una advertencia al usuario.
    :return: <bool> True: El usuario confirma borrar datos. False: El usuario cancela la tarea.
    """
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        if size > 0:
            confirma = input("\n¿Esta seguro de continuar? Se borrarán los datos existentes.\n"
                             "Presione 1 para confirmar, 2 para cancelar: ")
            while confirma not in ['1', '2']:
                confirma = input("Presione 1 para confirmar, 2 para cancelar: ")
            if confirma == '1':
                return True
            else:
                return False
    else:
        return True


def grabar_datos(a, ab):
    """
    Esta función crea un archivo binario a partir de un archivo .csv
    :param a: <str> Ruta del archivo .csv
    :param ab: <str> Ruta del archivo binario .dat
    :return: void
    """
    i = 0
    archivo = open(a, "rt")
    binario = open(ab, "wb")
    for linea in archivo:
        i += 1
        if i > 2:
            obj = str_to_ticket(linea)
            pickle.dump(obj, binario)
    archivo.close()
    binario.close()


def crear_archivo():
    """
    Esta función creará un archivo binario de tickets a partir de un archivo .csv dado.
    :return: void
    """
    if confirmar_datos():
        grabar_datos(NOMBRE_ARCHIVO, NOMBRE_ARCHIVO_BINARIO)
        print("\n", " " * 30, "*" * 3, "Archivo creado con éxito.", "*" * 3)
    else:
        print("\n", " " * 32, "-" * 3, "Operación cancelada.", "-" * 3)


# Punto 2
def pedir_datos():
    ticket_id = validar_entero_positivo("\nIngrese el código de identificación de ticket: ")
    patente = input("Ingrese la patente: ")
    while len(patente) == 0:
        patente = input("Ingrese un valor: ")

    tipo_vehiculo = validar_rango(0, 2, "Ingrese el tipo de vehículo: ")
    forma_pago = validar_rango(1, 2, "Ingrese forma pago: ")
    pais = validar_rango(0, 4, "Ingrese el pais: ")
    distancia = validar_rango(0, 50000, "Ingrese la distancia recorrida: ")

    return ticket_id, patente, tipo_vehiculo, forma_pago, pais, distancia


def agregar_ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia):
    archivo = open(NOMBRE_ARCHIVO_BINARIO, "ab")
    ticket = Ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia)
    pickle.dump(ticket, archivo)
    archivo.close()
    print("\n", " " * 30, "*" * 3, "Registro cargado con éxito.", "*" * 3)


# Punto 3
def mostrar_binario():
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            print(ticket.datos())
        archivo.close()
        return 0
    else:
        return 1


# Punto 4
def mostrar_p_binario(p):
    i = 0
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")

        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            if p == ticket.patente:
                i += 1
                print(ticket)
        archivo.close()
    print("\n", " " * 30, "-" * 3, f"Se encontraron {i} registros", "-" * 3)


# punto 5
def buscar_c_binario(c):
    # bandera es True cuando encuentra una coincidencia entre c (valor ingresado) y ticket.registro_id
    bandera = False
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            if c == ticket.registro_id:
                bandera = True
                print(ticket)
                break
        archivo.close()
        if not bandera:
            print("No se encontró el código buscado.")
    else:
        print("No hay datos guardados.")


# punto 6
def crear_matriz_contadora():
    m = [[0] * 3 for _ in range(5)]
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            m[int(ticket.pais_cabina)][int(ticket.tipo_vehiculo)] += 1
        archivo.close()
    else:
        print("No hay datos guardados.")
        return []
    return m


def mostrar_matriz(m):
    """
    Crea una tabla de doble entrada. Tipos de vehículos vs. paises de peajes.
    :param m: <list> Matriz de vehículos (tipo vs. paises)
    :return: None
    """
    guiones = f"{'-' * 61}"

    # Cabecera
    print("\n{:^61}".format("CRUCES POR PEAJES"))
    print(guiones)
    print("|{:^14}|{:^14}|{:^14}|{:^14}|".format("Paises", V_TRANSPORTE[0], V_TRANSPORTE[1], V_TRANSPORTE[2]))
    print(guiones)

    # Cuerpo de tabla
    for pais_cabina in range(len(m)):
        linea = []  # Arreglo temporal al que agregamos los valores que se imprimen en cada línea de la tabla (3)
        for c in range(len(m[pais_cabina])):
            linea.append(m[pais_cabina][c])
        print("|{:^14}|{:^14}|{:^14}|{:^14}|".format(V_PAISES_CABINA[pais_cabina], linea[0], linea[1], linea[2]))
    print(guiones, "\n")


# Punto 7
def mostrar_totales(m):
    a_tipos = [0] * 3
    a_paises_cabina = [0] * 5

    # Sumo valores a los 2 vectores acumuladores
    for pais_cabina in range(len(m)):
        for tipo in range(len(m[pais_cabina])):
            a_paises_cabina[pais_cabina] += m[pais_cabina][tipo]
            a_tipos[tipo] += m[pais_cabina][tipo]

    # Imprimo datos
    print("\n{:^31}".format("TOTALES"))
    print(f"{'-' * 31}")
    print("| Tipo de Veh. |{:^14}|".format("Total"))
    print(f"{'-' * 31}")
    for i in range(len(V_TRANSPORTE)):
        print("|{:^14}|{:^14}|".format(V_TRANSPORTE[i], a_tipos[i]))
    print(f"{'-' * 31}")

    print(f"\n{'-' * 31}")
    print("|{:^14}|{:^14}|".format("Pais", "Total"))
    print(f"{'-' * 31}")
    for i in range(len(V_PAISES_CABINA)):
        print("|{:^14}|{:^14}|".format(V_PAISES_CABINA[i], a_paises_cabina[i]))
    print(f"{'-' * 31}")


def calcular_promedio_km():
    total_km = 0
    total_tickets = 0
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            total_km += ticket.distancia_km
            total_tickets += 1
        archivo.close()
        return total_km // total_tickets
    else:
        return -1


def binary_search(v, x):
    # Búsqueda binaria... asume arreglo ordenado...
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c].distancia_km:
            return c
        if x < v[c].distancia_km:
            der = c - 1
        else:
            izq = c + 1
    # insertar el elemento en v[izq]
    return izq


def buscar_mayores_prom(prom):
    tickets_mayores = []
    # No validamos la existencia del archivo binario porque la validación se realiza al llamar la función.
    size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
    archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
    while archivo.tell() < size:
        ticket = pickle.load(archivo)
        if ticket.distancia_km > prom:
            # Insertar ticket al arreglo tickets_mayores de manera ordenada. De menor a mayor.
            i = binary_search(tickets_mayores, ticket.distancia_km)
            tickets_mayores[i:i] = [ticket]
    archivo.close()
    return tickets_mayores
