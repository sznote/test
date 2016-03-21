#!/usr/bin/python

import urllib2
import ftplib
import os

server = '110.34.250.200'
username = 'dbipmi'
userpass = 'HXsY0KnB1'
file = 'listIpmi'
url = 'http://portal.vpls.net/api/listIpmi'

response = urllib2.urlopen(url)
fh = open(file,"w")
fh.write(response.read())
fh.close()

ftp_conn = ftplib.FTP(server,username,userpass)
fh = open(file,'rb')
ftp_conn.storbinary('STOR listIpmi',fh)
fh.close()
ftp_conn.close()