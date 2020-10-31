# program game tebak angka

import random
# komputer memilih angka secara acak dari 1 s.d 100
angka = random.randint(1,100)
#atur score
maksimum_score = 100

print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
print(" ")
while angka:
    maksimum_score = maksimum_score - 2
    tebakan = int(input("Masukan tebakan anda : "))
    if tebakan == angka:
        print("Yeeee… Bilangan tebakan anda BENAR :-)")
    if tebakan > angka:
        print("Hehehe… Bilangan tebakan anda terlalu besar")
    if tebakan < angka:
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
    if tebakan == angka :
        break
print("")
print("Score Anda: ", maksimum_score)
