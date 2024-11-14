import json

with open('Scripts\Lectura y escritura de archivos\persona.json','r') as iteraciones:
    datos = json.load(iteraciones)

print(datos)
datos["profecion"]="Ingeniero"

with open('archivo.json','w') as iteraciones:
    json.dump(datos, iteraciones, indent=4)