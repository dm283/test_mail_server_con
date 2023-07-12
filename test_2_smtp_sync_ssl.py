# https://realpython.com/python-send-email/
import smtplib, ssl
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


# Create a secure SSL context
context = ssl.create_default_context()
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2); context.set_ciphers('DEFAULT@SECLEVEL=1')  # *** var 2 *** - e.g. gujon server (deprecated server)  -  appropriate for yandex too!


print('CONNECTION TO SMTP SERVER...')  #
with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
    server.login(MY_ADDRESS, PASSWORD)
    print('OK  -  CONNECTED')  #
    print('SENDING A MESSAGE...')  #
    server.sendmail(MY_ADDRESS, RECEIVER, message)
    print('OK  -  SENT')  #

