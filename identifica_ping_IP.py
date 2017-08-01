#!/usr/bin/env python
#Escuta o Ping
import socket



class EscutaPing:

    def __init__(selfself):
        print "Classe EscutaPing"

    def escuta(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
        print s

        while 1:
            data, addr = s.recvfrom(1508)
            print "Ping de %r" % (addr[0], )




l = EscutaPing()
l.escuta()
