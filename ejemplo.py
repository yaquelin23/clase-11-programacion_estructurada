Datos_Basicos ={"Nombre":"Juan carlos",
                "Apellidos":"Perez Garcia",
                "DUi":"01025487-9",
                "Fecha_Nacimiento":"23/07/1980",
                "Lugar_Nacimiento":"Soya City",
                "Nacionalidad":"Salvadoreña",
                "Estado_Civil":"Complicado"
                }
print("\nDetalle del Diccionario")
print("===========================")

print("\nClaves del diccionario:",Datos_Basicos.keys())
print("\nValores del diccionario:",Datos_Basicos.values())
print("\nElementos del diccionario:",Datos_Basicos.items())

print("\nInscripcion del curso")
print("================================")

print("\nDatos del participantes")
print("====================================")

print("DUI:",Datos_Basicos["DUI"])
print("Nombre Completo:",Datos_Basicos["Nombres"]+""+Datos_Basicos["Apellidos"])
