from ticket import *


def principal():
    v_tickets = []
    v_acumulador_importe = []
    v_registro_id_manual = []
    opc = "0"

    while opc != "9":
        print(" ")
        print("-" * 100)
        print(f'{" " * 40}Menú de opciones:')
        print("-" * 100 + "\n")
        print("1. Crear el archivo binario desde peajes-tp4.csv")

        print("2. Cargar por teclado los datos de un ticket")

        print("3. Mostrar los registros del arreglo (no importa el orden y debe mostrarse también el nombre del país al que pertenece cada patente).")

        print("4. Buscar por patente. Mostrar todos los registros encontrados (al final del listado mostrar una línea adicional indicando cuántos registros se mostraron).")

        print("5. Buscar por ID (código - se muestra el primero encontrado - mostrar mensaje si no hay).")

        print("6. Mostrar cantidad de vehículos de cada país (incluso \'otro\') que pasaron por las cabinas (matriz contador).")

        print("7. Según punto 6, mostar cantidad de vehículos contados por tipo de vehículo posible. Totalizar las filas de esa matriz, y por otro, totalizar las columnas.")

        print("8. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del archivo binario.") 

        print("9. Salir\n")

        print("-" * 100)
        opc = input("Ingrese su elección: ")

        if opc == '1':
            crear_archivo()
        elif opc == "2":
            cit, patente, tipo_vehiculo, forma_pago, pais, distancia = pedir_datos()
            agregar_ticket(cit, patente, tipo_vehiculo, forma_pago, pais, distancia)
        elif opc == "3":
            leer_binario()
        elif opc == "4":
            p = input("Ingrese la patente: ")
            mostrar_p_binario(p)
        elif opc == "5":
            c = input("Ingrese el codigo: ")
            buscar_c_binario(c)
        elif opc == "6":
            c = crear_matriz()
            mostrar_matriz(c)
        elif opc == "7":
            pass
        elif opc == "8":
            pass
        elif opc != "9":
            print("\n", " " * 29, "-" * 3, "Ingrese una opción correcta.", "-" * 3)
        
    print("\n***")



if __name__ == "__main__":
    principal()
