from amanuense.texto import Amanuense


new = Amanuense('https://www.jornada.com.mx/ultimas/politica/2020/10/19/lazaro-cardenas-fue-el-consumador-de-los-ideales-de-la-revolucion-amlo-4709.html', tipo='web')
print('\nTEXTO sin procesar')
print(new.texto)

print('\nTEXTO procesado')
new.retirar_muletillas()
print(new.texto)

print('\nConteo de palabras')
new.contar_palabras()
