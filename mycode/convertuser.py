#!/usr/bin/python

import sys
import string
import hashlib
import getopt
import os
import re

class convuser():

    ipmiweb = "110.34.250.100"

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
                    #self.thash[name] =self.tomd5sum(self.topasswd(data))
                    self.thash[name]= self.tomd5sum(data)
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
            print  "%s <> %s" %( x,self.thash[x])
            print  "xrd pass is: %s" %(self.thash[x][0:12])
            print  "web pass is: %s" %(self.thash[x][-8:])

    def writefile(self, file):
        f =  open(file,'w')
        f.write("<user-mapping>\n")

        for  cn in  self.thash.keys():
            #f.write("\t<authorize username=\"%s\" password=\"%s\">\n" % (cn,self.thash[cn]))

            f.write("\t<authorize username=\"%s\" password=\"%s\" " %( cn, self.tomd5sum(self.thash[cn][-8:])))
            f.write("encoding=\"md5\">\n")
            f.write("\t\t<connection name=\"%s\">\n" %(cn))
            f.write("\t\t\t<protocol>rdp</protocol>\n")
            f.write("\t\t\t<param name=\"hostname\">%s</param>\n" %(self.ipmiweb))
            f.write("\t\t\t<param name=\"username\">%s</param>\n" %(cn))
            #f.write("\t\t\t<param name=\"password\">%s</param>\n" %(self.thash[cn][-8:]))
            f.write("\t\t\t<param name=\"password\">%s</param>\n" %(self.thash[cn][0:12]))
            f.write("\t\t\t<param name=\"color-depth\">16</param>\n")
            f.write("\t\t</connection>\n")
            f.write("\t</authorize>\n")

        f.write("</user-mapping>\n")
        f.closed

def main(argv):
    infile  = ''
    outfile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'convertuser.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'convertuser.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg

    if not os.path.isfile(infile):
        print 'convertuser.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    a = convuser()
    a.readfile(infile)
    #a.showthash()
    a.writefile(outfile)

    #a.readfile('./listIpmi')
    #a.showthash()
    #a.writefile('./user-mapping.xml')


if __name__ == "__main__":
     main(sys.argv[1:])
