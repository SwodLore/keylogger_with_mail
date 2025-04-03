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

```bash
pip list | grep -E "pynput|smtplib|email"
```

Si todo está bien, ya puedes ejecutar el script sin problemas. 🚀
