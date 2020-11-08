from pyautogui import *
import pyautogui
from time import sleep
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def send_email(receiver_email):
    if len(receiver_email) == 0:
        return

    # CONSTANTS THAT YOU SHOULD FILL IN
    SENDER_EMAIL = "manoel0gustavo@gmail.com" # Use your own email
    PASSWORD = "The SENDER_EMAIL password" 
    MESSAGE = "Sua fila no league of legends foi aceita!"

    # create message object instance
    msg = MIMEMultipart()
         
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = "LOL - Partida Encontrada"
     
    # add in the message body
    msg.attach(MIMEText(MESSAGE, 'plain'))
 
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print('Não foi possível enviar email de notificaçao para "' + receiver_email + '"')

def check_screen():
    button_pos = pyautogui.locateOnScreen('fila.png', confidence=0.7)
            
    if button_pos != None:
        #print(f'Found {button_pos}')
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main():
    receiver_email = input('Seu email (opcional): ').strip()
    queue_counter = 0

    print('Estou de olho na fila...', end="\n\n")
    
    while True:
        if check_screen():
            queue_counter += 1
            print(f'Filas aceitas: {queue_counter}')
            
            send_email(receiver_email)         
            sleep(6)
            #break


main()            
