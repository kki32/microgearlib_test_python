#!/usr/bin/env python

import time
import os
import unittest
import logging
import unittest.mock
import microgear
import microgear.client as client
from unittest.mock import MagicMock
import subprocess
#from testfixtures import LogCapture
#import threading
connect_timeout = 4
message_timeout = 4

class TestResettoken(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"

        self.helperGearname = "helper"
        self.message = 'hello'
        self.topic = '/firstTopic'
        self.expectedMessage = str(self.message.encode('utf-8')) #convert to bytes
        self.expectedMsgTopic = "/" + self.appid + "/gearname/" + self.gearname
        self.expectedTopic = "/" + self.appid + self.topic
        self.received = False
        #clear microgear.cache file
        cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "w")
        print(cache_file)
        cache_file.write("")
        cache_file.close()    
        
        receiver_file = open(os.path.join(os.getcwd()+"/receiver.txt"), "w")
        print(receiver_file)
        receiver_file.write("")
        receiver_file.close()   

    def tearDown(self):
        #delete receive txt
        os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
   
  
    #fail
    # def testCode8Case3(self):  
    #     """resettoken twice"""
    #     self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

    #     self.assertIsNone(microgear.gearkey)
    #     self.assertIsNone(microgear.gearsecret)    
    #     self.assertIsNone(microgear.appid)
        
    #     client.create(self.gearkey, self.gearsecret, self.appid)
       
    #     client.on_connect = MagicMock()

    #     client.resettoken()
    #     time.sleep(2)
    #     self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
    #     # client.resettoken()
    #     # time.sleep(2)
    #     # self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
    #     client.connect()
    #     time.sleep(connect_timeout)
    #     self.assertTrue(client.on_connect.called)
    #     self.assertEqual(client.on_connect.call_count, 1)
    #     self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

    def testCode8Case2(self):  
        """resettoken when have microgear.cache while microgear is offline"""
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()

        client.resettoken()
        self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

    

# def main():
    # pass
#     #suite = unittest.TestSuite()
#     #suite.addTest(TestChat("testCode4Case2"))
#     #runner = unittest.TextTestRunner()
#     #runner.run(suite)
#     print(os.path.join(os.getcwd(),"microgear.cache"))    
#     unittest.main()

# if __name__ == '__main__':
#     main()    