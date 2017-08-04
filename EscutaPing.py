#!/usr/bin/env python
import socket

#Escuta o Ping
class EscutaPing:

    def __init__(selfself):
        print "Classe EscutaPing"

    def escuta(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)

        while 1:
            data, addr = s.recvfrom(1508)
            print "Ping de %r" % (addr[0], )
            #print "Dados: %r" % (data)

if __name__ == '__main__':
    l = EscutaPing()
    l.escuta()
