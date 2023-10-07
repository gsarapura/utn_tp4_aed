from platform import system


class Ticket:
    def __init__(self, registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km):
        self.registro_id = registro_id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia_km = distancia_km
        self.importe_basico = 300

    def __str__(self):
        return f"ID: {self.registro_id}\nPatente: {self.patente}\nTipo de vehiculo: {self.tipo_vehiculo}" \
               f"\nForma de pago: {self.forma_pago}\nPais de la cabina: {self.pais_cabina}\nDistancia en km: " \
               f"{self.distancia_km}"

    def obtener_pos_procedencia(self):
        if len(self.patente) == 7:
            # Argentina
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "0" <= self.patente[2] <= "9":
                        if "0" <= self.patente[3] <= "9":
                            if "0" <= self.patente[4] <= "9":
                                if "A" <= self.patente[5] <= "Z":
                                    if "A" <= self.patente[6] <= "Z":
                                        return 0

            # Bolivia
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "0" <= self.patente[2] <= "9":
                        if "0" <= self.patente[3] <= "9":
                            if "0" <= self.patente[4] <= "9":
                                if "0" <= self.patente[5] <= "9":
                                    if "0" <= self.patente[6] <= "9":
                                        return 1

            # Brasil
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "A" <= self.patente[2] <= "Z":
                        if "0" <= self.patente[3] <= "9":
                            if "A" <= self.patente[4] <= "Z":
                                if "0" <= self.patente[5] <= "9":
                                    if "0" <= self.patente[6] <= "9":
                                        return 2

            # Paraguay
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "A" <= self.patente[2] <= "Z":
                        if "A" <= self.patente[3] <= "Z":
                            if "0" <= self.patente[4] <= "9":
                                if "0" <= self.patente[5] <= "9":
                                    if "0" <= self.patente[6] <= "9":
                                        return 3

            # Uruguay
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "A" <= self.patente[2] <= "Z":
                        if "0" <= self.patente[3] <= "9":
                            if "0" <= self.patente[4] <= "9":
                                if "0" <= self.patente[5] <= "9":
                                    if "0" <= self.patente[6] <= "9":
                                        return 4
        # Chile
        elif len(self.patente) == 6:
            if "A" <= self.patente[0] <= "Z":
                if "A" <= self.patente[1] <= "Z":
                    if "A" <= self.patente[2] <= "Z":
                        if "A" <= self.patente[3] <= "Z":
                            if "0" <= self.patente[4] <= "9":
                                if "0" <= self.patente[5] <= "9":
                                    return 5
        # Otro
        return 6


paises = "Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otro"
tipo_v = "Motocicleta", "Automóvil", "Camión"


def revisar_sin_registros(v_tickets):
    if not v_tickets:
        print("\n", " " * 34, "-" * 3, "No hay registros", "-" * 3)
        return True

    return False


# Punto 1
def dividir_linea(linea):
    """
    Esta función recorta el string de cada línea y devuelve cada tipo de dato.
    :param linea: <str> registro de peaje
    :return: (patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia)
    """

    registro_id = linea[0:10]
    patente = linea[11:17] if linea[10] == " " else linea[10:17]
    tipo_vehiculo = linea[17]
    forma_pago = linea[18]
    pais_cabina = linea[19]
    distancia_km = linea[20:23]

    return int(registro_id), patente, int(tipo_vehiculo), int(forma_pago), int(pais_cabina), float(distancia_km)


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


