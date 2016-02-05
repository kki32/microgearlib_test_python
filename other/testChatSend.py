import microgear.client as client
import time

def testChat():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"

    origin = "oriA"
    destination = "destX"
    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname(origin)
    client.connect()

    def receive_message(topic, message):
        print topic + " " + message

    while True:
        client.chat(destination,"Hello world.")
        time.sleep(3)
testChat()