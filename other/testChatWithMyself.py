import microgear.client as client
import time
import os
def testChat():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"

    origin = "oriA"
    destination = "destX"
    
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    bf = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
    print(bf)
    client.resettoken()
    af = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
    print(af)
testChat()