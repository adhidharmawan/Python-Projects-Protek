#program menghitung waktu sampai

jrk1 = int(input("jarak1 = "))
jrk2 = int(input("jarak2 = "))

kcpt1 = int(input("kecepatan1 = "))
kcpt2 = int(input("kecepatan2 = "))

berangkat1 = int(input("berangkat(jam) = "))
berangkat2 = int(input("berangkat(menit) = "))

istirahat1 = int(input("istirahat(jam) = "))
istirahat2 = int(input("istirahat(menit) = "))

import math

jam1 = round(jrk1/kcpt1)
jam2 = round(jrk2/kcpt2)

print("waktu sampai pak amir=", (berangkat2 + berangkat1 + istirahat1 + istirahat2/100 + jam1 + jam2))