#!/usr/bin/python
import os
import re
import os.path
#import subprocess
from subprocess import  CalledProcessError,check_output

#z = re.compile('zone\s*\"(?P<zone>.*)\"\s*{')

pattern = 'zone\s*\"(?P<zone>.*)\"\s*{'
filepat = '\s+file\s*\"(?P<nfile>.*)\"\s*;'
chroot = '/home/saza/testdns/chroot'
count = 0 
zone = ''
nfile = ''

file = open("named.conf","r")


for line in file:
  #print (line)
  #if m = re.search( pattern, line):
  #print ( count )
  m = re.search( pattern, line)

  if m:
     count = 1 
     zone =  str( m.group('zone') )
     #print ("debug %s" % zone )
  else:
     f = re.search (filepat,line)
     if f:
        count = count + 1
        nfile = f.group('nfile') 
        #print (count)

     if count == 2:
        count = 0
        
        nfile  =  chroot  +  nfile
        #print  ( zone )
        #print  ( nfile )
    
        if  not os.path.isfile( nfile ):
            print ("Not Found %s" % nfile )
            continue
        else:
	    try:
               output  = check_output(["named-checkzone", zone, nfile])
               returncode = 0
            except CalledProcessError as e:
	       output = e.output
               returncode = e.returncode
               print ("File Error %s" % nfile )
        #print output
        #print returncode 
        #elif os.system("named-checkzone %s %s &> /tmp/hello" %( zone, nfile)):
	#      print ("Error:: %s" %nfile)

file.close()
