#program menetukan gaji seseorang

kode=input("Masuka kode karyawan        : ")
nama=input("Masukan nama karyawan       : ")
gol=input("Masukan golongan(A,B,C,D)   : ")
print("Status :\n\t1:Menikah \n\t2:Belum menikah")
status=input("Masukan Status              : ")
if status == "1":
     anak = input("Masukan jumlah anak         : ")
if status == "2":
     anak = '0'

if (gol =='A'):
     gajipokok = 10000000
     persen = 2.5
     tunistrisuami = gajipokok * 10/100
     tunanak = gajipokok * 5/100 * float(anak)
     pot = gajipokok * persen/100
     gajikotor = gajipokok + tunistrisuami + tunanak
     gajibersih = gajikotor - pot
elif(gol =='B'):
     gajipokok = 8500000
     persen = 2.0
     tunistrisuami = gajipokok * 10/100
     tunanak = gajipokok * 5/100 * float(anak)
     pot = gajipokok * persen/100
     gajikotor = gajipokok + tunistrisuami + tunanak
     gajibersih = gajikotor - pot
elif(gol =='C'):
     gajipokok = 6000000
     persen = 1.5
     tunistrisuami = gajipokok * 10/100
     tunanak = gajipokok * 5/100 * float(anak)
     pot = gajipokok * persen/100
     gajikotor = gajipokok + tunistrisuami + tunanak
     gajibersih = gajikotor - pot
elif(gol =='D'):
     gajipokok = 5000000
     persen = 1.0
     tunistrisuami = gajipokok * 10/100
     tunanak = gajipokok * 5/100 * float(anak)
     pot = gajipokok * persen/100
     gajikotor = gajipokok + tunistrisuami + tunanak
     gajibersih = gajikotor - pot

print("\n=======================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------------")
print("Nama Karyawan          : "+nama, "(Kode:"+kode+")")
print("Golongan               : "+gol)
print("Status Menikah         : "+status)
print("Jumlah Anak            : "+anak)
print("---------------------------------------")   
print("Gaji Pokok             :Rp ",gajipokok)
print("Tunjangan Istri/Suami  :Rp ",tunistrisuami)
print("Tunjangan anak         :Rp ",tunanak)
print("--------------------------------------- +")
print("Gaji Kotor             :Rp ",gajikotor)
print("Potongan(",(persen),")        :Rp ",pot)
print("--------------------------------------- -")
print("Gaji Bersih            :Rp ",gajibersih)
