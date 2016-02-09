import microgear
import microgear.client as client
import time
import sys
import os
import os.path



if(os.path.isfile(os.path.join(os.getcwd(),"microgear.cache"))):
    cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "w")
    print(cache_file)
    cache_file.write("")
    cache_file.close()  
    time.sleep(6)


def helper(createx=[], setaliasx=[], chatx=[], publishx=[], subscribex=[]):
    print(createx, setaliasx,chatx,publishx,subscribex)

    message = "hello"
    received = False
    if(len(createx) > 0):
        print(microgear.gearkey)
        client.create(createx[0],createx[1],createx[2],{'debugmode': True}) 

    def on_connected():
        print("connect")      
    def on_disconnected():
        print("disconnected") 
    def on_message(topic, message):
        print("message")
        time.sleep(2)
        ack = open(os.path.join(os.getcwd(),"../receiver.txt"), "w")
        print(ack)
        ack.write(message)
        ack.close()
       
    def on_present(gearkey):
        print("present")
    def on_absent(gearkey):
        print("absent")         
    def on_warning(msg):
        print("reject") 
    def on_info(msg):
        print("info")     
    def on_error(msg):
        print("error")  
    
    
    client.on_connect = on_connected
    client.on_disconnect = on_disconnected
    client.on_message = on_message 
    client.on_present = on_present
    client.on_absent = on_absent
    client.on_warning = on_warning
    client.on_info = on_info
    client.on_error = on_error

    if(len(setaliasx) > 0):
        client.setalias(setaliasx[0])
    if(len(subscribex) > 0): 
        client.subscribe(subscribex[0])

    client.resettoken()
    client.connect(False)
    
    if(len(chatx) > 0):
        while True:
            client.chat(chatx[0], message)
            print('chitchat')
            time.sleep(2)

    if(len(publishx) > 0) :
        while True:
            client.publish(publishx[0], message)
            print('pubpush')
            time.sleep(2)
    print("in helper file")
    print(os.path.join(os.getcwd(),"microgear.cache"))
    
    while True:
        pass


def code(x):
    gearkey = "yMPSuoFBV6Ao322"
    gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
    appid = "testPython"
    gearkey2 = "3z7DhYHB6XuC4EZ"
    gearsecret2 = "P6DdCpQVttgKN0F1Pc7yvUWWJkMOaf"
    appid2 = "testPythonHelper"    

    gearname = "mainPython"
    helperGearname = "helper"
    topic = "/firstTopic"
    emptyStr = ""
    invalidTopic = "firstTopic"

    if(x == 11):
    #create in different appkey and setalias to helperGearname
        helper(createx=[gearkey2, gearsecret2, appid2], setaliasx=[helperGearname])
    if(x == 12):
    #create in different appkey and setalias to gearname
        helper(createx=[gearkey2, gearsecret2, appid2], setaliasx=[gearname])
    #create in same appkey and setalias to helperGearname
    elif(x == 31):
        helper(createx=[gearkey, gearsecret, appid], setaliasx=[helperGearname])
    #create in same appkey and setalias to topic name
    elif(x == 32):
        helper(createx=[gearkey, gearsecret, appid], setaliasx=[topic])
    #create in same appkey and setalias to gearname
    elif(x == 33):
        helper(createx=[gearkey, gearsecret, appid], setaliasx=[gearname])
        #create in same appkey and setalias to empty str
    elif(x == 34):
        helper(createx=[gearkey, gearsecret, appid], setaliasx=[emptyStr])
    #create in same appkey and chat to gearname
    elif(x == 4):
        helper(createx=[gearkey, gearsecret, appid], chatx=[gearname])

    #create in same appkey and publish topic
    elif(x == 51):
        helper(createx=[gearkey, gearsecret, appid], publishx=[topic])

    #create in same appkey and publish to empty topic
    elif(x == 52):
        helper(createx=[gearkey, gearsecret, appid], publishx=[emptyStr])
        #create in same appkey and publish to invalid topic - no slash
    elif(x == 53):
        helper(createx=[gearkey, gearsecret, appid], publishx=[invalidTopic])
    #create in same appkey and subscribe to topic
    elif(x == 61):
        helper(createx=[gearkey, gearsecret, appid], subscribex=[topic])
    #create in same appkey and subscribe invalid topic - no slash
    elif(x == 63):
        helper(createx=[gearkey, gearsecret, appid], subscribex=[invalidTopic])


print(sys.argv)
code(int(sys.argv[1]))
# x = int(sys.argv[1])


