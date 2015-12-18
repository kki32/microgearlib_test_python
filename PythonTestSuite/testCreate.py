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
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    return gearkey, gearsecret, appid

def testCreateNetPie21():
    gearkey = ""
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = ""
    #appid = "p107microgear"    
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    #appid = ""
    
    return gearkey, gearsecret, appid
   
def testCreateNetPie22():
    gearkey = "ExhoyeQoTyJs5ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBSH"
    appid = "p107microgear"
    
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgeAR"
    
    return gearkey, gearsecret, appid
    
def testCreateNetPie231():   
    gearkey = "ExhoyeQoTyJS5"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjB"
    #appid = "p107microgear"
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    #appid = "p107microge"    
    return gearkey, gearsecret, appid

def testCreateNetPie232():   
    gearkey = "ExhoyeQoTyJS5Accc"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBshbb"
    appid = "p107microgear"
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBshhh"
    #appid = "p107microgear"
    
    #gearkey = "ExhoyeQoTyJS5Ac"
    #gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    #appid = "p107microgearrr"    
    return gearkey, gearsecret, appid
    
def testCreateNetPieDebug():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'debugmode' : False})
    client.connect()
    print("Sleep for 20 seconds")
    time.sleep(100)
    

def testCreateNetPieLabel():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'label' : "Microgear Python"})
    client.setname('logg')
    client.connect()
    print("Sleep for 90 seconds")
    time.sleep(90)
        

def testCreateNetPieScopeName():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'debugmode' : True, 'scope' : "name:logger"})
    client.setname('logg')
    client.connect()
    print("Sleep for 90 seconds")
    time.sleep(90)
    
def testCreateNetPieScopeChat():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'debugmode' : True, 'scope' : "chat:java ja"})
    client.setname('Python ja')
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while(True):
        client.chat('Html ka', "Hello html")
        time.sleep(3)
        client.on_message = receive_message
    
def testCreateNetPieScopeW():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
    client.create(gearkey , gearsecret, appid, {'debugmode': True,'scope': "r:/LetsShare" })
    client.create(gearkey , gearsecret, appid, {'debugmode': True,'scope': "w:/LetsShare" })
    client.setname("Python ja")
    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:
        client.publish("/StopsShare","Happy New Year!")
        time.sleep(3)
        client.on_message = receive_message
        
def testCreateNetPieScopeR():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear" 
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True, 'scope': "r:/LetsShare,w:/LetsShare"})
    client.setname("Python ja")
    #client.subscribe("/LetsShare")
    client.subscribe("/LetsPlay")
    client.connect()

    def receive_message(topic, message):
        print topic + " " + message
    
    while True:     
        time.sleep(3)
        client.on_message = receive_message


def testCreateNetPieConnection():
    gearkey, gearsecret, appid = testCreateNetPie1();
    client.create(gearkey, gearsecret, appid, {'debugmode' : False})
    
    def on_connection():
        print "I am connected"
    client.on_connect = on_connection
    print(client.on_connect == 0)
    client.connect()
    print("Sleep for 100 seconds")
    time.sleep(100)


testCreateNetPieConnection()