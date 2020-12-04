from amanuense.texto import Amanuense


while True:

    while True:
        print("""
        1) Página web
        2) Archivo de texto (.txt)
        3) Ingresar manualmente el texto

        Elige una opción:
         """)
        eleccion = input("  >")

        if eleccion == '1':
            print("Ingresa URL")
            tipo = 'web'
            break
        elif eleccion == '2':
            print("Ingresa dirección al documento")
            tipo = 'txt'
            break
        elif eleccion == '3':
            print("Ingresa texto manualmente")
            tipo = 'string'
            break
        else:
            print("Opción no válida")

    entrada = input("   >")

    new = Amanuense(entrada,tipo=tipo)
    new.retirar_muletillas()
    new.contar_palabras()
    #print(new.texto)
    print('\nBigramas')
    new.detectar_bigramas()

    print('\nTrigramas')
    new.detectar_trigramas()
