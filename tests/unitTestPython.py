#!/usr/bin/env python
#export PYTHONWARNINGS="ignore"
#TODO: resettoken should return null for microgear
#todo: if fail, need to find way to kill process
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
connect_worst_timeout = 30
helper_dir = os.path.join(os.getcwd()) + '/helpers'


receiver_file = os.path.join(os.getcwd(),"receiver.txt")

class TestChat(unittest.TestCase):
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
         

    def tearDown(self):
    #delete receive txt
        print('tearDown')
   
        os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
        if(self.connected):
            microgear.mqtt_client.disconnect()

    def testCode4Case1(self):
        """chat with itself"""   

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)
        client.on_message = MagicMock()
        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True
        client.chat(self.gearname, self.message)
        time.sleep(message_timeout)
        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_once_with(self.expectedMsgTopic, self.expectedMessage)
        

          #require helper 31
    def testCode4Case2(self):
        """chat with other microgear in same appid"""  
        print("run helper...")
        code = str(31)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)

        self.assertTrue(client.on_connect.called)
        self.connected = True
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        r_file = open(receiver_file, "r")
        received_message = r_file.read()
        r_file.close()        
        if(received_message == self.expectedMessage):
            self.received = True

        self.assertTrue(self.received)

        p.kill()

        #helper 11
    def testCode4Case3(self):
        """chat with other microgear in different appid"""   
  
        print("run helper...")
        code = str(11)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
        p.kill()
        
    #helper 33
    def testCode4Case5(self):
        """chat to microgear which shares the same name as itself"""   
        time.sleep(15)
        print("run helper...")
        code = str(33)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")
        self.helperGearname = self.gearname

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.on_message = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        self.assertTrue(client.on_message.called)
        client.on_message.assert_called_once_with(self.expectedMsgTopic, self.expectedMessage)
        
        r_file = open(receiver_file, "r")
        received_message = r_file.read()
        r_file.close()
        if(received_message == self.expectedMessage):
            self.received = True

        self.assertTrue(self.received)
    
        p.kill()

    #helper 12
    def testCode4Case6(self):
        """chat with other microgear which shares the same gearname in different appid"""

        print("run helper...")
        code = str(12)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)   

        print("run main...")
        self.helperGearname = self.gearname

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.on_message = MagicMock()
        
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True
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
        p.kill()

        #helper 32
    def testCode4Case8(self):
        """chat to microgear which has gearname similar to topic"""   

        print("run helper...")
        code = str(32)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")
        self.gearname = '/firstTopic'

        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
        p.kill()


    #helper 34
    def testCode4Case9(self):
        """chat with other microgear which has empty string as gearname"""

        time.sleep(15)
        print("run helper...")
        code = str(34)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")
        self.helperGearname = ""
    
        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)
    
        client.on_connect = MagicMock()
    
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True
        print(self.helperGearname, "empty")
        
        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
        p.kill()

    #helper 61
    def testCode4Case10(self):
        """chat to topic which has subscriber"""   
        time.sleep(15)
        print("run helper...")
        code = str(61)
        args = ['python', 'helper.py', code]
        p = subprocess.Popen(args, cwd=(helper_dir))
        time.sleep(connect_worst_timeout)

        print("run main...")
        self.gearname = '/firstTopic'


        client.create(self.gearkey, self.gearsecret, self.appid)
        client.setalias(self.gearname)

        client.on_connect = MagicMock()
        client.connect()
        time.sleep(connect_timeout)
        self.assertTrue(client.on_connect.called)
        self.connected = True

        client.chat(self.helperGearname, self.message)
        time.sleep(message_timeout)

        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "r")
        received_message = receiver_file.read()
        receiver_file.close()
        if(received_message == self.expectedMessage):
            self.received = True
        self.assertFalse(self.received)
        p.kill()


# class TestSubscribe(unittest.TestCase):
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
         

#     def tearDown(self):
#     #delete receive txt
#         print('tearDown')
   
