import pickle
import os.path

NOMBRE_ARCHIVO = "peajes-tp4.csv"
NOMBRE_ARCHIVO_BINARIO = "archivo_binario.dat"


class Ticket:
    def __init__(self, registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km):
        self.registro_id = registro_id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia_km = distancia_km

    def __str__(self):
        return f"ID: {self.registro_id} - Patente: {self.patente} - Tipo de vehiculo: {self.tipo_vehiculo} - " \
               f"Forma de pago: {self.forma_pago} - Pais de la cabina: {self.pais_cabina} - Distancia en km: " \
               f"{self.distancia_km}"

    def datos(self):
        return f"ID: {self.registro_id} - Patente: {self.patente} - Pais patente: {self.obtener_pais_patente()} - " \
               f"Tipo de vehículo: {self.tipo_vehiculo} - Forma de pago: {self.forma_pago} - " \
               f"País de la cabina: {self.pais_cabina} - Distancia en km: {self.distancia_km}"

    def obtener_pais_patente(self):
        """
        Esta función devuelve el nombre del pais correspondiente para el string self.patente.
        :return: <str> (ej.: "Argentina")
        """
        v = [2] * len(self.patente)
        pais_patente = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otros"]
        v_paises = [
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1]
        ]
        # Se crea un arreglo del mismo tamaño del string patente, donde cada posición indica si es letra o número.
        # 0: Letra  -  1: Número  -  2: Default
        for i in range(len(self.patente)):
            if "A" <= self.patente[i] <= "Z":
                v[i] = 0
            elif "0" <= self.patente[i] <= "9":
                v[i] = 1
        # Comparamos el vector creado con el formato de patente para cada pais, alojado en v_paises.
        for i in range(len(v_paises)):
            if v == v_paises[i]:
                return pais_patente[i]
        return pais_patente[6]


def mostrar_menu() -> None:
    print(" ")
    print("-" * 100)
    print(f'{" " * 40}Menú de opciones:')
    print("-" * 100 + "\n")
    print("1. Crear el archivo binario desde 'peajes-tp4.csv'.")

    print("2. Cargar por teclado los datos de un ticket.")

    print(f"3. Mostrar todos los datos guardados.")

    print(f"4. Buscar por patente y mostrar todos los registros encontrados.")

    print(f"5. Buscar por Código de Identificación de Ticket. (Se muestra el primero encontrado)")

    print(f"6. Mostrar tabla: cantidad de vehículos y las respectivas cabinas donde pasaron.")

    print(f"7. Totalizar tickets por tipos de vehiculo y tickets por pais de cabina.")

    print(f"8. Mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del archivo "
          f"binario. \n   Mostrar los tickets que superen el promedio en forma ascendente.")

    print("9. Salir\n")

    print("-" * 100)


def str_toticket(linea):
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


paises = "Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otro"
tipo_v = "Motocicleta", "Automóvil", "Camión"


def revisar_sin_registros(v_tickets):
    if not v_tickets:
        print("\n", " " * 34, "-" * 3, "No hay registros", "-" * 3)
        return True

    return False


def validar_rango(minimo, maximo, mensaje):
    """
    Solicita al usuario un valor dentro de un rango específico y verifica su elección.

    :param minimo: El número de inicio del rango (inclusive).
    :param maximo: El número final del rango (inclusive).
    :param mensaje: El mensaje a mostrar al usuario antes de solicitar la entrada.
    :return: Un entero válido dentro del rango especificado.
    """
    error = 'Error!!! El valor debe ser entre {} y {}. {}'.format(minimo, maximo, mensaje)
    numero = input(mensaje)
    while not numero.isdigit():
        numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = int(input(error))
    return numero


# Punto 1
def confirmar_datos():
    """
    Esta función verifica si existe un archivo grabado previamente para arrojar una advertencia al usuario.
    :return: <bool> True: El usuario confirma borrar datos. False: El usuario cancela la tarea.
    """
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        if size > 0:
            confirmacion = int(input("¿Estás seguro de continuar? Se borrarán los datos existentes.\n"
                                     "Presiona '1' para confirmar, '2' para cancelar: "))
            while confirmacion not in [1, 2]:
                confirmacion = int(input("Presiona '1' para confirmar, '2' para cancelar: "))
            if confirmacion == 1:
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
            obj = str_toticket(linea)
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
    else:
        print(f"\n{'*' * 3} Operación cancelada. {'*' * 3}")


# Punto 2
def pedir_datos():
    id = input("Ingrese el Código de Identificación de Ticket: ")
    while not id.isnumeric() or id == "0":
        id = input("Ingrese el CIT: ")
    id = int(id)
    patente = input("\nIngrese la patente: ")
    while len(patente) == 0:
        patente = input("Ingrese un valor: ")
    tipo_vehiculo = validar_rango(0, 2, "Ingrese el tipo de vehículo: ")
    forma_pago = validar_rango(1, 2, "Ingrese forma pago: ")
    pais = validar_rango(0, 4, "Ingrese el pais: ")
    distancia = validar_rango(0, 50000, "Ingrese la distancia recorrida: ")
    return id, patente, tipo_vehiculo, forma_pago, pais, distancia


