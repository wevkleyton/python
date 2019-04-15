# -*- coding:utf-8 -*-
# Script de syncronismo de libas dos ambientes de Teste/Homologação e Produção.
# Autor: Wev Kleyton
# Data: 12/04/2019

import os
path_tomcat8="/var/lib/tomcat8/webapps/cliente_*"
path_local="/var/lib/tomcat8/webapps/"
ips = ['172.17.7.151','172.17.7.152','172.17.7.153','172.17.7.154']

print("Verificando libs!")

for ip in ips:
    resultado = os.system('ping -c5 ' + ip +  ">/dev/null")
    if resultado != 0:
        print("Problema de Comunicação Com o Servidor " + ip )
    else:
        os.system('rsync -Cravzp wev@' +ip +'://' + path_tomcat8 + " " + path_local)
        if ip == "172.17.7.151":
            print("Filial de BCN Sincronizada")
        elif ip == "172.17.7.152":
            print("Filial de LMC Sincronizada")
        elif ip == "172.17.7.153":
            print("Filial de MJU Sincronizada")
        else:
            print("Filial de ABA Sincronizada")