def mostrar_menu():
    print("\nBienvenido a la universidad. ¿Qué información necesitas?")
    print("1. Fecha de inscripción")
    print("2. Inicio de ciclo")
    print("3. Finalización de ciclo")
    print("4. Salir")

def obtener_respuesta(opcion):      
    if opcion == "1":
        return "La fecha de inscripción para el próximo ciclo es del 1 al 15 de diciembre."
    elif opcion == "2":
        return "El inicio del ciclo académico es el 15 de enero."
    elif opcion == "3":
        return "La finalización del ciclo académico es el 30 de junio."
    elif opcion == "4":
        return "Gracias por preferirnos. ¡Hasta luego!"
    else:
        return "Opción no válida. Por favor, elige una opción del 1 al 4."

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        respuesta = obtener_respuesta(opcion)
        print(respuesta)
        if opcion == "4":
            break

if __name__ == "__main__":
    main()

