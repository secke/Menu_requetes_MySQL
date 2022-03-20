#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:51:02 2022

@author: secke
"""
#import pymysql

#connexion=pymysql.connect(host='localhost',user='root', password='secke2022', database='db_lem')
#bic=connexion.cursor()

from fonction_requete import *
copie_dict=liste.copy()
reexecuter_dict=liste.copy()
executer=[]
while True :
    for i,j in copie_dict.items():
        print(j)
    x=input("entrez votre choix: ")
    if x.isdigit():
        t=int(x)
        recup=liste.get(t)
        executer.append(recup)
        copie_dict.pop(t)
    if x=='1':
        requet1()
    elif x=='2':
        requet2()
    elif x=='3':
        requet3()
    elif x=='4':
        requet4()
    elif x=='5':
        requet5()
    elif x=='6':
        requet6()
    elif x=='7':
        requet7()
    elif x=='8':
        requet8()
    elif x=='9':
        requet9()
    elif x=='10':
        requet10()
    elif x=='11':
        print("OK")
    elif x=='12':
        requet12()
    elif x=='13':
        print("OK")
    elif x=='14':
        requet14()
    elif x=='15':
        print("OK")
    elif x=='16':
        print("OK")
    elif x=='17':
        print("OK")
    elif x=='18':
        print("OK")
    elif x=='E' or x=='e':
        print(executer)
    elif x=='R' or x=='r':
        copie_dict=reexecuter_dict

    elif x=='q' or x=='Q':
        break
