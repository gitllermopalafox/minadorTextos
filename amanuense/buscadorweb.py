from bs4 import BeautifulSoup
import requests


class Buscador:
    """Objeto Buscador web"""

    def __init__(self, url):
        self.url = url
        try:
            respuesta = requests.get(self.url)
            if not respuesta.ok:
                print("El sitio no respondió")
                self.__del__()
            else:
                self.texto_html = respuesta.text
        except:
            print('No se pudo conectar')
            self.texto_html = ''
            self.__del__()

    def __del__(self):
        print('Objeto eliminado')

    def encontrar_titulo(self, etiqueta='h1'):
        return self.soup.find(etiqueta).text

    def encontrar_texto_principal(self, etiqueta='p', parser='lxml'):
        self.soup = BeautifulSoup(self.texto_html, parser)
        self.titulo = self.encontrar_titulo()
        tags = self.soup.find_all(etiqueta)
        lista_tags = [self.titulo]
        for tag in tags:
            lista_tags.append(tag.text)
        return ''.join(lista_tags)
