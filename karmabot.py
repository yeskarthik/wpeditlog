import pyirclib
import re
import string
import sys
import time
import datetime

irc = pyirclib.Irclib('irc.wikimedia.org',6667)
irc.setDebug = 1
irc.login('client',username = 'karmabot')
irc.join("#en.wikipedia")
file = open("logs.html","w")
file.write('<html><body>')

regex = re.compile("\x0D|\x1f|\x02|\x12|\x0f|\x16|\x03(?:\d{1,2}(?:,\d{1,2})?)?", re.UNICODE)

def parsemessage(msg):
    if msg['event'] == "PRIVMSG" and msg['text'] == "!NAMES":
        print irc.names()

while True:
    message = irc.getmessage()
    if message['nickname'] == "rc-pmtpa" and message['event'] == "PRIVMSG" and message['recpt'] == "#en.wikipedia":
           
        
        timestamp = str(datetime.datetime.utcnow())
        file.write(timestamp+ " ")
        msg = regex.sub("",str(message['text']))
        file.write(msg)
        print msg
        file.write("</br>")
        
        parsemessage(message)
file.write("</body></html>")
#anyway in infinite loop. how will this be executed solve #issue1
   
   
