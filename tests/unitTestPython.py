#!/usr/bin/env python
#export PYTHONWARNINGS="ignore"
#TODO: resettoken should return null for microgear
#todo: if fail, need to find way to kill process
#TODO: chat no 7
import time
import os
import unittest
import logging
import unittest.mock
import imp
# import microgear
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



class TestSubscribe(unittest.TestCase):
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

    #helper 51
    def testCode5Case1(self):   
        """subscribe one topic"""
        try:
            print('Code5Case1')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)   

            time.sleep(message_timeout)
            self.assertTrue(client.on_message.called)
            client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
            p.kill()
                            #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)


    #helper 51
    def testCode5Case2(self):   
        """subscribe same topic twice"""
        try:
            print('Code5Case2')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
            client.subscribe(self.topic)
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)   

            time.sleep(message_timeout)
            self.assertTrue(client.on_message.called)
            client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
            p.kill()
                            #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 51
    def testCode5Case3(self):   
        """subscribe same topic twice"""
        try:
            print('Code5Case3')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)
            
            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
       
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            connected = True
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
            p.kill()
                            #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    def testCode5Case4(self):   
        """subscribe the topic that it publishes"""
        print('Code5Case4')
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.subscribe(self.topic)
   
        client.on_connect = MagicMock()
        client.on_message = MagicMock()
       
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True
        self.assertEqual(client.on_connect.call_count, 1)

        client.publish(self.topic, self.message)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

    #helper 51
    def testCode5Case5x1(self):   
        """subscribe empty topic"""
        try:
            print('Code5Case5x1')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)
            self.topic = ""

            
            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
       
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)
            time.sleep(message_timeout)
            self.assertFalse(client.on_message.called)
            p.kill()

                                    #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)
    
    # fail
    # helper 52
    def testCode5Case5x2(self):   
        """subscribe empty topic"""
        try:
            print('Code5Case5x1')
            print("run helper...")
            code = str(52)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.topic = ""
            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
       
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)
            time.sleep(message_timeout)
            self.assertFalse(client.on_message.called)
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 51 should publish topic
    def testCode5Case6x1(self):   
        """subscribe invalid topic - no slash"""
        try:
            print('Code5Case6x1')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)
            self.topic = "firstTopic"
            
            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
       
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)
            time.sleep(message_timeout)
            self.assertFalse(client.on_message.called)
            p.kill()

        #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 53 should publish invalid topic
    def testCode5Case6x2(self):
        """subscribe invalid topic - no slash"""
        try:
            print('Code5Case6x2')   
            print("run helper...")
            code = str(53)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.topic = "firstTopic"

            client.create(self.gearkey, self.gearsecret, self.appid)
            client.subscribe(self.topic)
       
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
           
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)
            time.sleep(message_timeout)
            self.assertFalse(client.on_message.called)  
            p.kill()

                                    #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

        #helper 51
    def testCode6Case1(self):  
        """unsubscribe the subscribed topic"""
        print('Code6Case1')
        try: 
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1) 

            client.subscribe(self.topic)
            time.sleep(message_timeout)
            self.assertTrue(client.on_message.called)
            client.unsubscribe(self.topic)
            client.on_message.reset_mock()
            self.assertFalse(client.on_message.called)
            time.sleep(message_timeout)
            self.assertFalse(client.on_message.called)
            p.kill()

        #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args) 
    # helper 51
    def testCode6Case2(self):  
        """unsubscribe the topic before subscribe""" 
        print('Code6Case2')

        print(microgear.gearkey)
 
        try:
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)
            print(microgear.gearkey)
            client.create(self.gearkey, self.gearsecret, self.appid)

            client.on_connect = MagicMock()
            client.on_message = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1) 
            self.assertFalse(client.on_message.called)
            client.unsubscribe(self.topic)
            self.assertFalse(client.on_message.called)
            client.subscribe(self.topic)
            time.sleep(message_timeout)
            self.assertTrue(client.on_message.called)
            client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
            p.kill()

        except Exception as e:
            p.kill()
            raise Exception(e.args) 

    #helper 51
    def testCode6Case3(self):  
        """unsubscribe the same topic twice"""

        print(microgear.gearkey)
    
        try:
            print('Code6Case3')
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)
            print(microgear.gearkey)
            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
            self.assertFalse(client.on_connect.called)
            self.assertFalse(client.on_message.called)

            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
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
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 

    #helper 51 to publish topic
    def testCode6Case4x1(self):  
        """unsubscribe the empty topic"""
        print('Code6Case4x1')
        try:
            print("run helper...")
            code = str(51)
            args = ['python', 'helper.py', code]
            p = subprocess.Popen(args, cwd=(helper_dir))
            time.sleep(connect_worst_timeout)

            self.emptyStr = ""

            
            client.create(self.gearkey, self.gearsecret, self.appid)
           
            client.on_connect = MagicMock()
            client.on_message = MagicMock()
          
            client.connect()
            time.sleep(connect_timeout)
            self.assertTrue(client.on_connect.called)
            self.connected = True
            self.assertEqual(client.on_connect.call_count, 1)
            self.assertFalse(client.on_message.called)
            client.subscribe(self.topic)
            time.sleep(message_timeout)
            self.assertTrue(client.on_message.called)
            client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

            client.on_message.reset_mock()
            self.assertFalse(client.on_message.called)

            client.unsubscribe(self.emptyStr)
            time.sleep(connect_timeout)
            self.assertTrue(client.on_message.called)
            client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 

