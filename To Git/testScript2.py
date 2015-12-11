#general case - blue sky scenario
#requirement: connect for the first time

import microgear.client as client
import time
import unittest

#class TestMicrogearInPython(unittest.TestCase):
    #def testGear(self):
        #self.failUnless()

#def main():
    #unittest.main()
    
#if __name__ == '__main__':
    #main()    

def testCreateNetPie1():
    gearkey = "qnlgzsPUUxYeyQP"
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
    appid = "testNo3"
    return gearkey, gearsecret, appid

def testCreateNetPie2():
    gearkey = ""
    gearsecret = ""
    appid = ""
    return gearkey, gearsecret, appid
   
def testCreateNetPie3():
    gearkey = "qnlgzsPUUxYeQp"    
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjpM7"
    appid = "testn3"
    return gearkey, gearsecret, appid
    
def testCreateNetPie4():   
    gearkey = "qnlgzsPUUxYeyQP" 
    gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjm7"    
    appid = "testno3"
    return gearkey, gearsecret, appid
    
def testCreateNetPie():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'debugmode': True})
    client.connect()
    print("Sleep for 5 seconds")
    time.sleep(5)
    

#def testSetName():

def testChat():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname("Python ja")
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
        
 
    while True:
        client.chat("Html ka","Hello world.")
        time.sleep(3)
        client.on_message = receive_message

def testPublish():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname("Python ja")
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:
        client.publish("/LetsShare","Happy New Year!")
        time.sleep(3)
        client.on_message = receive_message
        
def testSubscribe():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname("Python ja")
    client.subscribe("/Hi")
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:     
        time.sleep(3)
        print("receive something")
        client.on_message = receive_message

        
def testUnSubscribe():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname("Python ja")
    client.subscribe("/LetsShare")
    client.connect()
    
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:
        
        time.sleep(3)
        client.on_message = receive_message

    
#testCreateNetPie()
#testSetName()
#testChat()
testSubscribe()
#testUnSubscribe()
