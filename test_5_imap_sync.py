# https://docs.python.org/3/library/imaplib.html
import imaplib, configparser, ssl, sys

# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST_IMAP, PORT_IMAP = cnf['HOST_IMAP'], cnf['PORT_IMAP']


def test_imap_server():
    print('CONNECTION TO IMAP SERVER...')  #
    print(MY_ADDRESS, PASSWORD, HOST_IMAP, PORT_IMAP)

    context = ssl.SSLContext()
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # для сервера СВХ, для Yandex не нужно
    # context.set_ciphers('DEFAULT@SECLEVEL=1')       # для сервера СВХ, для Yandex не нужно
    imap = imaplib.IMAP4_SSL(
        host=HOST_IMAP, 
        port=PORT_IMAP,
        ssl_context=context
        )
    
    print(type(imap))  # class 'imaplib.IMAP4_SSL'

    print('starttls...', end=' ')
    imap.starttls()
    print('OK')

    
    print('login...', end=' ')
    imap.login(MY_ADDRESS, PASSWORD)
    print('OK')

    print('select...', end=' ')
    status, messages = imap.select("INBOX")
    print('OK', status)

    imap.close()
    imap.logout()


test_imap_server()
