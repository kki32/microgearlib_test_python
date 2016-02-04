












#class TestCreate(unittest.TestCase):
    #def setUp(self):
        #self.gearkey = "yMPSuoFBV6Ao322"
        #self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        #self.appid = "testPython"
        
    #def tearDown(self):
        #fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        #print("Name ", fo)
        #fo.close()         
        #print("done")

    
        ##def testConnectWithValidInput(self):
            ##client.on_connect = MagicMock()
            ##self.connected = False
            ##def on_connected():
                ##self.connected = True
            ##client.on_connect = on_connected
            ##client.create(self.gearkey, self.gearsecret, self.appid, {'debugmode': "True"})   
            ##client.connect()
            ##timeout = time.time() + 30.0
            ##if(time.time() > timeout or self.connected):
                ##self.assertTrue(self.connected)
 
    #@unittest.skip("") 
    #def testCode1Case1(self):   
        #"""create microgear with valid gearkey, gearsecret, and appid"""   
        #self.assertIsNone(microgear.gearkey)
        #self.assertIsNone(microgear.gearsecret)    
        #self.assertIsNone(microgear.appid)
        
        #client.create(self.gearkey, self.gearsecret, self.appid)
        #self.assertEqual(self.gearkey, microgear.gearkey)
        #self.assertEqual(self.gearsecret, microgear.gearsecret)
        #self.assertEqual(self.appid, microgear.appid)
        
        #client.on_connect = MagicMock()
        #client.connect()
        #time.sleep(5)
        #self.assertTrue(client.on_connect.called)
        #self.assertEqual(client.on_connect.call_count, 1)   
        
    #@unittest.skip("")
    #def testCode1Case2(self):
        #"""create microgear with invalid gearkey"""   
        #self.assertIsNone(microgear.gearkey)
        #self.assertIsNone(microgear.gearsecret)    
        #self.assertIsNone(microgear.appid)
        #self.gearkey = ""
        #client.create(self.gearkey, self.gearsecret, self.appid)
        
        #self.assertEqual(self.gearkey, microgear.gearkey)
        #self.assertEqual(self.gearsecret, microgear.gearsecret)
        #self.assertEqual(self.appid, microgear.appid)
        
        #client.on_connect = MagicMock()
        #client.on_error = MagicMock()
        #self.assertFalse(client.on_connect.called)
        #client.connect()
        #time.sleep(5)
        #self.assertFalse(client.on_connect.called)
        #self.assertTrue(client.on_error.called)   
        
    
    
    ##@unittest.skip("")
    #def testCode1Case3(self):
        #"""create microgear with invalid gearsecret"""  
        #self.assertIsNone(microgear.gearkey)
        #self.assertIsNone(microgear.gearsecret)    
        #self.assertIsNone(microgear.appid)
        #self.gearsecret = ""
        #client.create(self.gearkey, self.gearsecret, self.appid)
        
        #self.assertEqual(self.gearkey, microgear.gearkey)
        #self.assertEqual(self.gearsecret, microgear.gearsecret)
        #self.assertEqual(self.appid, microgear.appid)
        
        #client.on_connect = MagicMock()
        #client.on_error = MagicMock()
        #self.assertFalse(client.on_connect.called)
        #client.connect()
        #time.sleep(connect_timeout)
        #self.assertFalse(client.on_connect.called)
        #self.assertTrue(client.on_error.called)   
 





class TestConnect(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello"        
        
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")



class TestSetalias(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello"        
        
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")



class TestPublish(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello" 
        self.topic = '/firstTopic'
        
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")

    @unittest.skip("") 
    def testCode1Case1(self): 
        #write file TODO
        receiver_file = open(os.path.join(os.getcwd(),"receiver.txt"), "w")
        
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
        #watch file
class TestSubscribe(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello"        
        self.topic = '/firstTopic'
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")
        
    def testCode4Case1(self):   
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
        #check if equal
        
class TestUnsubscribe(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello"        
        
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")
    def testCode4Case1(self):   
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
        client.on_message.reset()
        time.sleep(message_timeout)
        self.assertFalse(client.on_message.called)
        
        #check if equal
        

class TestResettoken(unittest.TestCase):
    def setUp(self):
        self.gearkey = "yMPSuoFBV6Ao322"
        self.gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
        self.appid = "testPython"
        self.gearname = "mainPython"
        self.message = "hello"        
        
    def tearDown(self):
        fo = open(os.path.join(os.getcwd(),"microgear.cache"), "rb")
        print("Name ", fo)
        fo.close()         
        print("done")