# class TestUnsubscribe(unittest.TestCase):
#     def setUp(self):
#         print('setUp')

#         self.gearkey = "yMPSuoFBV6Ao322"
#         self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
#         self.appid = "testPython"
#         self.gearname = "mainPython"


#         self.helperGearname = "helper"
#         self.message = 'hello'
#         self.topic = '/firstTopic'
#         self.expectedMessage = str(self.message.encode('utf-8')) #convert to bytes
#         self.expectedMsgTopic = "/" + self.appid + "/gearname/" + self.gearname
#         self.expectedTopic = "/" + self.appid + self.topic
#         self.received = False
#         self.connected = False

#         #clear microgear.cache file
#         cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "w")
#         print(cache_file)
#         cache_file.write("")
#         cache_file.close()

#         receiver_file = open(os.path.join(os.getcwd()+"/receiver.txt"), "w")
#         print(receiver_file)
#         receiver_file.write("")
#         receiver_file.close()

#         imp.reload(client)
#         imp.reload(microgear) 
         
#     def tearDown(self):
#         #delete receive txt
#         print('tearDown')
#         os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
#         if(self.connected):
#             microgear.mqtt_client.disconnect()
 
#     #helper 51
#     def testCode6Case1(self):  
#         """unsubscribe the subscribed topic"""
#         try: 
#             print("run helper...")
#             code = str(51)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)

#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1) 

#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)
#             client.unsubscribe(self.topic)
#             client.on_message.reset_mock()
#             self.assertFalse(client.on_message.called)
#             time.sleep(message_timeout)
#             self.assertFalse(client.on_message.called)
#             p.kill()

#         #if fails due to assertion error
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 
#     #helper 51
#     def testCode6Case2(self):  
#         """unsubscribe the topic before subscribe""" 

#         try:
#             print("run helper...")
#             code = str(51)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)

#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1) 
#             self.assertFalse(client.on_message.called)
#             client.unsubscribe(self.topic)
#             self.assertFalse(client.on_message.called)
#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#             p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 

#     #helper 51
#     def testCode6Case3(self):  
#         """unsubscribe the same topic twice"""
#         try:
#             print("run helper...")
#             code = str(51)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)
            
#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1)
#             self.assertFalse(client.on_message.called)
#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#             client.on_message.reset_mock()
#             self.assertFalse(client.on_message.called)
#             client.unsubscribe(self.topic)
#             time.sleep(connect_timeout)
#             self.assertFalse(client.on_message.called)
#             client.unsubscribe(self.topic)
#             time.sleep(connect_timeout)
#             self.assertFalse(client.on_message.called)
#             p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 

#     #helper 51 to publish topic
#     def testCode6Case4x1(self):  
#         """unsubscribe the empty topic""" 
#         print("run helper...")
#         code = str(51)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)

#         self.emptyStr = ""

        
#         client.create(self.gearkey, self.gearsecret, self.appid)
       
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
      
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)
#         self.assertFalse(client.on_message.called)
#         client.subscribe(self.topic)
#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#         client.on_message.reset_mock()
#         self.assertFalse(client.on_message.called)

#         client.unsubscribe(emptyStr)
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#         p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 

#     #fail due to subscribe to empty string fail
#     #helper 52 to publish empty string topic
#     def testCode6Case4x2(self):  
#         """unsubscribe the empty topic"""
#         try:
#             print("run helper...")
#             code = str(52)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)

#             self.topic = ""
      
            
#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1)
#             self.assertFalse(client.on_message.called)
#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)

#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#             client.on_message.reset_mock()
#             self.assertFalse(client.on_message.called)

#             client.unsubscribe(self.topic)
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#             p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 

#     #helper 51
#     def testCode6Case5x1(self):  
#         """unsubscribe the invalid topic - no slash"""
#         try:
#             print("run helper...")
#             code = str(51)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)

#             self.invalidStr = "firstTopic"
     
#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1)
#             self.assertFalse(client.on_message.called)
#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#             client.on_message.reset_mock()
#             self.assertFalse(client.on_message.called)

#             client.unsubscribe(self.invalidStr)
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#             p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 
#     #helper 51
#     def testCode6Case6(self):  
#         """unsubscribe the topic that is not subscribed"""
#         try:
#             print("run helper...")
#             code = str(51)
#             args = ['python', 'helper.py', code]
#             p = subprocess.Popen(args, cwd=(helper_dir))
#             time.sleep(connect_worst_timeout)

#             self.anotherTopic = "/secondTopic"
            
#             client.create(self.gearkey, self.gearsecret, self.appid)
           
#             client.on_connect = MagicMock()
#             client.on_message = MagicMock()
          
#             client.connect()
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_connect.called)
#             self.connected = True
#             self.assertEqual(client.on_connect.call_count, 1)
#             self.assertFalse(client.on_message.called)
#             client.subscribe(self.topic)
#             time.sleep(message_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#             client.on_message.reset_mock()
#             self.assertFalse(client.on_message.called)

#             client.unsubscribe(self.anotherTopic)
#             time.sleep(connect_timeout)
#             self.assertTrue(client.on_message.called)
#             client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#             p.kill()
#         except Exception as e:
#             p.kill()
#             raise Exception(e.args) 


def main():
    #suite = unittest.TestSuite()
    #suite.addTest(TestChat("testCode4Case2"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    print(os.path.join(os.getcwd(),"microgear.cache"))    
    unittest.main()

if __name__ == '__main__':
    main()    