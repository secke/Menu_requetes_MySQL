#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:53:57 2022

@author: secke
"""
import pymysql
connexion=pymysql.connect(host='localhost',user='root', password='secke2022', database='db_lem')
bic=connexion.cursor()

def requet1():
    bic.execute("select adresse_AGENCE from AGENCE")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])


def requet2():
    bic.execute("select nom_USER from USERS where id_PROFIL_PROFIL=3 order by nom_USER")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])

def requet3():
    bic.execute("select nom_USER, adresse_AGENCE from USERS,AGENCE where id_PROFIL_PROFIL=1 and numero_AGENCE=numero_AGENCE_AGENCE;")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0],'         ',i[1])

def requet4():
    bic.execute("select * from AGENCE,COMPTE_TRANSACTION where numero=numero_AGENCE and adresse_AGENCE='37 Dunning Road'")
    affiche=bic.fetchall()
    for i in affiche:
        print(i)

def requet5():
    bic.execute("select montant_TRANSACTION from TRANSACTIONS,USERS,AGENCE where numero_AGENCE=USERS.numero_AGENCE_AGENCE and id_TYPE_TYPE=1 and id_PROFIL_PROFIL=3 and nom_USER='Goby' order by montant_TRANSACTION")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])
        
def requet6():
    bic.execute("select nom_USER from USERS,AGENCE where id_USER=id_USER_USER and adresse_AGENCE='37 Dunning Road'")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])
        
def requet7():
    bic.execute("select numero_AGENCE,adresse_AGENCE,count(*) as nombre from USERS,AGENCE where numero_AGENCE=numero_AGENCE_AGENCE group by numero_AGENCE")
    affiche=bic.fetchall()
    for i in affiche:
        print(i)
        #print(i[0],"  ",i[1],"        ",i[2])       
        
def requet8():
    bic.execute("select numero from USERS,COMPTE_TRANSACTION,ASSOCIER where id_USER=id_USER_USER and numero=numero_COMPTE_TRANSACTION and nom_USER='Slott' and year(date_fin)=2019 and month(date_fin)=05")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])
        #print(i[0],"  ",i[1],"        ",i[2])            
        
def requet9():
    bic.execute("select nom_USER from USERS,ASSOCIER,COMPTE_TRANSACTION where id_USER=id_USER_USER and numero=numero_COMPTE_TRANSACTION  and year(date_fin)=2022 and numero_COMPTE_TRANSACTION=1")
    affiche=bic.fetchall()
    for i in affiche:
        print(i[0])
        #print(i[0],"  ",i[1],"        ",i[2])           
        
def requet10():
    bic.execute("select montant_TRANSACTION,date_TRANSACTION,nom_USER from TRANSACTIONS,USERS,AGENCE where numero_AGENCE=TRANSACTIONS.numero_AGENCE_AGENCE and id_USER=TRANSACTIONS.id_USER_USER and numero_AGENCE=1")
    affiche=bic.fetchall()
    for i in affiche:
        print(i)
        #print(i[0],"  ",i[1],"        ",i[2])      
        
def requet12():
    bic.execute("select libelle_PROFIL,nom_USER,adresse_AGENCE,TYPE,montant_TRANSACTION from TRANSACTIONS,PROFIL,USERS, TYPE,AGENCE where id_PROFIL=1 and id_PROFIL=USERS.id_PROFIL_PROFIL and id_TYPE=id_TYPE_TYPE and USERS.id_USER=TRANSACTIONS.id_USER_USER and AGENCE.numero_AGENCE=TRANSACTIONS.numero_AGENCE_AGENCE and nom_USER='Hargreaves' order by montant_TRANSACTION")
    affiche=bic.fetchall()
    for i in affiche:
        print(i)
        #print(i[0],"  ",i[1],"        ",i[2])       
        
def requet14():
    bic.execute("select date_TRANSACTION,sum((valeur*montant_TRANSACTION)) as somme from TRANSACTIONS,AGENCE,PART,POSSEDR where numero_AGENCE=numero_AGENCE_AGENCE and numero_AGENCE=1 and id_PART=1 and id_PART_PART group by date_TRANSACTION")
    affiche=bic.fetchall()
    for i in affiche:
        print(i)
        #print(i[0],"  ",i[1],"        ",i[2])         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
liste={1:"1: liste de tous les agents",2:"2: liste de tous les caissiers par ordre croissant de leur nom",
       3:"3: liste de tous les chef d'agence ainsi que le nom d'agence",4:"4: liste des comptes de transaction de l'agence dont l'adresse est 37 Dunning Road par ordre croissant du solde",
       5:"5: liste la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est Goby par ordre croissant du montant",
       6:"6: liste les utilisateurs de l’agence de l'adreese 37 Dunning Road",7:"7: liste du nombre de compte par agence",
       8:"8: liste comptes affectés à l’utilisateur 'Slott' durant le mois de Mai 2019",
       9:"9: liste utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
       10:"10: liste montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 1",
       11:"11: nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
       12:"12: les dépôts effectués et les retraits par jour dans l’agence dont le chef est 'Hargreaves' par ordre croissant du montant",
       13:"13 les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop",
       14:"14 la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
       15:"15 la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
       16:"16 l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
       17:"17 l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
       18:"18 l’agence qui a fait le retrait le plus grand durant le mois de MAI 21",
       19:"19 les agences qui n’ont pas fait de dépôt le 10-08-2021",
       20:"20 les noms utilisés par l’agence numéro 001 durant le mois de MAI 21",
       21:"21 Liste du ou des clients qui ont effectué le dépôt le plus petit durant le mois de MAI 21",
       22:"22 Liste du ou des clients qui ont effectué le plus de dépôt durant le mois de MAI 21",
       23:"23 Liste des 5 agences qui ont effectué le plus de transactions durant l’année 2021",
       24:"24 Liste des 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021",
       25:"25 Liste de l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop",
       26:"E ou e: Pour afficher les requêtes déjà choisi pour les ré exécuter",
       27:"R ou r: Pour réafficher tout le menu (exécuter ou non)",28:"Q ou q: Pour quitter"}
#x=int(input("entrez votre choix: "))
#recup=liste.get(x)
#print(recup)






#for i,j in liste.items():
#    print(j)