# https://realpython.com/python-send-email/
import smtplib, ssl, sys
import configparser

# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST, PORT = cnf['HOST'], cnf['PORT']
RECEIVER = [cnf['RECEIVER'], ]

msg_subject = '***Smtplib TEST message***'
msg_text = 'Sent via smtplib'

message = f"""To: {RECEIVER}
From: {MY_ADDRESS}
Subject: {msg_subject}

{msg_text}
"""

# THIS WORK FOR YA AND GU !!!

# Create a secure SSL context
# context = ssl.create_default_context()    # ok for Ya, not for Gu
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)   # ok for Ya & Gu
context.set_ciphers('DEFAULT@SECLEVEL=1')        # ok for Ya & Gu

print('CONNECTION TO SMTP SERVER...')  #
with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
    server.login(MY_ADDRESS, PASSWORD)
    print('OK  -  CONNECTED')  #

    # print('SENDING A MESSAGE...')  #
    # server.sendmail(MY_ADDRESS, RECEIVER, message)
    # print('OK  -  SENT')  #

