#SOAL NO 2a

string = input("Masukkan kalimat : ")

substring = input("Masukkan kata untuk dihitung: ")

count = string.count(substring)

print('ada', count, 'buah kata', substring)


#SOAL NO 2 b

string = input("Masukkan kalimat: ")

substring = input("Masukkan kata untuk dihitung: ")

count = string.casefold().count(substring)

print('ada', count, 'buah kata', substring)
