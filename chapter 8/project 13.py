def tertinggi(data):
    tinggi = 0
    dictionary = {}
    for i in data:
        uas = i['uas']
        mid = i['mid']
        akhir = (mid + 2*uas)/3
        if akhir > tinggi:
            tinggi = akhir
            dictionary['nim'] = i['nim']
            dictionary['nama'] = i['nama']
    print('Mahasiswa memiliki nilai akhir tertinggi')
    print('Nama :',dictionary['nama'])
    print('NIM  :',dictionary['nim'])

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
tertinggi(nilaiMhs)
