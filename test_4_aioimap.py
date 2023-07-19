# https://pypi.org/project/aioimaplib/
# https://github.com/bamthomas/aioimaplib
# pip install aioimaplib
import asyncio, configparser, ssl, sys
from aioimaplib import aioimaplib

# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST_IMAP, PORT_IMAP = cnf['HOST_IMAP'], cnf['PORT_IMAP']

async def test_imap_server():
    print('CONNECTION TO IMAP SERVER...')  #
    print(MY_ADDRESS, PASSWORD, HOST_IMAP, PORT_IMAP)
    context = ssl.SSLContext()  # для сервера СВХ, для Yandex не нужно
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # для сервера СВХ, для Yandex не нужно
    # context.set_ciphers('DEFAULT@SECLEVEL=1')       # для сервера СВХ, для Yandex не нужно
    imap_client = aioimaplib.IMAP4_SSL(
        host=HOST_IMAP, 
        port=PORT_IMAP, 
        ssl_context=context                         # для сервера СВХ, для Yandex не нужно
        )  # не ловиться исключение здесь!
    
    print(type(imap_client))  # class 'aioimaplib.aioimaplib.IMAP4_SSL'

    print('wait_hello_from_server...', end=' ')
    await imap_client.wait_hello_from_server()
    print('OK')

    print('login...', end=' ')
    await imap_client.login(MY_ADDRESS, PASSWORD)
    print('OK')

    print('select...', end=' ')
    await imap_client.select('INBOX')
    print('OK')
    
    await imap_client.close()
    await imap_client.logout()
    

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(test_imap_server())

# async def send_with_sendmail():
#     print('CONNECTION TO SMTP SERVER...')  #
    
#     # SET SSL CONTEXT (IF NECESSARY)  
#     # https://docs.python.org/3/library/ssl.html
#     # https://docs.python.org/3/library/ssl.html#ssl.SSLContext
#     # context = None  # ok with Yandex server
#     # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # set tls protocol version (not needed actually for Ya or Gu)
#     # context = ssl.SSLContext()            # NOT load ca certs from system (ok with Ya and Gu)
#     context = ssl.create_default_context()  #  load all ca certs from system (ok with Ya, not Gu)
#     context.set_ciphers('DEFAULT@SECLEVEL=1')  # ok with Ya and Gu   -   default seclevel=2

#     # print SSL parameters
#     print('cert_store_stats = ', context.cert_store_stats())  # it's different between SSLContext & create_default_context !!!
#     print('get_ca_certs = ', context.get_ca_certs())          # it's different between SSLContext & create_default_context !!!
#     print('get_ciphers = ', context.get_ciphers())
#     print('options = ', context.options)
#     print('security_level = ', context.security_level)

#     smtp_client = SMTP(hostname=HOST, port=PORT, username=MY_ADDRESS, password=PASSWORD, 
#                        use_tls=True,     # False(default)/True
#                        start_tls=None,   # None(default)/False/True   mutually exclusive with use_tls
#                        tls_context=context,
#                        )

#     await smtp_client.connect()
#     print('OK  -  CONNECTED')  #
    
#     # print('SENDING A MESSAGE...')  #
#     # r = await smtp_client.sendmail(MY_ADDRESS, RECEIVER, message)
#     # print('OK  -  SEND')  #
#     # print(r)

#     await smtp_client.quit()


