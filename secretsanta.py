#!/usr/bin/python

import random
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

wichtel = {
    "Andrea": "amxe",
    "Klaus": "klabe",
    "Max": "made",
    "Sarah": "sxde",    
    "Benjamin": "bede"
}
receivers = list(wichtel)
givers = list(wichtel)
secret = {}

def uniqueGiver(receiver):
    i = 0
    while (i < 100):
        i = i + 1
        x = random.randint(0, len(givers) - 1)
        if (givers[x] == receiver): continue
        return givers.pop(x)
    return "---"
        
def shuffle():
    for i in range(len(receivers)):
        receiver = receivers[i]
        giver = uniqueGiver(receiver)
        secret[receiver] = giver

def sendMail(giverName, receiverName):
    print "Send mail to", giverName, "(" + `wichtel[giverName]` + ")"
    msg = MIMEText("Es ist " + receiverName + "!")
    msg["From"] = "wit"
    msg["To"] = wichtel[giverName]
    msg["Subject"] = giverName + ", dein Wichtel steht fest :-)"
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())
        
shuffle()
for i in secret:
    if i == "---": 
	    print "ooooooh nooooo!"
	    exit()
y = raw_input("Hit (y)es to send mails out! ")
if y != "y":
    print "Invalid input, exit!"
    exit()
for i in secret:
    sendMail(secret[i], i)
