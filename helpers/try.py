import microgear.client as client
import time
import os

# if not (os.path.isfile(os.path.join(os.getcwd(),"microgear.cache"))):
#     cache_file = open(os.path.join(os.getcwd(),"microgear.cache"), "w")
#     print(cache_file)
#     cache_file.write("")
#     cache_file.close()  


gearkey = "yMPSuoFBV6Ao322"
gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
appid = "testPython"

# gearkey = "EDosiaMiPZMhK7M"
# gearsecret = "7Od2AxYdq0hPDBImyAqCJCH9fdsdAG"
# appid = "testPythonHelper" 
client.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    print("Now I am connected with netpie")

def subscription(topic,message):
    print(topic+" "+message)
    # client.publish("mainPython","Hey guy."+str(int(time.time())))

# client.setalias("doraemon2")
client.on_connect = connection
client.on_message = subscription
# client.subscribe("/firstTopic")
print('resettoken')
client.resettoken()
client.resettoken()
time.sleep(3)
client.connect(False)
# while(True):
#     client.chat("firstTopic","Hello world.")
#     print("pub")
#     time.sleep(3)
#     #need delay
print("end")
#os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
#print(os.path.join(os.getcwd()))
#cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "r").read()
#print(cache_file)
#cache_file.write("")
#cache_file.close()