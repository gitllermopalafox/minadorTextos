from amanuense.texto import Amanuense
new = Amanuense('plano.txt', tipo='txt')
print('\nTEXTO sin procesar')
print(new.texto)

print('\nTEXTO procesado')
new.retirar_muletillas()
print(new.texto)

print('\nConteo de palabras')
new.contar_palabras()
