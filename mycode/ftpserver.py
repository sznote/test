#!/usr/bin/python

import os

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.filesystems import UnixFilesystem


class MyHandler(FTPHandler):

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        #print  "you send file :: %s" % (file)
        pass

    def on_file_received(self, file):
        #print "hello ip  recive file"
        # do something when a file has been received
        # print  "you send file :: ->%s<-" % (file)

        if file  ==  "/home/dbipmi/listIpmi":
           # print "IS done"
           os.system('/home/dbipmi/ipmi-init.sh')
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)

def main():
    authorizer = UnixAuthorizer(rejected_users=["root"], require_valid_shell=True)


#    handler = FTPHandler
    handler = MyHandler
    handler.authorizer = authorizer
    handler.abstracted_fs = UnixFilesystem
    server = FTPServer(('', 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
