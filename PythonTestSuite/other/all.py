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



class TestChat(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.helperGearname = "helper"
        self.message = 'hello'
        self.expectedMessage = str(self.message.encode('utf-8')) #convert to bytes
        self.expectedMsgTopic = "/" + self.appid + "/gearname/" + self.gearname
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

    def testCode4Case1(self):
        """chat with itself"""   
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)
        client.on_message = MagicMock()
        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        client.chat(self.gearname, self.message)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_once_with(self.expectedMsgTopic, self.expectedMessage)
        
    #require helper 31
    def testCode4Case2(self):
        """chat with other microgear in same appid"""  
        print("run main...")

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()        
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertTrue(self.received)
    
    #helper 11
    def testCode4Case3(self):
        """chat with other microgear in different appid"""   

       
        print("run main...")

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)

        #helper 31
        #helper 33
    def testCode4Case5(self):
        """chat to microgear which shares the same name as itself"""   
        print("run main...")
        self.helperGearname = self.gearname
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.on_message = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_once_with(self.expectedMsgTopic, self.expectedMessage)
        
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertTrue(self.received)
    #helper 12
    def testCode4Case6(self):
        """chat with other microgear which shares the same gearname in different appid"""   
        print("run main...")
        self.helperGearname = self.gearname
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.on_message = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_once_with(self.expectedMsgTopic, self.expectedMessage)
        
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
            
        self.assertFalse(self.received)

        #helper 31
    
    #helper 32
    def testCode4Case8(self):
        """chat to microgear which has gearname similar to topic"""   
        print("run main...")
        self.gearname = '/firstTopic'
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
     #helper 34
    #helper 34
    def testCode4Case9(self):
        """chat with other microgear which has empty string as gearname"""   
        print("run main...")
        self.helperGearname = ""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

    
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)
    
        client.on_connect = MagicMock()
    
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        print(self.helperGearname, "empty")
        
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
    
    #helper 61
    def testCode4Case10(self):
        """chat to topic which has subscriber"""   
        print("run main...")
        self.gearname = '/firstTopic'
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)

class TestSubscribe(unittest.TestCase):
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

    #helper 51
    def testCode5Case1(self):   
        """subscribe one topic"""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)   

        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

    #helper 51
    def testCode5Case2(self):   
        """subscribe same topic twice"""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
        client.subscribe(self.topic)
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)   

        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

    #helper 51
    def testCode5Case3(self):   
        """subscribe same topic twice"""

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        #unsubscribe after receive message
        client.unsubscribe(self.topic)
        client.on_message.reset_mock() #reset count recorded by mock
        self.assertFalse(client.on_message.called)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called) #should not receive message now
        client.subscribe(self.topic) #subscribe again
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called) #should receive message


    def testCode5Case4(self):   
        """subscribe the topic that it publishes"""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.topic, self.message)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

    #helper 51
    def testCode5Case5x1(self):   
        """subscribe empty topic"""
        self.topic = ""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)
    #fail
    #helper 52
    def testCode5Case5x2(self):   
        """subscribe empty topic"""
        self.topic = ""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)

    #helper 51 should publish topic
    def testCode5Case6x1(self):   
        """subscribe invalid topic - no slash"""
        self.topic = "firstTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)
    #helper 53 should publish invalid topic
    def testCode5Case6x2(self):   
        """subscribe invalid topic - no slash"""
        self.topic = "firstTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)  



class TestUnsubscribe(unittest.TestCase):
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
 
    #helper 51
    def testCode6Case1(self):  
        """unsubscribe the subscribed topic""" 
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1) 

        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.unsubscribe(self.topic)
        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)
        #helper 51
    def testCode6Case2(self):  
        """unsubscribe the topic before subscribe""" 
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1) 
        self.assertFalse(client.on_message.called)
        client.unsubscribe(self.topic)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        #helper 51
    def testCode6Case3(self):  
        """unsubscribe the same topic twice""" 
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)
        client.unsubscribe(self.topic)
        time.sleep(connect_timeout)
        self.assertFalse(client.on_message.called)
        client.unsubscribe(self.topic)
        time.sleep(connect_timeout)
        self.assertFalse(client.on_message.called)

    #helper 51 to publish topic
    def testCode6Case4x1(self):  
        """unsubscribe the empty topic""" 
        self.emptyStr = ""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)

        client.unsubscribe(emptyStr)
        time.sleep(connect_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

    #fail due to subscribe to empty string fail
    #helper 52 to publish empty string topic
    def testCode6Case4x2(self):  
        """unsubscribe the empty topic"""
        self.topic = ""
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)

        client.unsubscribe(self.topic)
        time.sleep(connect_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
        #helper 51
    def testCode6Case5x1(self):  
        """unsubscribe the invalid topic - no slash""" 
        self.invalidStr = "firstTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)

        client.unsubscribe(self.invalidStr)
        time.sleep(connect_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
    

    #helper 51
    def testCode6Case6(self):  
        """unsubscribe the topic that is not subscribed""" 
        self.anotherTopic = "/secondTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertFalse(client.on_message.called)
        client.subscribe(self.topic)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

        client.on_message.reset_mock()
        self.assertFalse(client.on_message.called)

        client.unsubscribe(self.anotherTopic)
        time.sleep(connect_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

class TestPublish(unittest.TestCase):
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
 
    #helper 61
    def testCode7Case1(self):  
        """publish topic after some microgear subscribe that topic""" 
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.topic, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertTrue(self.received)
    #helper 61
    def testCode7Case3(self):  
        """publish topic that has no subscriber""" 
        self.anotherTopic = "/secondTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.anotherTopic, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
    
    #fail due to subscribe empty topic fail
    #helper 61
    def testCode7Case4(self):  
        """publish empty string topic""" 
        self.anotherTopic = "/secondTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.anotherTopic, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)

        #helper 61
    def testCode7Case5(self):  
        """publish invalid topic - no slash""" 
        self.invalidTopic = "firstTopic"
        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()
      
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.invalidTopic, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
        self.assertTrue(client.on_connect.call_count > 1)


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
   
  
    def testCode8Case1(self):  
        """resettoken when no microgear.cache
            pre-requisite: no microgear.cache file""" 
        if(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache"))):
            os.remove(os.path.join(os.getcwd()+"/microgear.cache"))

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

    #fail
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

    def testCode8Case3(self):  
        """resettoken twice"""
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid)
       
        client.on_connect = MagicMock()

        client.resettoken()
        self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
        client.resettoken()
        self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.assertEqual(client.on_connect.call_count, 1)
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))
    

def main():
    #suite = unittest.TestSuite()
    #suite.addTest(TestChat("testCode4Case2"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)    
    unittest.main()
    
if __name__ == '__main__':
    main()    