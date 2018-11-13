import urequests
import ujson
import time
import machine

global size
size=0

sub = 'http://pubsub.pubnub.com/subscribe/sub-c-0fe02006-4dfd-11e8-9c03-eafb26272eb6/"Your-channel-name"/0/0'
m1c = machine.Pin(0, machine.Pin.OUT)
m1a = machine.Pin(2, machine.Pin.OUT)

m2c = machine.Pin(13, machine.Pin.OUT)
m2a = machine.Pin(15, machine.Pin.OUT)

def func(cmd):
    print(cmd)
    if(cmd=='Letter C'):
        print("moving forward...")
        m1c.on()
        m2c.on()
        time.sleep(1)
        m1c.off()
        m2c.off()
    elif(cmd=='Letter O'):
        print("moving Left...")
        m1a.on()
        # m2a.on()
        time.sleep(1)
        m1a.off()
        # m2a.off()
    elif(cmd=='Number 3'):
        print("moving Right...")
        # m1a.on()
        m2a.on()
        time.sleep(1)
        # m1a.off()
        m2a.off()



while True:
    print("listening...")
    #Subscribe request (initial)
    subscribe = urequests.get(sub)
    #Subscribe request into variable
    read = urequests.get('http://pubsub.pubnub.com/subscribe/sub-c-0fe02006-4dfd-11e8-9c03-eafb26272eb6/"Your-channel-name"/0/' + str(subscribe.content[1])+str('?'))
    #Jsonify data into an object
    jData = ujson.loads(read.content)
    # print(jData)
    s=len(jData[0])
    if(s>size):
        size=s
        command = jData[0][size-1]
        func(command)
    else:
        print("no new msg")
    time.sleep(0.5)
