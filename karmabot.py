import sys
import socket
import string

HOST="irc.wikimedia.org"
PORT=6667
NICK="karbot"
IDENT="karbot"
REALNAME="KarthiksBot"
CHANNEL="#en.wikipedia"
readbuffer=""

s=socket.socket()
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" %CHANNEL)
file=open("logs.txt","w")

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )
   

    for line in temp:
        decodedline = ""
        line=string.rstrip(line)
#        line=string.split(line)
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
        file.write((line)+"\r\n")
        
