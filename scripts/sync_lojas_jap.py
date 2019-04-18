#-*- coding-utf-8 -*-
# Autor : Wev Kleyton
# Data : 15/04/2019
# Script de Syncronismo de libs das filias jap

import os
import time

#from _json import make_encoder
#Constantes
IP_SERVIDOR="172.16.40.127"
PATH_DIR='/home/cliente_jap'


lista_tomcat6 = ['aba','alt','bao','bcn','bgc','bnv','cap','cdc','cao','edc','igm','itu','mar','mju','pag','pap',
                 'rbc','red','rmo','sat','sda','sdn','sfx','sll','saa','sti','tal','tcm','tub','tmc','vir','xig']
lista_tomcat8 = ['lmc']





def menu_de_sincronismo_principal():
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
        menu_de_sincronismo_principal()


def sincronia():
    for loja in lista_tomcat6:
        resultado = os.system('ping -c5  sco'+ loja + ">/dev/null")
        if resultado != 1:
            print("Fazendo Sincronismo da filial de " + loja.upper())
            os.system('rsync -Cravzp socic@sco' + loja + ':/var/lib/tomcat6/webapps/cliente_' + loja + PATH_DIR +'/chegando/cliente_' + loja)
            os.system('cp -r '  + PATH_DIR + '/chegando/cliente_' + loja + ' ' + PATH_DIR + 'cliente_' + loja)
            print('Sincronismo Finalizado ...!')


    for t8 in lista_tomcat8:
        print("Lojas com Tomcat8:" + t8)


def atualiza_lojas(loja):
    print(loja)

def muda_ip_jnlp():
    print(IP_SERVIDOR)

def ver_ip_jnlp():
    print(IP_SERVIDOR)

def testa_comunucacao():
    print("teste")


menu_de_sincronismo_principal()