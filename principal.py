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
        print("-" * 100)
        print("\n1. Crear el archivo binario desde peajes-tp4.csv")

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
            if not v_tickets:
                v_tickets = crear_arreglo()
            else:
                op = input("\n* Advertencia: se borrarán los registros hechos * \n1 Continuar - 0 Volver: ")

                while op not in "0 1":
                    op = input("1 Continuar - 0 Volver: ")

                if op == "1":
                    v_tickets = crear_arreglo()
                else:
                    continue
        elif opc == "2":
            cargar_ticket(v_tickets, v_registro_id_manual)
        elif opc == "3":
            mostrar_registros(v_tickets)
        elif opc == "4":
            buscar_patente_cabina(v_tickets)
        elif opc == "5":
            buscar_registro_id(v_tickets)
        elif opc == "6":
            mostrar_cantidad_patentes(v_tickets)
        elif opc == "7":
            v_acumulador_importe = mostrar_acumulado_por_vehiculo(v_tickets)
        elif opc == "8":
            mostrar_mayor_porcentaje(v_acumulador_importe)
        elif opc != "9":
            print("\n", " " * 29, "-" * 3, "Ingrese una opción correcta.", "-" * 3)
        
    print("\n***")



if __name__ == "__main__":
    principal()
