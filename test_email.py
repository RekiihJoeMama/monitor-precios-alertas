import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv("GMAIL_USER")
contraseña = os.getenv("GMAIL_APP_PASSWORD")

mensaje = EmailMessage()
mensaje["Subject"] = "Prueba de monitor-precios-alertas"
mensaje["From"] = usuario
mensaje["To"] = usuario
mensaje.set_content("Si estas leyendo esto, el envio de emails funciona correctamente.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(usuario, contraseña)
    servidor.send_message(mensaje)
    
    print("Email enviado con exito xd")