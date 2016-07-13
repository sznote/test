#!/usr/bin/python

import smtplib

email_to = 'xxxxx'
username = 'xxxxx'
password = "xxxxxx"

smtpserver = smtplib.SMTP("xxxxxx",2525)
smtpserver.set_debuglevel(2)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login( username, password )

header = 'To:' + email_to + '\n' + 'From: ' + username + '\n' + 'Subject: Python SMTP Auth\n'
msg = header + '\n\n This is a test message generated from python script \n\n'
smtpserver.sendmail(username, email_to, msg)
smtpserver.close()
print 'Email sent successfully'
