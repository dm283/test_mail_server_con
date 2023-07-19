# https://docs.python.org/3/library/poplib.html
import poplib, configparser, ssl, sys


# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST_POP3, PORT_POP3 = cnf['HOST_POP3'], cnf['PORT_POP3']

def test_pop3_server():
    print('CONNECTION TO POP3 SERVER...')  #
    print(MY_ADDRESS, PASSWORD, HOST_POP3, PORT_POP3)

    # connect to server
    print('pop3 server connect...', end=' ')
    server = poplib.POP3_SSL(
        host=HOST_POP3, 
        port=PORT_POP3,
        context=None,
        )
    print('OK', server)

    # login
    print('send user...', end=' ')
    server_response = server.user(MY_ADDRESS)
    print('OK', server_response)

    print('send password...', end=' ')   
    server_response = server.pass_(PASSWORD)
    print('OK', server_response)

    # list items on server
    print('read from server...')
    resp, items, octets = server.list()
    print(resp, items, octets)


test_pop3_server()
