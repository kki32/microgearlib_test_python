#general case - blue sky scenario
#requirement: connect for the first time

import microgear.client as client
import time

def testResetToken():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"
 
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname("Python ja")
    client.setname("Not Python ja")

    client.connect()
    
    def receive_message(topic, message):
        print topic + " " + message
    
    while True:     
        time.sleep(3)
        print("hello")
        client.on_message = receive_message
        

                
    
testResetToken()

