#-*- coding-utf-8 -*-
# Autor : Wev Kleyton
# Data : 15/04/2019
# Script de Syncronismo de libs das filias jap

import os
import time

from _json import make_encoder

lista_tomcat6 = ['aba','alt','bao','bcn','bgc','bnv','cap','cdc','cao','edc','igm','itu','mar','mju','pag','pap',
                 'rbc','red','rmo','sat','sda','sdn','sfx','sll','saa','sti','tal','tcm','tub','tmc','vir','xig']
lista_tomcat8 = ['lmc']
IP_SERVIDOR="172.16.40.127"



def menu_de_sincronismo():
    print("\033[96m ##############################")
    print("\033[96m #      Escolha a opção       #")
    print("\033[96m # 1 - Sincronizar lojas      #")
    print("\033[96m # 2 - Atualizar Lojas        #")
    print("\033[96m # 3 - Muda IP do JNLP        #")
    print("\033[96m # 4 - ver IP do JNLP         #")
    print("\033[96m # 0 - Sair                   #")
    print("\033[96m ##############################")

    retorno = input("Informe a opção : ")

    if retorno == "1":
        print("\33[95m Realizando Sincronismos de TODAS as Filiais")
        time.sleep(2)
        sincronia()
    elif retorno == "2":
        loja = input("\33[95m Informe a Lojas a ser Atualizada ? ")
        atualiza_lojas(loja)
    elif retorno == "3":
        print("\33[95m Mudando Ip de dentro do JNLP")
    elif retorno == "4":
        print("\33[95m Mostra Ips!")
    elif retorno == "0":
        print("\33[930m Saindo!")
    else:
        print("\33[91m Opção Desconhecida")
        os.system('clear')
        menu_de_sincronismo()


def sincronia():
    for l in lista_tomcat6:
        print("lojas : " + l)


def atualiza_lojas(loja):
    print(loja)

def muda_ip_jnlp():
    print(IP_SERVIDOR)

def ver_ip_jnlp():
    print(IP_SERVIDOR)

"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' """

menu_de_sincronismo()