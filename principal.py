from ticket import *


def principal():
    tickets_may_prom = []
    opc = "0"

    while opc != "9":
        mostrar_menu() # Aqui se imprimen las opciones
        opc = input("Ingrese su elección: ")
        if opc == '1':
            crear_archivo()
        elif opc == "2":
            cit, patente, tipo_vehiculo, forma_pago, pais, distancia = pedir_datos()
            agregar_ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia)
        elif opc == "3":
            r = leer_binario()
            if r == 1:
                print("No hay datos registrados. Utilice las opciones 1 o 2.")
        elif opc == "4":
            p = input("Ingrese la patente: ")
            mostrar_p_binario(p)
        elif opc == "5":
            id = input("Ingrese el Código de Identificación de Ticket: ")
            while not id.isnumeric() or id == "0":
                id = input("Ingrese el CIT: ")
            id = int(id)
            buscar_c_binario(id)
        elif opc == "6":
            m = crear_matriz()
            mostrar_matriz(m)
        elif opc == "7":
            m = crear_matriz()
            mostrar_totales(m)
        elif opc == "8":
            r = calcular_promedio_km()
            if r == -1:
                print("No se encontró el archivo de datos. Utilice las opciones 1 o 2.")
            else:
                tickets_may_prom = buscar_mayores_prom(r)
                for i in tickets_may_prom:
                    print(i)
                print(f"\nEl promedio de distancia recorrida de todos los tickets es {r} kms.")
                print(f"\nCantidad de tickets con distancia recorrida superior al promedio: {len(tickets_may_prom)} tickets.")
        elif opc != "9":
            print("\n", " " * 29, "-" * 3, "Ingrese una opción correcta.", "-" * 3)
    print("\n***")


if __name__ == "__main__":
    principal()
