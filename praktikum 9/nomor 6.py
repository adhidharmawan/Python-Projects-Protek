nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*67)
print('NIM'.ljust(10), 'NAMA'.ljust(15), 'N.MID'.ljust(10), 'N.UAS'.ljust(10), 'N.AKHIR'.ljust(10), 'STATUS')
print('-'*67)
for i in nilai:
    na = (i['mid'] +2*i['uas'])/3
    membulat = round(na)
    if na >= 60:
        status = 'LULUS'
    if na < 60:
        status = 'TIDAK LULUS'
    print(i['nim'].ljust(10), i['nama'].ljust(15), str(i['mid']).ljust(10), str(i['uas']).ljust(10), str(membulat).ljust(10), status)
print('='*67)
