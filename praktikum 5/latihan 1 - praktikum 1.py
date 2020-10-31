#program menentutakan status kelulusan ujian

bindo   = int(input("Masukan nilai Bahasa Indonesia : "))
ipa     = int(input("Masukan nilai IPA              : "))
mtk     = int(input("Masukan nilai Matematika       : "))

if (bindo >= 60 and bindo <= 100) and (ipa >= 60 and ipa <= 100) and (mtk > 70 and mtk <= 100):
    print("Status Kelulusan               : LULUS ")
else:
    print("Status Kelulusan               : TIDAK LULUS ")
