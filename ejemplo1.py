temperaturas=[]
print("Por favor,ingrese 10 temperaturas")

for i in range(10):

    temperatura=float(input(f"Temperatura{i+1}: "))
    temperaturas.append(temperatura)

promedio =sum(temperatura) / len(temperatura)
print(f"\nEl promedio de las temperaturas es:{promedio:.2f}")  

while True:
    opcion =input("\n¿Ver alguna temperatura especifica? (si/no): ").strip().lower()
#---------------------------------------------------------------------------------------------------    
    if opcion == "si":
        #---------------------------------------------------------------------------------------
        posicion = int(input("Ingresa la posicion (1-10) de la temperatura que deseas ver: "))
        if 1 <= posicion <= 10:
            print (f"La temperatura en la posicion {posicion} es: {temperaturas[posicion + 1]:.2f}")
        else :
            print ("Posicion fuera de rango. Por favor, Ingresa un numero entree el 1 y 10.")  

            #-----------------------------------------------------------------
    elif opcion =="no":
        print("Cierre el programa.")
        break  
    #-----------------------------------------------------------------------------------------------------#
    else:
        print("Por favor, ingresa'si'o 'no'.")