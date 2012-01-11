import pyirclib
import string
import sys
import time
import datetime

irc = pyirclib.Irclib('irc.wikimedia.org',6667)
irc.setDebug = 1
irc.login('client',username = 'karmabot')
irc.join("#en.wikipedia")
file = open("logs.html","w")
file.write("<html><body>")
#irc.privmsg("#en.wikipedia","hi future developers!")

def parsemessage(msg):
    if msg['event'] == "PRIVMSG" and str(msg['text']) == "!NAMES":
        print irc.names()
while 1:
    message = irc.getmessage()
    if message['nickname'] == "rc-pmtpa" and message['event'] == "PRIVMSG" and message['recpt'] == "#en.wikipedia":
           
        print message
        timestamp = str(datetime.datetime.now())
        file.write(timestamp+ " ")
        file.write(message['text'])
        file.write("</br>")
        
        parsemessage(message)
file.write("</body></html>")
#anyway in infinite loop. how will this be executed solve #issue1
   
   
