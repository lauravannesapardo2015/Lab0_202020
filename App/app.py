"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";")->list:
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep

    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\n**************************************************************************************")
    print("\n Bienvenidos a la consola del Reto 1 Explorando la           ***    MAGIA DEL CINE ***")
    print("\n**************************************************************************************")
    print("1- Cargar Datos de Archivos Large ")
    print("2- Cargar Datos de Archivos Small ")
    print("3- Consultar numero de peliculas buenas (vote_average>=6)")
    print("4- Cacular el promedio de la votacion")
    print("5- Consultar buenas peliculas por director")
    print("0- Salir")
    
def peliculasBuenas(lst1: list)-> int:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
   
    return pelBuenas

def PromedioPeliculasBuenas(lst1: list)-> float:
    #print(lst1)
    print("Aqui estoy ")
    nRegistros= len(lst1)
    pelBuenas=0
    proBuenas=0.0
    for i in range (0, nRegistros, 1):
        if (float(lst1[i]['vote_average']) >= 6):
            pelBuenas+=1
            proBuenas= proBuenas + float(lst1[i]['vote_average'])
        #print(lst1[i]['vote_average'])
        #pelBuenas=pelBuenas+ float(lst1[i]['vote_average'])
    #print(pelBuenas)    
    #input("Click para continuar")
    proBuenas=proBuenas/pelBuenas
    return proBuenas

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1 = [] #instanciar una lista vacia para "Movies Details"
    lista2 = [] #instanciar una lista vacia para "Casting"
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar:  ') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista1=loadCSVFile("Data/MoviesDetailsCleaned-large.csv", lista1) 
                print("Datos cargados de Movies Large, "+str(len(lista1))+" elementos cargados")
                lista2=loadCSVFile("Data/MoviesCastingRaw-large.csv", lista2) 
                print("Datos cargados de Casting Large, "+str(len(lista2))+" elementos cargados")
                input ("Clic para cotinuar...")

            elif int(inputs[0])==2: #opcion 2
                lista1=loadCSVFile("Data/MoviesDetailsCleaned-small.csv", lista1) 
                print("Datos cargados de Movies Small, "+str(len(lista1))+" elementos cargados")
                lista2=loadCSVFile("Data/MoviesCastingRaw-small.csv", lista2) 
                print("Datos cargados de Casting Small, "+str(len(lista2))+" elementos cargados")
                input ("Clic para cotinuar")

            elif int(inputs[0])==3: #opcion 3
                peliculas_buenas= peliculasBuenas(lista1)
                print("El numero de peliculas revisadas fueron: " , len(lista1) , " de las cuales " , peliculas_buenas , "obtuvieron calificacion >= a 6") 
                input ("Clic para cotinuar")

            elif int(inputs[0])==4: #opcion 4
                proPeliculas_buenas= PromedioPeliculasBuenas(lista1)
                print("El  promedio de las peliculas buenas fue de:  " , proPeliculas_buenas ) 
                input ("Clic para cotinuar")
            elif int(inputs[0])==5: #opcion 5
                print("Funcion en construccion") 
                input ("Clic para cotinuar")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