def agregar_ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia):
    archivo = open(NOMBRE_ARCHIVO_BINARIO, "ab")
    ticket = Ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia)
    pickle.dump(ticket, archivo)
    archivo.close()


# Punto 3
def leer_binario():
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
    print(f"Se encontraron {i} registros")


# punto 5
def buscar_c_binario(c):
    # bandera es True cuando encuentra una coincidencia entre c y ticket.registro_id
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
def crear_matriz():
    m = [[0] * 3 for i in range(5)]
    if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
        size = os.path.getsize(NOMBRE_ARCHIVO_BINARIO)
        archivo = open(NOMBRE_ARCHIVO_BINARIO, "rb")
        while archivo.tell() < size:
            ticket = pickle.load(archivo)
            m[int(ticket.pais_cabina)][int(ticket.tipo_vehiculo)] += 1
        archivo.close()
    else:
        print("No hay datos guardados.")
    return m


def mostrar_matriz(m):
    """
    Crea una tabla de doble entrada. Tipos de vehiculos vs paises de peajes.
    :param m: <list> Matriz de vehiculos (tipo vs paises)
    :return: None
    """
    guiones = f"{'-'* 61}"
    v_paises = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay"]
    t_vehiculos = ['Motocicletas', 'Automóviles', 'Camiones']

    # Cabecera
    print("\n{:^61}".format("CRUCES POR PEAJES"))
    print(guiones)
    print("|{:^14}|{:^14}|{:^14}|{:^14}|".format("Paises", t_vehiculos[0], t_vehiculos[1], t_vehiculos[2]))
    print(guiones)

    # Cuerpo de tabla
    for pais_cabina in range(len(m)):
        linea = [] # Arreglo temporal al que agregamos los valores que se imprimen en cada linea de la tabla (3)
        for c in range(len(m[pais_cabina])):
            linea.append(m[pais_cabina][c])
        print("|{:^14}|{:^14}|{:^14}|{:^14}|".format(v_paises[pais_cabina], linea[0], linea[1], linea[2]))
    print(guiones, "\n")


# Punto 7
def mostrar_totales(m):
    v_paises = ["Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay"]
    t_vehiculos = ['Motocicletas', 'Automóviles', 'Camiones']
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
    for i in range(len(t_vehiculos)):
        print("|{:^14}|{:^14}|".format(t_vehiculos[i],a_tipos[i]))
    print(f"{'-' * 31}")

    print(f"\n{'-' * 31}")
    print("|{:^14}|{:^14}|".format("Pais", "Total"))
    print(f"{'-' * 31}")
    for i in range(len(v_paises)):
        print("|{:^14}|{:^14}|".format(v_paises[i], a_paises_cabina[i]))
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
        # ¿División entera o división común? -------------------------------------------------------
        return total_km // total_tickets
    else:
        return -1


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


def binary_search(v, x):
    # busqueda binaria... asume arreglo ordenado...
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


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        h //= 3


def encontrar_idioma(primera_linea):
    """
    Esta función determina el idioma según la primera línea de un registro de peaje.
    :param primera_linea: <str> primera línea del registro de peaje
    :return: <str> idioma encontrado "Portugués", "Español" o "Idioma no encontrado" si no se reconoce
    """

    if "PT" in primera_linea:
        return "Portugués"
    elif "ES" in primera_linea:
        return "Español"
    else:
        return "Idioma no encontrado"


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def cargar_valor_valido(mensaje, tipo):
    """
    Solicita al usuario un valor válido (entero o flotante) y verifica su elección.

    :param mensaje: El mensaje a mostrar al usuario antes de solicitar la entrada.
    :param tipo: El tipo de valor esperado ('entero' o 'flotante').
    :return: Un valor válido del tipo especificado.
    """
    op = input(f"\n{mensaje}")

    if tipo == 'entero':
        while not op.isnumeric():
            op = input("Por favor, ingrese un entero: ")
        return int(op)
    elif tipo == 'flotante':
        while not is_float(op):
            op = input("Por favor, ingrese un entero o flotante con punto: ")
        return round(float(op), 2)


def revisar_id(v_registro_id_manual):
    registro_id = cargar_valor_valido("Ingrese el ID: ", "entero")
    while registro_id in v_registro_id_manual:
        registro_id = cargar_valor_valido("ID ya ingresado, ingrese otro: ", "entero")
    v_registro_id_manual.append(registro_id)

    return registro_id


