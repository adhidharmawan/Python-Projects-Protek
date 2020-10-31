#program menentutakan status kelulusan ujian

bindo   = int(input("Masukan nilai Bahasa Indonesia : "))
ipa     = int(input("Masukan nilai IPA              : "))
mtk     = int(input("Masukan nilai Matematika       : "))


if (bindo >= 60 and bindo <= 100) and (ipa >= 60 and ipa <= 100) and (mtk > 70 and mtk <= 100):
    print("Status Kelulusan               : LULUS ")
elif (bindo > 0 and bindo < 60) and (ipa > 0 and ipa < 60) and (mtk > 0 and mtk <=70):
    print("Status Kelulusan               : TIDAK LULUS ")
elif (bindo < 0 or bindo > 100) and (ipa < 0 or ipa > 100) and (mtk < 0 or mtk > 100):
    print("Maaf input ada yang tidak valid")
elif (bindo < 0 or bindo > 100) or (ipa < 0 or ipa > 100) or (mtk < 0 or mtk > 100):
    print("Maaf input ada yang tidak valid")
elif (bindo > 0 and bindo < 60) or (ipa > 0 and ipa < 60) or (mtk > 0 and mtk <=70):
    print("Status Kelulusan               : TIDAK LULUS ")
