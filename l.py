from amanuense.texto import Amanuense
new = Amanuense("""

Xiaomi presentó la serie Mi 10T que está conformada por dos equipos, el Mi 10T y el Mi 10T Pro, que evolucionan lo que presentó la marca con el Mi 10 de hace unos meses, pero con mejoras en la cámara, el procesamiento y la batería.

“Estamos liderando en cinco países de América Latina y nuestro objetivo es seguir manteniendo la relación de calidad y precio como nuestro objetivo principal para seguir creciendo y con esta nueva serie se mantiene este objetivo”, precisó en el evento de prensa, Zoe Zhang, líder regional de marketing en Xiaomi.

La marca domina mercados como el de Colombia, Perú o Chile pero en México aún no logra entrar en el top tres de marcas dominantes, donde Samsung, Motorola y Huawei mantienen cautivo al 65.9% del mercado de smartphones, de acuerdo con The Competitive Intelligence Unit, pero donde la relación entre precio y calidad de producto puede jugar a favor de la empresa de origen chino.

El par de equipos están enfocados en un segmento de gama media alta y gama alta con herramientas destacadas como una cámara principal de 108 MP, soporte de redes 5G y baterías de alto poder de 5,000 mAh.

En cuanto a las especificaciones del Mi 10T cuenta con un conjunto de cámaras con un lente principal de 108 MP, un lente más de 64 MP, un gran angular de 13 MP y un macro de 5MP, además de una cámara frontal de 20 MP. La batería es de 5,000 mAh, con carga rápida de 33W y cuenta con un lector de huellas lateral, además de dual SIM.

En cuanto a precio, éste costará 13,999 pesos y estará disponible a partir del 10 de diciembre en Telcel.

Por su parte el Mi 10T Pro tendrá una cámara principal de 108 MP, un procesador Snapdragon 865 y una velocidad en su pantalla de 144 Hz, además de una batería de 5,000 mAh, 8 GB de RAM y 128 GB de almacenamiento. En este caso el equipo costará 16,999 pesos y por tiempo limitado tendrá una promoción de regalo en donde por la compra de este equipo, los usuarios se llevarán un Redmi 9 de regalo.

""")
print('\nTEXTO sin procesar')
#print(new.texto)

print('\nTEXTO procesado')
new.retirar_muletillas()
print(new.texto)

print('\nConteo de palabras')
new.contar_palabras()

print('\nBigramas')
new.detectar_bigramas()

print('\nTrigramas')
new.detectar_trigramas()
