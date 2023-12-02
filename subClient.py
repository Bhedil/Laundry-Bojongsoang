# gunakan library paho mqtt
import paho.mqtt.client as mqtt
# library untuk sleep
import time

import random

# callback: fungsi yang akan dipanggil jika message di buffer
############
def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

# Inisialisasi broker
broker_bojong="192.168.92.217"
broker_soang="192.168.92.105"
# buat client bernama P1
print("creating new instance")
client = mqtt.Client("Client 1")
# pada client dikaitkan callback function
client.on_message=on_message

tombolSubs = ""

waktuLaundryB = random.randint(24, 72)
waktuLaundryS = random.randint(24, 72)

while tombolSubs != "exit":
    print('''
    Selamat datang di aplikasi laundry
        Mau cuci laundry dimana?
    1. Laundry Bojong
    2. Laundry Soang
    3. Tampilkan informasi
    ketik 'exit' untuk keluar
    Masukkan input: ''', end = "")

    tombolSubs = input()
    if tombolSubs == "1":
        client.connect(broker_bojong, port=1883)
        client.loop_start()
        client.subscribe("bojong")
        time.sleep(7)
    elif tombolSubs == "2":
        client.connect(broker_soang, port=1883)
        client.loop_start()
        client.subscribe("soang")
        time.sleep(7)
    elif tombolSubs == "3":
        print(f'\nWaktu laundry bojong memakan waktu selama {waktuLaundryB} jam ')
        print(f'Waktu laundry soang memakan waktu selama {waktuLaundryS} jam')
    else:
        print("input Salah")
    time.sleep(7)
    client.loop_stop()