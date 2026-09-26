import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
usuario = os.getenv("GMAIL_USER")
contraseña = os.getenv("GMAIL_APP_PASSWORD")

import requests
from bs4 import BeautifulSoup

def obtener_precio(url):
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.content, "html.parser")
    elemento_precio = soup.find("p", class_="price_color")
    texto_precio = elemento_precio.get_text()
    precio = float(texto_precio.replace("£", ""))
    print(precio)
    print(type(precio))
    return precio

def enviar_alerta(nombre_libro, precio_actual, umbral):
    mensaje = EmailMessage()
    mensaje["Subject"] = f"¡Bajó de precio! {nombre_libro}"
    mensaje["From"] = usuario
    mensaje["To"] = usuario
    mensaje.set_content(
        f"El libro '{nombre_libro}' bajó a ${precio_actual} (tu umbral era ${umbral})."
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(usuario, contraseña)
        servidor.send_message(mensaje)

    print(f"Alerta enviada para {nombre_libro}")
    
def guardar_historial(nombre_libro, precio_actual, hubo_alerta):
    archivo_existe = os.path.exists("historial_precios.csv")

    with open("historial_precios.csv", mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if not archivo_existe:
            escritor.writerow(["fecha", "libro", "precio", "alerta_enviada"])

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
        escritor.writerow([fecha_actual, nombre_libro, precio_actual, hubo_alerta])    

libros_a_vigilar = [
    {
        "nombre": "A Light in the Attic",
        "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "umbral": 55.00
    },
]

for libro in libros_a_vigilar:
    precio_actual = obtener_precio(libro["url"])
    print(f"{libro['nombre']}: precio actual ${precio_actual}, umbral ${libro['umbral']}")
    
    if precio_actual <= libro["umbral"]:
        enviar_alerta(libro["nombre"], precio_actual, libro["umbral"])
        guardar_historial(libro["nombre"], precio_actual, True)
    else:
        print("Sin novedades.")
        guardar_historial(libro["nombre"], precio_actual, False)
