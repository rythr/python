jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')
jumlah_baca = 0

jumlah_paham = 0
print(f'Jumlah buku yang dibaca dan dipahami {jumlah_paham}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham + 1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca {jumlah_paham}')
if jumlah_paham == jumlah_buku:
        print('"Bu semua buku sudah dibaca dan dipahami"')
else :
        print(f'"Bu, tidak semua buku bisa dipahami. Budi hanya bisa memahami {jumlah_paham} buku"')



