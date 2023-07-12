# https://realpython.com/python-send-email/
import smtplib, ssl
import configparser

# загрузка конфигурации
CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE, encoding='utf-8')
cnf = config['DEFAULT']

MY_ADDRESS, PASSWORD = cnf['MY_ADDRESS'], cnf['PASSWORD']
HOST, PORT = cnf['HOST'], 587  # For starttls
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

# Try to log in to server and send email
try:
    print('CONNECTION TO SMTP SERVER...')  #
    server = smtplib.SMTP(HOST, PORT)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(MY_ADDRESS, PASSWORD)
    print('OK  -  CONNECTED')  #
    print('SENDING A MESSAGE...')  #
    server.sendmail(MY_ADDRESS, RECEIVER, message)
    print('OK  -  SENT')  #
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

