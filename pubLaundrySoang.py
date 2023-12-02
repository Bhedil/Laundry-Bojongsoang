# gunakan library paho mqtt
import paho.mqtt.client as mqtt
# library untuk sleep
import time

#Library untuk generator angka secara acak
import random

# alamat broker yang akan digunakan
broker_address="192.168.92.105"
# buat client bernama P1
print("creating new instance")
client = mqtt.Client("Laundry Soang")
# client terkoneksi dengan broker
print("connecting to broker")
client.connect(broker_address, port=1883
)

#Pake module randInt untuk angka random sampai kurang dari sama dengan
jemputBaju = random.randint(1, 3)
sendBaju = random.randint(24, 72)
totalBaju = jemputBaju + sendBaju

client.loop_start()
# client P1 publish ke broker dengan topik "soang"
# P1 -> broker
inputs = ""

while inputs != "exit":
    time.sleep(10)
    client.publish("soang", "\nSelamat datang di laundry Soang")
    client.publish("soang", f"Estimasi penjemputan baju kotor selama {jemputBaju} jam")
    client.publish("soang", f"Estimasi pengiriman baju hasil laundry selama {sendBaju} jam")
    client.publish("soang", f"Total waktu proses laundry Soang ialah {totalBaju} jam")
    client.loop_stop()
    print("Apakah sudah semua? {Y/n) ", end = "")
    inputs = input()
    if inputs.lower() == "y":
        inputs = "exit"