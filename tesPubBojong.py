import paho.mqtt.client as mqtt

import time

import random

broker_address = "localhost"

Client = mqtt.Client("Laundry Bojong")

Client.connect(broker_address, port = 3333)

takeBaju = random.randint(1, 3)
sendBaju = random.randint(24, 72)
totalWaktuLaundry = takeBaju + sendBaju

inputs = ""

while inputs.lower() != "y":
    Client.loop_start()
    Client.publish("bojong", "Selamat datang di laundry bojong")
    Client.publish("bojong", f"Estimasi penjemputan baju kotor selama {takeBaju} jam")
    Client.publish("bojong", f"Estimasi pengiriman baju hasil laundry selama {sendBaju} jam")
    Client.publish("bojong", f"Total waktu baju hasil laundry selama {totalWaktuLaundry} jam")
    print("Apakah sudah semua? (Y/n)", end= " ")
    inputs = input()
    Client.loop_stop()
    