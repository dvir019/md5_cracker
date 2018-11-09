from threading import Thread
import socket


class Network(object):
    def __init__(self, ip, port):
        self.sock = socket.socket()
        while True:
            try:
                self.sock.connect((ip, port))
                break
            except:
                pass

    def send(self, msg):
        try:
            self.sock.send(msg)
            print 'send ' +msg
        except:
            print 'error send ' + msg

    def receive(self):
        recv = ''
        print 'going to rec'
        try:
            recv = self.sock.recv(1024)
            print 'rece ' + recv
        except:
            print 'error receive'
        return recv

    def close(self):
        self.sock.close()
