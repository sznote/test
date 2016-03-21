#!/usr/bin/python

import ftplib
import os

server = '110.34.250.200'
username = 'dbipmi'
userpass = 'HXsY0KnB1'
file = 'listIpmi'
ftp_conn =  ftplib.FTP(server,username,userpass)
fh = open(file,'rb')
ftp_conn.storbinary('STOR listIpmi',fh)
fh.close()
ftp_conn.close()