def cargar_ticket(v_tickets, v_registro_id_manual):
    print("\nCargar ticket:")

    # Ingresar ID, no importa qué cantidad tenga
    registro_id = revisar_id(v_registro_id_manual)

    patente = input("\nIngrese la patente: ")
    while len(patente) == 0:
        patente = input("Ingrese un valor: ")

    tipo_vehiculo = validar_rango(0, 2, "Ingrese tipo de vehiculo (0: motocicleta, 1: automóvil, 2: camión): ")
    forma_pago = validar_rango(1, 2, "Ingrese forma de pago (1: manual, 2: telepeaje): ")
    pais_cabina = validar_rango(0, 4, "Ingrese país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay,"
                                      " 4: Uruguay): ")

    distancia_km = cargar_valor_valido("Ingrese los kilómetros recorridos desde la cabina anterior "
                                       "(0 si es la primera): ", "flotante")

    ticket = Ticket(registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
    v_tickets.append(ticket)

    print("\n", " " * 30, "*" * 3, "Registro cargado con éxito.", "*" * 3)


# Punto 3
def ordenar_ascendente_dir(v_tickets):
    largo = len(v_tickets)

    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if v_tickets[i].registro_id > v_tickets[j].registro_id:
                v_tickets[i], v_tickets[j] = v_tickets[j], v_tickets[i]


def mostrar_registros(v_tickets):
    if revisar_sin_registros(v_tickets):
        return

    ordenar_ascendente_dir(v_tickets)
    for t in v_tickets:
        print(f"\n{t}")
        pos_pais = t.obtener_pos_procedencia()
        print(f"País de procedencia: {paises[pos_pais]}")


# Punto 4
def buscar_patente_cabina(v_tickets):
    if revisar_sin_registros(v_tickets):
        return

    print("\nBúsqueda:")

    patente = input("Ingrese la patente: ")
    pais_cabina = validar_rango(0, 4, "Ingrese país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay,"
                                      " 4: Uruguay): ")

    # Búsqueda secuencial
    for t in v_tickets:
        if t.patente == patente and t.pais_cabina == pais_cabina:
            print("\n", " " * 35, "*" * 3, "Patente encontrada", "*" * 3)
            print(t)
            pos_pais = t.obtener_pos_procedencia()
            print(f"País de procedencia: {paises[pos_pais]}")
            return

    print("\n", " " * 30, "-" * 3, "Sin resultado disponible.", "-" * 3)


# Punto 5
def buscar_registro_id(v_tickets):
    if revisar_sin_registros(v_tickets):
        return

    registro_id = cargar_valor_valido("Ingrese el ID del registro por buscar: ", "entero")

    for c in v_tickets:
        if c.registro_id == registro_id:
            print("\n", " " * 35, "*" * 3, "Patente encontrada", "*" * 3)
            print(f"Forma de pago anterior: {c.forma_pago}")

            if c.forma_pago == 2:
                c.forma_pago = 1
                print(f"\n{c}")
                pos_pais = c.obtener_pos_procedencia()
                print(f"País de procedencia: {paises[pos_pais]}")
                return

            if c.forma_pago == 1:
                c.forma_pago = 2
                print(f"\n{c}")
                pos_pais = c.obtener_pos_procedencia()
                print(f"País de procedencia: {paises[pos_pais]}")
                return

    print("\n", " " * 29, "-" * 3, "Ningún registro con ese ID.", "-" * 3)


# Punto 6
def mostrar_cantidad_patentes(v):
    if revisar_sin_registros(v):
        return

    m_conteo = [0] * 7

    for ticket in v:
        pos = ticket.obtener_pos_procedencia()
        m_conteo[pos] += 1

    n = len(m_conteo)
    print("\n", " " * 35, "*" * 3, "Conteo de patentes", "*" * 3)
    for i in range(n):
        print(f"{paises[i]}: {m_conteo[i]}")


# Punto 8
def vehiculo_mayor_acumulado(v_acumulador):
    n = len(v_acumulador)
    monto_mayor, monto_total, porcentaje = 0, 0, 0
    pos_mayor = 0

    # Recorre el vector acumulador y determina qué tipo de vehículo tiene el monto mayor
    for i in range(n):
        monto_total += v_acumulador[i]
        if v_acumulador[i] > monto_mayor:
            monto_mayor = v_acumulador[i]
            pos_mayor = i

    if monto_mayor != 0:
        porcentaje = round(monto_mayor * 100 / monto_total, 2)

    return pos_mayor, porcentaje


# Punto 9
def mostrar_distancia(tickets):
    if revisar_sin_registros(tickets):
        return

    suma = 0

    for ticket in tickets:
        suma += ticket.distancia_km
    promedio = suma / len(tickets)

    contador = 0
    for ticket in tickets:
        if ticket.distancia_km >= promedio:
            contador += 1

    print(f"Promedio de distancias recorridas: {round(promedio, 2)}")
    print(f"Cantidad de vehículos que supera el promedio: {contador}")
