#!/usr/bin/env python
# Minimal Wake-On-LAN Python implementation.
# (C) 2008 Taher Shihadeh <taher@unixwars.com>
# This is free software licensed under GPL v2

import struct
import socket
import sys

DEFAULT_MAC='00:90:dc:06:fc:cd'

def broadcast(magic):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  s.sendto(magic, ('<broadcast>', 9))
  
def build_packet(mac_str):
  bytes = [255]*6 + [int(x,16) for x in mac_str.split(':')]*16
  magic = struct.pack('B'*102, *bytes)
  return magic

if __name__ == "__main__":
  if len(sys.argv)==1:
    broadcast (build_packet (DEFAULT_MAC))
  elif len(sys.argv[1].split(':'))==6:
    broadcast (build_packet (sys.argv[1]))
  else:
    print('Usage: wol AA:BB:CC:DD:EE:FF') 
