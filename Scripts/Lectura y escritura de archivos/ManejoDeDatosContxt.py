with open('Scripts\Lectura y escritura de archivos\Archivo.txt','r', encoding='utf-8') as archivo:#abro el archivo y lo recorro en modo lectura
    contenido = archivo.readlines() #leo el archivo

print(contenido)

contenido[2]="mister bombastic, mister fantastic \n"

with open('Archivo.txt','w', encoding='utf-8') as archivo:
    archivo.writelines(contenido)

with open('Archivo.txt','a', encoding='utf-8') as archivo:
    archivo.write("\nhola a todos, ola de frio")

with open('laeradehielo.txt','x', encoding='utf-8') as archivo:
    archivo.write("que extinguio a los dinosaurios?, la edad de hielo")