import microgear.client as client
import time
import microgear
import unittest
import logging
import os
from testfixtures import LogCapture
from testfixtures import *
import threading


def connectTo():
    gearkey = "qnlgzsPUUxYeyQP"
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
    appid = "testNo3"    
    client.create(gearkey, gearsecret, appid, {'debugmode': "True"})
    
    def on_connected():
        print("connect")
    def on_closed():
        print("close")  
    def on_rejected():
        print("reject")     
    def on_error():
        print("error")  
    def on_message():
        print("message")  
    def on_present():
        print("present")
    def on_absent():
        print("absent") 
    client.on_connect = on_connected
    client.on_error = on_error
    client.on_present = on_present
    client.on_absent = on_absent
    client.on_rejected = on_rejected
    client.on_closed = on_closed
    client.on_message = on_message
    logs = LogCapture()
    client.connect()
    print(logs)
    logs.check(('root', 'DEBUG', 'Check stored token.'))

def testAlias():
    gearkey = "qnlgzsPUUxYeyQP"
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
    appid = "testNo3"    

    client.create(gearkey, gearsecret, appid, {'debugmode': "True", 'alias': "Python"})
    client.connect()
    while True:
        pass
def testScopeChat():
    gearkey = "qnlgzsPUUxYeyQP"
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
    appid = "testNo3"    

    client.create(gearkey, gearsecret, appid, {'debugmode': "True", 'scope': "chat:receiver"})
    client.setname("sender")
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:
        client.chat("not receiver","How are you?")
        time.sleep(3) 
def test():
    gearkey = "qnlgzsPUUxYeyQP"
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
    appid = "testNo3"    
    if(os.path.isfile("microgear.cache")):
        f = open((os.getcwd() + "/microgear.cache"), 'r')
        print(f.readlines())
        f.close()  
    
    else:
        print("yes1")       
    client.create(gearkey, gearsecret, appid, {'debugmode': "True", 'scope': "chat:receiver"})
    client.setname("sender")
    if(os.path.isfile("microgear.cache")):
        f = open((os.getcwd() + "/microgear.cache"), 'r')
        print(f.readlines())
        f.close() 
    else:
        print("yes2")    
    client.connect()
    f = open((os.getcwd() + "/microgear.cache"), 'r')
    print(f.readlines())
    f.close()
    client.resettoken()
    if(os.path.isfile("microgear.cache")):
        f = open((os.getcwd() + "/microgear.cache"), 'r')
        print(f.readlines())
        f.close()
    else:
        print("yes3")

    
    
#def testChat2():
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    #appid = "p107microgear"
    
    #client.create(gearkey , gearsecret, appid, {'debugmode': True})
    #client.setname("Python ja")
    #client.connect()
    
    #def receive_message(topic, message):
        #print topic + " " + message
        
 
    #while True:
        #client.chat("Html ka","How are you?")
        #time.sleep(3)
        #client.on_message = receive_message    
    
#print(os.path.isfile("microgear.cache"))
#if(os.path.isfile("microgear.cache")):
    #os.remove("microgear.cache")
    #print(os.path.isfile("microgear.cache"))
test()