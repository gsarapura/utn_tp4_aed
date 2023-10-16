from ticket import *


def principal():
    matriz_cont = []
    opc = "0"

    while opc != "9":
        mostrar_menu()  # Aquí se imprimen las opciones

        opc = input("Ingrese su elección: ")
        if opc == '1':
            crear_archivo()

        elif opc == "2":
            cit, patente, tipo_vehiculo, forma_pago, pais, distancia = pedir_datos()
            agregar_ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia)

        elif opc == "3":
            r = mostrar_binario()
            if r == 1:
                print("No hay datos registrados. Utilice las opciones 1 o 2.")

        elif opc == "4":
            if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
                p = input("Ingrese la patente: ")
                mostrar_p_binario(p)
            else:
                print("No hay datos registrados. Utilice las opciones 1 o 2.")

        elif opc == "5":
            if os.path.exists(NOMBRE_ARCHIVO_BINARIO):
                ticket_id = validar_entero_positivo("Ingrese el código de identificación de ticket: ")
                buscar_c_binario(ticket_id)
            else:
                print("No hay datos registrados. Utilice las opciones 1 o 2.")

        elif opc == "6":
            matriz_cont = crear_matriz_contadora()
            if matriz_cont:
                mostrar_matriz(matriz_cont)

        elif opc == "7":
            if matriz_cont:
                mostrar_totales(matriz_cont)
            else:
                print("No hay matriz calculada. Utilice la opción 6.")

        elif opc == "8":
            r = calcular_promedio_km()
            if r == -1:
                print("No se encontró el archivo de datos. Utilice las opciones 1 o 2.")
            else:
                tickets_may_prom = buscar_mayores_prom(r)
                for i in tickets_may_prom:
                    print(i)
                print(f"\nEl promedio de distancia recorrida de todos los tickets es {r} kms.")
                print(f"\nCantidad de tickets con distancia recorrida superior al promedio: {len(tickets_may_prom)}"
                      f" tickets.")

        elif opc != "9":
            print("\n", " " * 29, "-" * 3, "Ingrese una opción correcta.", "-" * 3)
    print("\n***")


if __name__ == "__main__":
    principal()
