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
gearkey = "qnlgzsPUUxYeyQP"
gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
appid = "testNo3"

client.create(gearkey , gearsecret, appid, {'debugmode': True})

client.setname("Conan")
client.connect()

while True:
    client.chat("do", message)

    
#while True:
    #client.chat("Unicare","Hello world.")
    #time.sleep(5)
#testCreateNetPie()
#testSetName()
