import requests
import json
from PIL import Image
from io import BytesIO

#pip install Pillow
#pip install request

# Cargar la clave API desde el archivo JSON
with open('key_api_nasa.json', 'r') as file:
    data = json.load(file)
    api_key = data['api_key']

# Construir la URL con la clave API
url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

# Realizar la solicitud GET con la clave API
req = requests.get(url)
responseJson = req.json()

# Obtener la URL de la imagen desde la respuesta
image_url = responseJson['url']

# Descargar la imagen
image_response = requests.get(image_url)
image = Image.open(BytesIO(image_response.content))

# Mostrar la imagen
image.show()

