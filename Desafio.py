import requests
import sys

usuario = 'pixies'
repositorio = 'calculadora-teste-py'

def versao_repositorio_link(usuario, repositorio):
    url = 'https://github.com/' + usuario + '/' + repositorio + '/releases/latest'
    req = requests.get(url).url.split('https://')[1]
    # https://github.com/pixies/calculadora-teste-py/releases/tag/v1.1
    host, usuario, repositorio, releases, tag, versao, = req.split('/')
    return {'usuario': usuario, 'repositorio': repositorio, 'versao': versao }

print(versao_repositorio_link(usuario,repositorio))
