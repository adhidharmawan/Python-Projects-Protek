#program menetukan gaji seseorang

kode=input("Masuka kode karyawan        : ")
nama=input("Masukan nama karyawan       : ")
gol=input("Masukan golongan(A,B,C,D)   : ")
if (gol =='A'):
     gajipokok = 10000000
     persen = 2.5
     pot = gajipokok * persen/100
     gajibersih = gajipokok - pot
elif(gol =='B'):
     gajipokok = 8500000
     persen = 2.0
     pot = gajipokok * persen/100
     gajibersih = gajipokok - pot
elif(gol =='C'):
     gajipokok = 6000000
     persen = 1.5
     pot = gajipokok * persen/100
     gajibersih = gajipokok - pot
elif(gol =='D'):
     gajipokok = 5000000
     persen = 1.0
     pot = gajipokok * persen/100
     gajibersih = gajipokok - pot

print("\n=======================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------")
print("Nama Karyawan    : "+nama, "(Kode:"+kode+")")
print("Golongan         : "+gol)
print("---------------------------------------")   
print("Gaji Pokok       :Rp ",gajipokok)
print("Potongan(",(persen),")  :Rp ",pot)
print("--------------------------------------- -")
print("Gaji Bersih      :Rp ",gajibersih)
