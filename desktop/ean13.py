# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:53:14 2019

@author: gmmonsalve
"""
import barcode
import webbrowser
from PIL import Image

valor = input('Digite el código a generar: ')

def crear_ean13(valor, archivo):
    ean = barcode.get('ean13', valor, writer=barcode.writer.ImageWriter())
 
    # mostramos el codigo de barras en consola
    print('El código completo es: '+str(ean))
    print(ean.to_ascii())
    
 
    # generamos el archivo
    filename = ean.save(archivo)
    return str(ean)

cod = crear_ean13(valor, "ean13")

url = 'https://barcodesdatabase.org/es/barcode/'+str(cod)

webbrowser.open(url)


#...

img = Image.open('./ean13.png')
img.show()

