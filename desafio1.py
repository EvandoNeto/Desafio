""" Etapa 1 """

link = "https://github.com/pixies/devinf/releases/tag/db-base-v1.1"

def repartir(link):
    lista_link = [link.splint('/')]
    return lista_link


def retonar(lista_link):
    qntd = len(lista_link)
    versao = lista_link[qntd]
    user = lista_link[3,4]
    return versao,user

""" Etapa 2 """