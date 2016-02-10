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

    def testCode4Case1(self):
        """chat with itself"""   
        print('Code4Case1')
       
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
        try:
            print('Code4Case2')  
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
            if(received_message == self.message):
                self.received = True
            self.assertTrue(self.received)
            p.kill()
        #if fails due to assertion error
        except Exception as e:
            print("fail")
            raise Exception(e.args)
            

    #helper 11
    def testCode4Case3(self):
        """chat with other microgear in different appid"""   
        try:
            print('Code4Case3')
  
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
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()

        #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)
            
        
    #helper 33
    def testCode4Case5(self):
        """chat to microgear which shares the same name as itself"""   
        try:
            print('Code4Case5')
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
            if(received_message == self.message):
                self.received = True

            self.assertTrue(self.received)
            p.kill()
        #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 12
    def testCode4Case6(self):
        """chat with other microgear which shares the same gearname in different appid"""
        try:
            print('Code4Case6')
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
            if(received_message == self.message):
                self.received = True
                
            self.assertFalse(self.received)
            p.kill()
                    #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 32
    def testCode4Case8(self):
        """chat to microgear which has gearname similar to topic"""
        try:  
            print('Code4Case8')
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
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()
                #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)


    #helper 34
    def testCode4Case9(self):
        """chat with other microgear which has empty string as gearname"""
        try:
            print('Code4Case9')
             
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
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()
                        #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)

    #helper 61
    def testCode4Case10(self):
        """chat to topic which has subscriber"""
        try:   
            print('Code4Case10')
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
            if(received_message == self.message):
                self.received = True
            self.assertFalse(self.received)
            p.kill()
                            #if fails due to assertion error
        except Exception as e:
            p.kill()
            raise Exception(e.args)




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
            if(received_message == self.expectedMessage):
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
            if(received_message == self.expectedMessage):
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
            if(received_message == self.expectedMessage):
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
            if(received_message == self.expectedMessage):
                self.received = True
            self.assertFalse(self.received)
            self.assertTrue(client.on_connect.call_count > 1)
            p.kill()
        except Exception as e:
            p.kill()
            raise Exception(e.args) 

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
   

    def testCode8Case2(self):  
        """resettoken when have microgear.cache while microgear is offline"""
        #pre-requisite: ensure there is microgear.cache
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

        self.assertIsNone(microgear.gearkey)
        self.assertIsNone(microgear.gearsecret)    
        self.assertIsNone(microgear.appid)
        
        client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': True})
       
        client.on_connect = MagicMock()

        #resettoken when have microgear.cache
        client.resettoken()
        time.sleep(4)
        #should delete microgear.cache
        self.assertFalse(os.path.isfile(os.path.join(os.getcwd()+"/microgear.cache")))

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

        #should not affect connect
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