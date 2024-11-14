import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura los detalles del correo

with open('contraseña.json', 'r') as file:
    data = json.load(file)
    password = data['key']

email = "correoparapruebasdecodigo@gmail.com"
destinatario = "destinatario@ejemplo.com"

# Crea el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = email
mensaje['To'] = destinatario
mensaje['Subject'] = "Asunto del correo"

# Agrega el contenido del correo
cuerpo = "Este es el contenido del correo electrónico."
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Configura el servidor SMTP
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login(email, password)

# Envía el correo
servidor.sendmail(email, destinatario, mensaje.as_string())
servidor.quit()
