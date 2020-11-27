try:
    file = open('d:/anyfiles.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
