#!/usr/bin/python
import socket

# Open a raw socket listening on all ip addresses
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sock.bind(('', 1))

try :
   while True :
      # receive data
      data = sock.recv(1024)

      # ip header is the first 20 bytes
      ip_header = data[:20]

      # ip source address is 4 bytes and is second last field (dest addr is last)
      ips = ip_header[-8:-4]

      # convert to dotted decimal format
      source = '%i.%i.%i.%i' % (ord(ips[0]), ord(ips[1]), ord(ips[2]), ord(ips[3]))

      print 'Ping from %s' % source
except KeyboardInterrupt :
   print