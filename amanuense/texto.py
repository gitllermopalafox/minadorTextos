import os
from collections import Counter
from .buscadorweb import Buscador


class Amanuense:
    """Este objeto hace desaparecer las palabras repetidas
    y crea estadísticas sobre el texto analizado"""

    def __init__(self, fuente, tipo='string'):
        if tipo == 'txt':
            self.obtener_texto_como_string(fuente, tipo=tipo)
        elif tipo == 'string':
            self.limpiar_texto(fuente)
        elif tipo == 'web':
            self.buscar_en_la_web(fuente)
        self.muletillas = self.obtener_muletillas()

    def buscar_en_la_web(self, url):
        buscador = Buscador(url)
        self.limpiar_texto(buscador.encontrar_texto_principal())

    def obtener_texto_como_string(self, dir_archivo, tipo='txt'):
        dir_archivo = dir_archivo.split('.')[0]
        with open(dir_archivo+'.'+tipo, 'r') as f:
            texto = f.read()
        self.limpiar_texto(texto)

    def limpiar_texto(self, texto):
        caracteres_no_deseados = ['\n', '\t', '/', ':', '"', "'", ',', '“', '”','»', '«',
         '(', ')', '\u200b', '\xa0', '!', '¡', '?', '¿', ' ']
        self.texto = []
        for caracter in caracteres_no_deseados:
            self.texto = [i for i in texto.split(caracter) if i != '']
            texto = ' '.join(self.texto)

        self.texto = texto.lower()
        self.texto_crudo = self.texto

    def obtener_muletillas(self):
        ESTE_FOLDER = os.path.dirname(os.path.abspath(__file__))
        MULETILLAS_CSV = os.path.join(ESTE_FOLDER, 'muletillas.csv')
        muletillas = []
        with open(MULETILLAS_CSV) as f:
            for linea in f:
                if linea[-1:] == '\n':
                    linea = linea[:-1]
                linea = linea.split(', ')
                [muletillas.append(muletilla) for muletilla in linea if muletilla != '\n' or muletilla != '']
        return muletillas

    def retirar_muletillas(self, excepto=('.', ' '), idioma='español'):
        if idioma == 'español':
            self.remover_es(excepto)
        else:
            print(f"Sorry! No support for {idioma} yet")

    def remover_es(self, excepto):
        self.texto = self.texto.split(' ') #esto evita que se separen muletillas de mas de una palabra :'(
        nuevo_texto = self.texto.copy()
        self.muletillas_en_texto = [] #cuales muletillas se usaron
        for palabra in self.texto:
            if palabra in self.muletillas:
                if palabra not in excepto:
                    self.muletillas_en_texto.append(palabra) #solo se guardan una vez
                    nuevo_texto = [i for i in nuevo_texto if i != palabra] #borra todas las apariciones de la muletilla
        self.texto = nuevo_texto
        self.num_palabras_unicas = len(self.texto) # aqui self.texto ya es una lista NO un string

    def encontrar_palabras_mas_comunes(self, top=5):
        contador = Counter(self.conteo)
        return contador.most_common(top), top

    def contar_palabras(self):
        contador = Counter(self.texto)
        self.conteo = {}
        for palabra in self.texto:
            self.conteo.update({palabra : contador[palabra]})
        palabras_comunes, top = self.encontrar_palabras_mas_comunes()
        print(f" -> Mostrando las {top} palabras más frecuentes:")
        for par in palabras_comunes:
            print(par[0], ' : ', par[1])

    def constructo(self, j):
        concatenacion = ''
        for x in range(self.grama_actual):
            if x > 0 and x <= self.grama_actual - 1:
                concatenacion += ' '
            concatenacion += self.texto[j + x]
        return concatenacion

    def detectar_colocaciones(self, grama, frecuencia=2):
        """ Este método detecta bigramas y trigramas
            grama = 2 encuentra bigramas
            grama = 3 encuentra trigramas
        """
        xgrama = {}
        self.grama_actual = grama
        for i in range(self.num_palabras_unicas - (grama - 1) ):
            colocacion = self.constructo(i)
            #print(colocacion)
            ocurrencias = self.texto_crudo.count(colocacion)
            if ocurrencias >= frecuencia:
                xgrama.update({colocacion : ocurrencias})
        print(xgrama)
        return xgrama

    def detectar_bigramas(self):
        self.bigramas = self.detectar_colocaciones(2)

    def detectar_trigramas(self):
        self.bigramas = self.detectar_colocaciones(3)

    def clasificar_texto(self):
        """ Este método coloca el texto en una categoría dependiendo de sus etiquetas """
        pass

    def interpretar_contexto(self):
        """ Este método intenta detectar si el tema es positivo, negativo o neutro (tuple)
        Así como encontrar emociones
        """
        pass

    def determinar_temporalidad(self):
        """
        Intenta determinar si es reciente, actual o antiguo (menor a un año, menor a 5 años, mayor a 5 años)
        Requiere internet
        """
        pass

    def extraer_del_texto(self):
        """ Este método intenta extraer nombres, correos, usuarios de IG, Tiktok o Indeed.
            Así como identificar nombres de marcas o personalidades públicas o famosas
        """
        pass




#hello
