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
                    self.thash[name]= self.topasswd(data)
                    #self.thash[name] =self.tomd5sum(self.topasswd(data))
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
        f.write("<user-mapping>\n")

        for  cn in  self.thash.keys():
            f.write("\t<authorize username=\"%s\" password=\"%s\">\n" % (cn,self.thash[cn]))
            #f.write("\t<authorize username=\"%s\" password=\"%s\" " %( cn, self.thash[cn]))
            #f.write("encoding=\"md5\">\n")
            f.write("\t\t<connection name=\"%s\">\n" %(cn))
            f.write("\t\t\t<protocol>rdp</protocol>\n")
            f.write("\t\t\t<param name=\"hostname\">110.34.250.200</param>\n")
            f.write("\t\t\t<param name=\"username\">%s</param>\n" %(cn))
            f.write("\t\t\t<param name=\"password\">%s</param>\n" %(self.thash[cn]))
            f.write("\t\t\t<param name=\"color-depth\">16</param>\n")
            f.write("\t\t</connection>\n")
            f.write("\t</authorize>\n")

        f.write("</user-mapping>\n")
        f.closed


if __name__ == "__main__":
    a = convuser()
    a.readfile('./listIpmi')
    #a.showthash()
    a.writefile('./user-mapping.xml')
