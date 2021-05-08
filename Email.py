# mail response

import socket
import smtplib
import dns
import re

addressToVerify = 'prasad.keluskar@gmail.com'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
	print('Bad request')
	raise ValueError('Bad Syntax')

records = dns.resolver.query('prasad.keluskar@gmail.com', 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)
# get local server status

host = socket.gethostbyname()
host = socket.gethostbyaddr()

#smtp lib setup ( )

server = smtplib.SMTP()
server.set_debuglevel(0)

#SMTP conversation

server.connect(mxRecord)
server.helo()
server.mail('prasad.keluskar@gmail.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

#status

if code == 200:
    print("success")
else:
    print("bad request")
