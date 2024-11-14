with open('binary.bin','rb') as archivo_binario:#abro el archivo y lo recorro en modo lectura
    contenido = archivo_binario.read()

print(contenido)

binary=b'01010101 11001100'+b' '+contenido+b' '

with open('binary.bin','wb') as archivo_binario:#abro el archivo y lo recorro en modo lectura
    archivo_binario.write(binary)