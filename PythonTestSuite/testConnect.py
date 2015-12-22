import microgear.client as client
import time
import os
import microgear
import unittest
import logging
from testfixtures import LogCapture
import threading


class TestCreateAndConnect(unittest.TestCase):
    def setUp(self):
        self.gearkey = "qnlgzsPUUxYeyQP"
        self.gearsecret = "1euJPvxybllEPQZzq2u9wpRJXDbjM7"
        self.appid = "testNo3"
        
    def tearDown(self):
        if(os.path.isfile("microgear.cache")):
            os.remove("microgear.cache")
        
    def helperForConnect(self):
        client.connect()
        print("done")
        
    def helperForDebuglog(self):      
        threads = []
        t = threading.Thread(target=self.helperForConnect)
        threads.append(t)
        logs = LogCapture(level=logging.DEBUG)
        t.start()
        debugDetected = False
        timeout = time.time() + 1.0
        while(not debugDetected and time.time() < timeout):
            if 'DEBUG' in str(logs):
                debugDetected = True
            time.sleep(3)
        return logs

        
    def helperForErrorlog(self):      
        threads = []
        t = threading.Thread(target=self.helperForConnect)
        threads.append(t)
        logs = LogCapture(level=logging.ERROR)

        t.start()
        errorDetected = False
        timeout = time.time() + 30.0
        while(not errorDetected and time.time() < timeout):
            if 'Request token is not issued, please check your appkey and appsecret.' in str(logs):
                errorDetected = True
            time.sleep(3)
        print(logs)
        assert('Request token is not issued, please check your appkey and appsecret.' in str(logs))
        assert('Any other error.' not in str(logs))       

    #def testConnectWithValidInput(self):
        #self.connected = False
        #def on_connected():
            #self.connected = True
        #client.on_connect = on_connected
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})   
        #client.connect()
        #timeout = time.time() + 30.0
        #if(time.time() > timeout or self.connected):
            #self.assertTrue(self.connected)
    
        
    #def testConnectWithEmptyGearkey(self):
        #self.gearkey = ""
        #print(self.gearkey)
        #self.helperForErrorlog()        

    #def testConnectWithEmptyGearSecret(self):
        #self.gearsecret = ""
        #print(self.gearsecret)
        #self.helperForErrorlog()        
        
    #@unittest.skip("Would fail due to no proper handling is taken.")
    #def testConnectWithEmptyAppId(self):
        #print("yay")
        #self.appid = ""
        #self.helperForErrorlog()  
     
            
    #def testConnectWithInvalidCaseGearKey(self):
        #self.gearkey = self.gearkey.upper()
        #print("gear key" + self.gearkey)
        #self.helperForErrorlog()
 
        
    #def testConnectWithInvalidCaseGearSecret(self):
        #self.gearsecret = self.gearsecret.upper()
        #print(self.gearsecret)
        #self.helperForErrorlog()
        
    #@unittest.skip("to do")
    #def testConnectWithInvalidCaseAppId(self):
        #self.appid = self.appid.upper()
        #print(self.appid)
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})   
        
        #def on_connection(self):
            #client.on_connect = on_connection
            
    #def testConnectWithLessGearKey(self):
        #self.gearsecret = self.gearsecret[:-2]
        #self.helperForErrorlog()
    #def testConnectWithMoreGearKey2(self):
        #self.gearkey = self.gearkey + "x"
        #self.helperForErrorlog()
        
    #def testConnectWithLessGearSecret(self):   
        #self.gearsecret = self.gearsecret[:-2]
        #self.helperForErrorlog()    
    #def testConnectWithMoreGearSecret(self):
        #self.gearsecret = self.gearsecret + "x"
        #self.helperForErrorlog()    
        
    #def testConnectWithLessAppId(self):
        #self.appid = self.appid[:-2]
        #print(self.appid)    
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})
        #client.connect()

    @unittest.skip("Will fail")
    def testConnectWithMoreAppId(self):
        self.appid = self.appid + "x"
        print(self.appid)
        self.helperForDebuglog()
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})
        #client.connect()        
 
    #def testConnectWithInvalidGearKey(self):
        #self.gearkey = self.gearkey.replace(self.gearkey[-1], "!")
        #print(self.gearkey)
        #self.helperForErrorlog()
    #def testConnectWithInvalidGearSecret(self):
        #self.gearsecret = self.gearsecret.replace(self.gearsecret[-1], "!")
        #print(self.gearsecret)    
        #self.helperForErrorlog()
    @unittest.skip("not yet")
    def testConnectWithInvalidAppId(self):
        self.appid = self.appid + self.appid.replace(self.appid[-1], "!")
        print(self.appid)
        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})
        client.connect()    
        
    #def testConnectWithDebugTrue(self):
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})
        #logs = self.helperForDebuglog()
        #print(logs)
        #assert('DEBUG' in str(logs)) 
    
    @unittest.skip("not yet")
    def testConnectWithDebugFalse(self):
        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "False"})
        logs = self.helperForDebuglog()
        print(logs)
        assert('DEBUG' not in str(logs))         

        
    #def testConnectWillBlockTrue(self):
        #client.create(gearkey, gearsecret, appid, {'debugmode': "True"})
        #client.connect(True)   
            
    def testConnectWillBlockFalse(self):
        self.connected = False
        def on_connected():
            self.connected = True
        client.on_connect = on_connected
        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})   
        client.connect(False)
        timeout = time.time() + 30.0
        if(time.time() > timeout or self.connected):
            self.assertTrue(self.connected)

    #def testResettoken(self):
        #client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})   
        #client.connect()
        #self.assertTrue(os.path.isfile("microgear.cache"))
        #client.resettoken()
        #if (os.path.isfile("microgear.cache")):
            #self.fail()
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()    