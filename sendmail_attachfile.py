#!//usr/bin/python


import smtplib
import base64
import mimetypes

from random import randint
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


filename = "5ca32d5b87.zip"
#filename = "test.txt"
#filename = "CHRY_200_2015.png"
#filename = "Volkswagen-logo-259x210.jpg"
ctype, encoding =  mimetypes.guess_type(filename)



fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)

tx=[randint(0,9) for p in range(0,6)]
ty=[randint(0,9) for p in range(0,10)]
tz=[randint(0,9) for p in range(0,13)]
x=''.join(str(k) for k in  tx)
y=''.join(str(k) for k in  ty)
z=''.join(str(k) for k in  tz)

marker = "---=_Part_%s_%s.%s" % (x,y,z)

#marker = "AUNIQUEMARKER"


fromaddr = "sahai@aim.co.th"
toaddr = "sahai@secchem.com"

body = "genarate mail  by python "



# Define the main headers.
part1 = """From: sahai srichock <sahai@aim.co.th>
To: saza <sahai@secchem.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=\"%s\"

""" % (marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)


# Define the attachment section
part3 = """Content-Type: %s; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=\"%s\"

%s
--%s--
""" %(ctype, filename, filename, encodedcontent, marker)

message = part1 + part2 + part3

server = smtplib.SMTP('smtp-server', 25)
server.set_debuglevel(1)
#server.starttls()
#server.login(fromaddr, "YOUR PASSWORD")
#text = msg.as_string()
server.sendmail(fromaddr, toaddr, message)
server.quit()
