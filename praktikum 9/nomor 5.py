nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*45)
print('NIM'.ljust(10), 'NAMA'.ljust(15), 'N.MID'.ljust(10), 'N.UAS')
print('-'*45)
for i in nilai:
    print(i['nim'].ljust(10), i['nama'].ljust(15), str(i['mid']).ljust(10), str(i['uas']))
print('='*45)
