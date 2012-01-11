import pyirclib
import string
import sys
import time

irc = pyirclib.Irclib('irc.wikimedia.org',6667)
irc.setDebug = 1
irc.login('client',username = 'karmabot')
irc.join("#en.wikipedia")

#irc.privmsg("#en.wikipedia","hi future developers!")

def parsemessage(msg):
  if msg['event'] == "PRIVMSG" and str(msg['text']) == "!NAMES":
    print irc.names()
while 1:
  message = irc.getmessage()
  print message
  parsemessage(message)
   
   
