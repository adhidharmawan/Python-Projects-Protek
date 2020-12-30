makskey= 26

def sandi():
    kata = input('Masukan Sandi Caesar: ')
    return kata

def keysandi():
    key = 0
    while True:
        key = int(input('Masukan berapa key(1-%s):'%(makskey)))
        if key >= 1 and key <= makskey:
            return key

def ubah(pesan, kunci):
    kunci = -kunci
    merubah = ''
    for symbol in pesan:
        if symbol.isalpha():
            num = ord(symbol)
            num += kunci

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            merubah += chr(num)
        else:
            merubah += symbol
    return merubah

pesan = sandi()
kunci = keysandi()
print('kata aslinya adalah: ', ubah(pesan, kunci))