def crear_arreglo():
    """
    Esta función crea un arreglo de objetos Ticket a partir de un archivo de registro de peajes.

    La función realiza las siguientes tareas:
    1. Determina automáticamente la codificación del archivo de registro en función del sistema operativo.
    2. Abre el archivo de registro y lee cada línea.
    3. Identifica el idioma del registro de peaje a partir de la primera línea.
    4. Divide cada línea en campos utilizando la función dividir_linea.
    5. Crea un objeto Ticket para cada línea y lo agrega a una lista.
    6. Imprime un mensaje indicando que el arreglo se ha creado con éxito.

    :return: Una lista de objetos Ticket que representan los registros de peaje.
    """
    # Chequeo para sistemas Linux - Codificaciones de Windows no válidos para algunos distros de Linux
    ruta_archivo = "peajes-tp3.txt"
    cod = "windows-1252" if system() == "Linux" else None

    v_tickets = []

    idioma = None

    archivo = open(ruta_archivo, encoding=cod)
    for linea in archivo:
        if idioma is None:
            idioma = encontrar_idioma(linea)
            continue

        registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km = dividir_linea(linea)

        ticket = Ticket(registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
        v_tickets.append(ticket)

    archivo.close()

    print("\n", " " * 20, "*" * 3, f"Arreglo creado con éxito | Idioma: {idioma}", "*" * 3)

    return v_tickets


# Punto 2
def crear_rango(comienzo, final):
    """
    Crea una lista de números en forma de cadena dentro del rango indicado, incluyendo los valores de inicio y final.

    :param comienzo: El número de inicio del rango (inclusive).
    :param final: El número final del rango (inclusive).
    :return: Una lista de cadenas que representan los números dentro del rango.
    """

    rango = []
    for i in range(comienzo, final + 1):
        rango.append(str(i))

    return rango


def validar_rango(comienzo, final, mensaje):
    """
    Solicita al usuario un valor dentro de un rango específico y verifica su elección.

    :param comienzo: El número de inicio del rango (inclusive).
    :param final: El número final del rango (inclusive).
    :param mensaje: El mensaje a mostrar al usuario antes de solicitar la entrada.
    :return: Un entero válido dentro del rango especificado.
    """

    op = input(f"\n{mensaje}")
    rango = crear_rango(comienzo, final)

    while op not in rango:
        op = input(f"Por favor, ingrese un entero entre {comienzo} y {final}: ")

    return int(op)


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


# Punto 7
def calcular_importe(cabina_pais, tipo_vehiculo, forma_pago):
    """
    Calcula el importe final a pagar en el peaje
    :param cabina_pais: <str> (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)
    :param tipo_vehiculo: <str> (0: motocicleta, 1: automóvil, 2:camión)
    :param forma_pago: <str> (1: manual, 2 telepeaje)
    :return: <float> importe a pagar
    """
    peaje_general = 300
    peaje_bolivia = 200
    peaje_brasil = 400

    importe_final = 0

    if cabina_pais == 1:
        importe_final += peaje_bolivia
    elif cabina_pais == 2:
        importe_final += peaje_brasil
    else:
        importe_final += peaje_general

    if tipo_vehiculo == 0:
        # Moto: descuento de 50%
        importe_final *= 0.5
    elif tipo_vehiculo == 2:
        # Camión: recarga de 60%
        importe_final *= 1.6
    # Auto: sin recargos

    # Descuento del 10% por telepeaje
    if forma_pago == 2:
        importe_final *= 0.9

    return importe_final


def calcular_vector_acumulador(v):
    v_acumulador = [0] * 3

    for ticket in v:
        pos = ticket.tipo_vehiculo
        v_acumulador[pos] += calcular_importe(ticket.pais_cabina, ticket.tipo_vehiculo, ticket.forma_pago)

    return v_acumulador


def mostrar_acumulado_por_vehiculo(v):
    if revisar_sin_registros(v):
        return

    v_acumulador = calcular_vector_acumulador(v)
    n = len(v_acumulador)

    print(f"\n*** Monto acumulado por cada tipo de vehiculo ***\n")
    for i in range(n):
        print(f"{tipo_v[i]}: ${v_acumulador[i]}")

    return v_acumulador


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


def mostrar_mayor_porcentaje(v_acumulador):
    if not v_acumulador:
        print(f"\nCalcular el punto 7 previamente, por favor.")
    else:
        pos_mayor, porcentaje = vehiculo_mayor_acumulado(v_acumulador)
        print(f"\n*** Mostrando información ***\n")

        print(f"El tipo de vehiculo con mayor monto acumulado: ** {tipo_v[pos_mayor]} **\n\n"
              f"Monto correspondiente: ${v_acumulador[pos_mayor]}\n"
              f"Porcentaje sobre el total facturado: {porcentaje}%\n")


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
