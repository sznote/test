#!/usr/bin/python

import sys
import string
import hashlib

import re
class convuser():
    def readfile(self, file):
        self.file = file
        self.thash = {}

        with  open(file,'r') as f:
            for lines in f:
                lines = lines.rstrip()
                matchObj = re.match('(.*),(\d+),(\d+\.\d+\.\d+\.\d+)',lines)
                if matchObj:
                    name = matchObj.group(1)
                    data = "W0nderl@nd" + lines.replace(',','')
                    #self.thash[name]= self.topasswd(data)
                    self.thash[name] =self.tomd5sum(self.topasswd(data))
                    '''
                    if name == 'xin31':
                        self.thash[name]= self.topasswd(data)
                    '''
        f.closed

    def topasswd(self, mdstr):
        return hashlib.md5(mdstr).hexdigest()[-8:]

    def tomd5sum(self, mdstr):
        return hashlib.md5(mdstr).hexdigest()

    def showthash(self):
        for x  in self.thash.keys():
            print  "%s <> %s" %( x,self.thash[x] )

    def writefile(self, file):
        f =  open(file,'w')
        f.write("<user-mapping>")
        f.write("</user-mapping>")

        f.closed

if __name__ == "__main__":
    a = convuser()
    a.readfile('./listIpmi')
    a.showthash()
    a.writefile('./user-mapping.xml')