#         os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
#         if(self.connected):
#             microgear.mqtt_client.disconnect()

#     #helper 51
#     def testCode5Case1(self):   
#         """subscribe one topic"""
#         print("run helper...")
#         code = str(51)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)

#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)   

#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#         p.kill()

#     #helper 51
#     def testCode5Case2(self):   
#         """subscribe same topic twice"""

#         print("run helper...")
#         code = str(51)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)

#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
#         client.subscribe(self.topic)
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)   

#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)
#         p.kill()
#     #helper 51
#     def testCode5Case3(self):   
#         """subscribe same topic twice"""
#         print("run helper...")
#         code = str(51)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)
        
#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
   
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         connected = True
#         self.assertEqual(client.on_connect.call_count, 1)

#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#         #unsubscribe after receive message
#         client.unsubscribe(self.topic)
#         client.on_message.reset_mock() #reset count recorded by mock
#         self.assertFalse(client.on_message.called)
#         time.sleep(message_timeout)
#         self.assertFalse(client.on_message.called) #should not receive message now
#         client.subscribe(self.topic) #subscribe again
#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called) #should receive message
#         p.kill()

#     def testCode5Case4(self):   
#         """subscribe the topic that it publishes"""
        
#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
   
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)

#         client.publish(self.topic, self.message)
#         time.sleep(message_timeout)
#         self.assertTrue(client.on_message.called)
#         client.on_message.assert_called_with(self.expectedTopic, self.expectedMessage)

#     #helper 51
#     def testCode5Case5x1(self):   
#         """subscribe empty topic"""

#         print("run helper...")
#         code = str(31)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)
#         self.topic = ""

        
#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
   
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)
#         time.sleep(message_timeout)
#         self.assertFalse(client.on_message.called)
#         p.kill()
#     #fail
#     #helper 52
#     # def testCode5Case5x2(self):   
#     #     """subscribe empty topic"""
#     #     self.topic = ""
#     #     client.create(self.gearkey, self.gearsecret, self.appid)
#     #     client.subscribe(self.topic)
   
#     #     client.on_connect = MagicMock()
#     #     client.on_message = MagicMock()
       
#     #     client.connect()
#     #     time.sleep(connect_timeout)
#     #     self.assertTrue(client.on_connect.called)
#     #     self.assertEqual(client.on_connect.call_count, 1)
#     #     time.sleep(message_timeout)
#     #     self.assertFalse(client.on_message.called)

#     #helper 51 should publish topic
#     def testCode5Case6x1(self):   
#         """subscribe invalid topic - no slash"""

#         print("run helper...")
#         code = str(51)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)
#         self.topic = "firstTopic"
        
#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
   
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)
#         time.sleep(message_timeout)
#         self.assertFalse(client.on_message.called)
#     #helper 53 should publish invalid topic
#     def testCode5Case6x2(self):   
#         """subscribe invalid topic - no slash"""
#         print("run helper...")
#         code = str(53)
#         args = ['python', 'helper.py', code]
#         p = subprocess.Popen(args, cwd=(helper_dir))
#         time.sleep(connect_worst_timeout)

#         self.topic = "firstTopic"

#         client.create(self.gearkey, self.gearsecret, self.appid)
#         client.subscribe(self.topic)
   
#         client.on_connect = MagicMock()
#         client.on_message = MagicMock()
       
#         client.connect()
#         time.sleep(connect_timeout)
#         self.assertTrue(client.on_connect.called)
#         self.connected = True
#         self.assertEqual(client.on_connect.call_count, 1)
#         time.sleep(message_timeout)
#         self.assertFalse(client.on_message.called)  
#         p.kill()


def main():
    #suite = unittest.TestSuite()
    #suite.addTest(TestChat("testCode4Case2"))
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    print(os.path.join(os.getcwd(),"microgear.cache"))    
    unittest.main()

if __name__ == '__main__':
    main()    