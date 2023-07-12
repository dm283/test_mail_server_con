# https://aiosmtplib.readthedocs.io/en/stable/overview.html
# pip install aiosmtplib
#  см. все возможные параметры подключения  -  https://aiosmtplib.readthedocs.io/en/latest/_modules/aiosmtplib/smtp.html

import asyncio
import aiosmtplib, ssl
from aiosmtplib import SMTP
from email.message import EmailMessage
import configparser

# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST, PORT = cnf['HOST'], cnf['PORT']
RECEIVER = [cnf['RECEIVER'], ]

msg_subject = '***AioSmtplib TEST message***'
msg_text = 'Sent via aiosmtplib'

message = f"""To: {RECEIVER}
From: {MY_ADDRESS}
Subject: {msg_subject}

{msg_text}
"""
async def send_with_sendmail():
    print('CONNECTION TO SMTP SERVER...')  #
    
    # context = None  # *** var 1 *** - e.g. yandex server (actual server)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2); context.set_ciphers('DEFAULT@SECLEVEL=1')  # *** var 2 *** - e.g. gujon server (deprecated server)  -  appropriate for yandex too!

    smtp_client = SMTP(hostname=HOST, port=PORT, username=MY_ADDRESS, password=PASSWORD, 
                       use_tls=True,     # False(default)/True
                       start_tls=None,   # None(default)/False/True   mutually exclusive with use_tls
                       tls_context=context,
                       )

    await smtp_client.connect()
    print('OK  -  CONNECTED')  #
    print('SENDING A MESSAGE...')  #
    r = await smtp_client.sendmail(MY_ADDRESS, RECEIVER, message)
    print('OK  -  SEND')  #
    print(r)
    await smtp_client.quit()

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(send_with_sendmail())
