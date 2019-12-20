'''
Created on 19 may. 2017

@author: Román
'''

#abre archivo, escribe, guarda
archivo = open("archivo2","w")
archivo.write("linea desde programa\n")
archivo.write("otra desde programa\n")
archivo.write("tercera desde programa\n")
archivo.write("cuarta desde programa\n")
archivo.close()
#lee
archivo = open("archivo2","r")
print(archivo.read())

