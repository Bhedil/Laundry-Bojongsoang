# gunakan library paho mqtt
import paho.mqtt.client as mqtt
# library untuk sleep
import time

#Library untuk generator angka secara acak
import random

# alamat broker yang akan digunakan
broker_address="192.168.213.217"
# buat client bernama P1
print("creating new instance")
client = mqtt.Client("Laundry Bojong")
# client terkoneksi dengan broker
print("connecting to broker")
client.connect(broker_address, port = 1883)

#Pake module randInt untuk angka random sampai kurang dari sama dengan
jemputBaju = random.randint(1, 3)
sendBaju = random.randint(24, 72)
totalBaju = jemputBaju + sendBaju

client.loop_start()
# client P1 publish ke broker dengan topik "house/bulbs/bulb1"
# P1 -> broker
inputs = ""

while inputs.lower() != "y":
    time.sleep(10)
    client.publish("bojong", "selamat datang di laundry bojong")
    client.publish("bojong", f"Estimasi waktu penjemputan baju kotor selama {jemputBaju} jam")
    client.publish("bojong", f"Estimasi waktu pengiriman baju hasil laundry selama {sendBaju} jam")
    client.publish("bojong", f"Total waktu baju hasil laundry selama {totalBaju} jam")
    print("Apakah sudah semua? (Y/n) ", end= " ")
    inputs = input()