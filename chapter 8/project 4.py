sayur = ['bayam','kangkung','wortel','selada']
def data():
    try:

        if menu == 'A':
            tambah = input('Masukan nama sayur yang ingin ditambah: ')
            sayur.append(tambah)
            print('daftar sayur: ',sayur)

        if menu == 'B':
            hapus = input('Nama sayur yang ingin dihapus: ')
            sayur.remove(hapus)
            print('daftar sayur: ',sayur)
    
        if menu == 'C':
             print('daftar sayur: ',sayur)
        
    except ValueError:
        print('Nama sayur tersebut tidak terdaftar')

print('Menu:')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
menu = input('Pilih (A/B/C):')
data()
