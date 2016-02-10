#!/usr/bin/env python
#export PYTHONWARNINGS="ignore"
#TODO: resettoken should return null for microgear
#todo: if fail, need to find way to kill process
#TODO: chat no 7
#TODO: make failing test pass if possible
import time
import os
import unittest
import logging
import unittest.mock
import imp
import microgear
import microgear.client as client
        
from unittest.mock import MagicMock
import subprocess
#from testfixtures import LogCapture
#import threading
connect_timeout = 4
message_timeout = 6
connect_worst_timeout = 30
helper_dir = os.path.join(os.getcwd()) + '/helpers'


receiver_file = os.path.join(os.getcwd(),"receiver.txt")
microgear_cache = os.path.join(os.getcwd(),"microgear.cache")

class TestResettoken(unittest.TestCase):
    def setUp(self):
        print('setUp')

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
        self.connected = False

        # # #clear microgear.cache file
        # cache_file = open(microgear_cache, "w")
        # print(cache_file)
        # cache_file.write("")
        # cache_file.close()
        if(os.path.isfile(microgear_cache):
            os.remove(microgear_cache)

        r_file = open(receiver_file, "w")
        print(r_file)
        r_file.write("")
        r_file.close()

        imp.reload(client)
        imp.reload(microgear) 
         
    def tearDown(self):
        #delete receive txt
        print('tearDown')
        os.remove(receiver_file)
        if(self.connected):
            microgear.mqtt_client.disconnect()
  
    # def testCode8Case1(self):  
    #     """resettoken when no microgear.cache
    #         pre-requisite: no microgear.cache file""" 
    #     if(os.path.isfile(microgear_cache)):
    #         os.remove(microgear_cache)

    #     self.assertIsNone(microgear.gearkey)
    #     self.assertIsNone(microgear.gearsecret)    
    #     self.assertIsNone(microgear.appid)
        
    #     client.create(self.gearkey, self.gearsecret, self.appid)
       
    #     client.on_connect = MagicMock()

    #     client.resettoken()
    #     self.assertFalse(os.path.isfile(microgear_cache))
   

    def testCode8Case2(self):  
        """resettoken when have microgear.cache while microgear is offline"""
        #pre-requisite: ensure there is microgear.cache
  

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': True})
        client.connect(False)
        self.assertTrue(os.path.isfile(microgear_cache))
        #resettoken when have microgear.cache
        
        client.resettoken()

        time.sleep(4)
        #should delete microgear.cache
        self.assertFalse(os.path.isfile(microgear_cache))

    
    def testCode8Case3(self):  
        """resettoken twice"""
        self.assertTrue(os.path.isfile(microgear_cache))

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': True})
        client.connect(False)
        self.assertTrue(os.path.isfile(microgear_cache))

        client.resettoken()
        self.assertFalse(os.path.isfile(microgear_cache))
        client.resettoken()
        self.assertFalse(os.path.isfile(microgear_cache))

        client.on_connect = MagicMock()
        #should not affect connect
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertTrue(os.path.isfile(microgear_cache))
    


def main():
    #suite = unittest.TestSuite()
    #suite.addTest(TestChat("testCode4Case2"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    print(os.path.join(os.getcwd(),"microgear.cache"))    
    unittest.main()

if __name__ == '__main__':
    main()    