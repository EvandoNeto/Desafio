import requests
import sys

user = 'pixies'
rep = 'calculadora-teste-py'

def separa_link(user,rep):
    url = 'https://github.com/' + user + '/' + rep + '/releases/latest'
    # https://github.com/pixies/calculadora-teste-py/releases/tag/v1.1
    sep_host = requests.get(url).url.split('https://')
    div = sep_host[1].split('/')
    return div

def indica_link(div):
    host = div[0]
    usuario = div[1]
    repositorio = div[2]
    versao = div[4]
    return host, usuario, repositorio, versao
