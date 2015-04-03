import time, serial, mosquitto #imports functions needed to work, allows us to send and receive data

def messageReceived(broker, obj, msg):
    global ser                          #allows serial to be used globally
    print("Message " + msg.topic " containing: " + msg.payload) #prints the message it has received
    if msg.payload =='ON': ser.write("1") #if it gets the right message the light will turn on
    else : ser.write("0") #if not the light stays off


client = mosquitto.Mosquitto("phamilton01") #unique user id
client.connect("") #the clients IP address
client.subscribe("lights") #the thing we're listening to
client.on_message = messageReceived

ser = serial.Serial("/dev/cu.usbmodem14611",9600,timeout=2)

while True: client.loop()
