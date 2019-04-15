#-*- coding-utf-8 -*-
# Autor : Wev Kleyton
# Data : 15/04/2019
# Script de Syncronismo de libs das filias jap

import os

lista_tomcat6 = ['aba','alt','bao','bcn','bgc','bnv','cap','cdc','cao','edc','igm','itu','mar','mju','pag','pap',
                 'rbc','red','rmo','sat','sda','sdn','sfx','sll','saa','sti','tal','tcm','tub','tmc','vir','xig']
lista_tomcat8 = ['lmc']
IP_SERVIDOR="172.16.40.127"


def menu_principal():
    print("################################")
    print("#  Informa a opção desejada    #")
    print("# 1 - Sincroniza Libs Filias   #")
    print("# 2 - Acessar o Shell          #")
    print("# 3 - Sair                     #")
    print("################################")
    retorno = input("prompt")



def menu_de_sincronismo():
    print("##############################")
    print("#      Escolha a opção       #")
    print("# 1 - Sincronizar lojas      #")
    print("# 2 - Atualizar Lojas        #")
    print("# 3 - Muda IP do JNLP        #")
    print("# 4 - ver IP do JNLP         #")
    print("# 0 - Sair                   #")
    print("##############################")


def sincronia():
    for l in lista_tomcat6:
        print("lojas : " + l)


def atualiza_lojas():
    loja = input("Informe a Loja a ser atualizada:")
    print(loja)

def muda_ip_jnlp():
    print(IP_SERVIDOR)

def ver_ip_jnlp():
    print(IP_SERVIDOR)


menu_principal()