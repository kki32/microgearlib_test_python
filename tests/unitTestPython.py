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



class TestPublish(unittest.TestCase):
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

        #clear microgear.cache file
        cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "w")
        print(cache_file)
        cache_file.write("")
        cache_file.close()

        receiver_file = open(os.path.join(os.getcwd()+"/receiver.txt"), "w")
        print(receiver_file)
        receiver_file.write("")
        receiver_file.close()

        imp.reload(client)
        imp.reload(microgear) 
         
    def tearDown(self):
        #delete receive txt
        print('tearDown')
        os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
        if(self.connected):
            microgear.mqtt_client.disconnect()
 

 
    #helper 61
    def testCode7Case1(self):  
        """publish topic after some microgear subscribe that topic""" 
        try:
            print("run helper...")
            code = str(61)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)

            client.publish(self.topic, self.message)
            time.sleep(message_timeout)

            receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
            received_message = receiver_file.read()
            receiver_file.close()
            print(received_message)
            print('received')
            if(received_message == self.message):
                self.received = True
            self.assertTrue(self.received)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 
    #helper 61
    def testCode7Case3(self):  
        """publish topic that has no subscriber"""
        try:
            print("run helper...")
            code = str(61)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.anotherTopic = "/secondTopic"
            
            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)

            client.publish(self.anotherTopic, self.message)
            time.sleep(message_timeout)

            receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
            received_message = receiver_file.read()
            receiver_file.close()
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 
    #fail due to subscribe empty topic fail
    #helper 61
    def testCode7Case4(self):  
        """publish empty string topic"""
        try:
            print("run helper...")
            code = str(61)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.anotherTopic = "/secondTopic"
            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)

            client.publish(self.anotherTopic, self.message)
            time.sleep(message_timeout)

            receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
            received_message = receiver_file.read()
            receiver_file.close()
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 
    #helper 61
    def testCode7Case5(self):
        """publish invalid topic - no slash"""
        try:
            print("run helper...")
            code = str(61)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.invalidTopic = "firstTopic"
            
            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)

            client.publish(self.invalidTopic, self.message)
            time.sleep(message_timeout)

            receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
            received_message = receiver_file.read()
            receiver_file.close()
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            self.assertTrue(client.on_connect.call_count > 1)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 


def main():
    #suite = unittest.TestSuite()
    #suite.addTest(TestChat("testCode4Case2"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    print(os.path.join(os.getcwd(),"microgear.cache"))    
    unittest.main()

if __name__ == '__main__':
    main()    