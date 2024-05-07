import os
import json
import funciones.globales as gf
import ui.uiProductos as uiP

def MewProducto ():

   title =  """
   ***************************
   ** REGISTRO DE PRODUCTOS **
   ***************************
   """
   gf.borrar_pantalla()
   print(title)
   ID = input("ingrese el numero de identificacion : ")
   nombreProducto= input("ingrese el nombre del producto :" )
   valorUnitario= input("ingrese valor unitario :" )
   stockmin = input("ingrese el stockmin:")
   stockmax= input("ingrese el stockmax:")
   

   Producto = {
      'identificacion': ID,
      'nmbreProducto': nombreProducto,
      'ValorUnitario' : valorUnitario,
      'stockmin' : stockmin,
      'stockmax': stockmax,
      
   }
   
   cf.AddData('data'Producto)
   gf.Tienda.get('data').update({Producto})
   if(bool(input("desdea ingresar otro producto S(si)) o Enter(no)"))):
      Producto()
   else:
    uiP.MewProducto(0)

def searchData():
   criterio = input('ingrese la codigo del producto:')
   dataProductos=gf.Tienda.get('dataProducto')
   return dataProductos


def Modifydata():
   dataProductos = searchData() 

   identificacion,nombreProducto,valorUnutario,stockmin,stockmax = dataProductos.values()
   for key in dataProductos.keys():
      if(key != 'identificacion'and key != 'producto'):
         if (bool(input('Desea modificar el {key}  S(si) o enter (no)'))):
            searchData[key] = input (f'ingrese el numero valor para {key}')
   gf.Tienda.get('dataMedico').update({identificacion:dataProductos})
   uiP.menuProductos


