import requests
from PIL import Image
from io import BytesIO
import json

def main():
    base_url = "https://epic.gsfc.nasa.gov/archive/natural"

    with open('api_nasa_key.json', 'r') as file:
        data = json.load(file)
        api_key = data['api_key']

    date = input("Ingresa la fecha en formato YYYY-MM-DD (ejemplo: 2022-01-01): ")

    try:
        year, month, day = date.split("-")

        api_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}"

        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        if not data:
            print("No hay imágenes disponibles para la fecha especificada.")
        else:
            image_data = data[0]
            image_name = image_data['image']

            image_url = f"{base_url}/{year}/{month}/{day}/png/{image_name}.png"

            image_response = requests.get(image_url)
            image_response.raise_for_status()

            img = Image.open(BytesIO(image_response.content))
            img.show()

            print(f"Imagen mostrada: {image_name}")
            print(f"Fecha: {date}")

    except ValueError:
        print("Formato de fecha inválido. Usa el formato YYYY-MM-DD.")
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")

if __name__ == ("__main__"):
    main()