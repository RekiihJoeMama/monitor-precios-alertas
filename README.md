# 📚 Monitor de Precios y Alertas

Script en Python que rastrea el precio de un libro en [books.toscrape.com](https://books.toscrape.com/) y envía una alerta por correo cuando el precio baja de un umbral definido.

## 🎯 ¿Qué hace?

- Consulta el precio actual del libro configurado
- Lo compara contra un umbral (precio máximo aceptable)
- Si el precio bajó del umbral, envía un correo de alerta automáticamente
- Registra cada consulta (fecha, libro, precio, si se envió alerta) en `historial_precios.csv`
- Corre de forma automática todos los días a las 9:00 AM mediante el Programador de tareas de Windows

## 📦 Requisitos

- Python 3.14+
- Librerías: `requests`, `beautifulsoup4`, `python-dotenv` (ajustar según lo que uses realmente en `monitor.py`)

Instalación:
```bash
pip install requests beautifulsoup4 python-dotenv
```

## ⚙️ Configuración

Crear un archivo `.env` en la raíz del proyecto (no se sube al repo, ya está en `.gitignore`) con:

GMAIL_USER=tu_correo@gmail.com
GMAIL_APP_PASSWORD=tu_contraseña_de_aplicación


> Nota: `GMAIL_APP_PASSWORD` es una [contraseña de aplicación](https://support.google.com/accounts/answer/185833) de Gmail, no tu contraseña normal.

## ▶️ Uso

### Manual
```bash
python monitor.py
```

### Automático (Windows)
El proyecto está configurado para correr todos los días a las 9:00 AM usando el **Programador de tareas de Windows**, sin intervención manual.

## 📊 Historial de precios

Cada ejecución agrega una fila a `historial_precios.csv` con: fecha, libro, precio y si se envió alerta.

## 📖 Libro monitoreado actualmente

- *A Light in the Attic* — [books.toscrape.com](https://books.toscrape.com/)

## 🚀 Próximas mejoras

- Soporte para monitorear varios libros a la vez
- Dashboard visual con historial de precios