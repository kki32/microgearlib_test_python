import microgear.client as client
import time

def testChat():
    gearkey = "ExhoyeQoTyJS5Ac"
    gearsecret = "gzDawaaHRe1KvQhepAw3WYuuGHjBsh"
    appid = "p107microgear"

    gear_name = "not receiver"

    client.create(gearkey , gearsecret, appid, {'debugmode': True})
    client.setname(gear_name)
    client.connect()

    def receive_message(topic, message):
        print topic + " " + message

    while True:
        client.chat("not receiver", "hello")
        time.sleep(3)
        client.on_message = receive_message

testChat()