import microgear.client as client
import time
import os


gearkey = "yMPSuoFBV6Ao322"
gearsecret = "0LoUk4hHStPMzOg5TczeSps3L0XRcE"
appid = "testPython"

if(os.path.isfile(os.path.join(os.getcwd(),"microgear.cache"))):
    cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "w")
    print(cache_file)
    cache_file.write("")
    cache_file.close()  
    time.sleep(6)

client.create(gearkey,gearsecret,appid,{'debugmode': True})

def connection():
    print("Now I am connected with netpie")

def subscription(topic,message):
    print(topic+" "+message)
    client.unsubscribe("/secondTopic")
    # client.chat("mainPython","Hey guy."+str(int(time.time())))
   

# client.setalias("doraemon2")
client.subscribe("/firstTopic")


print("shoud")
client.on_connect = connection
client.on_message = subscription
# client.subscribe("/mails")
# client.subscribe("/firstTopic")
client.connect(False)

#client.chat("","Hello world."+str(int(time.time())))
    #need delay
while(True):
	pass
print("end")
#os.remove(os.path.join(os.getcwd()+"/receiver.txt"))
#print(os.path.join(os.getcwd()))
#cache_file = open(os.path.join(os.getcwd()+"/microgear.cache"), "r").read()
#print(cache_file)
#cache_file.write("")
#cache_file.close()