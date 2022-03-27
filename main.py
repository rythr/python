print('"Kak, tolong belikan Bakso dan mie ayam untuk kita makan, ini uangnya" kata Bapak')
print('Bapak memberi uang dan memberi list pesanan')

# Information
list_pesanan = {'Bapak': 'Bakso Telur', 'Ibu': 'Mie Ayam', 'Kakak': 'Mie Ayam Pangsit', 'Adik': 'Bakso Telur'}
list_harga = {'Bakso Telur': '10000', 'Mie Ayam': '12000', 'Mie Ayam pangsit': '13000'}
uang_bapak = 100000
harga_bakso_telur = 10000
harga_mie_ayam_pangsit = 13000
harga_mie_ayam = 12000
harga_fanta_1_lt = 10000
harga_tea_jus = 2000
harga_rokok = 30000
sisa_kembalian_sebelum_membeli_rokok = 55000
sisa_setelah_membeli_rokok = 25000

print('List Pesanan :')
print(list_pesanan['Bapak'])
print(list_pesanan['Ibu'])
print(list_pesanan['Kakak'])
print(list_pesanan['Adik'])

print('"Berapa harganya" Kakak bertanya pada tukang Bakso')
print('Tukang Bakso pun menghitung dan berkata')
print('Bakso Telur', list_harga['Bakso Telur'], 'dikali dua jadi', harga_bakso_telur*2)
print('Mie Ayam', list_harga['Mie Ayam'])
print('Mie Ayam Pangsit', list_harga['Mie Ayam pangsit'])
print('jadi totalnya', harga_bakso_telur*2+harga_mie_ayam+harga_mie_ayam_pangsit)

print('kakak memberi uang 100000')
print('Tukang bakso mengembalikan', uang_bapak-harga_bakso_telur*2-harga_mie_ayam-harga_mie_ayam_pangsit)
print('uang tersisa', sisa_kembalian_sebelum_membeli_rokok)
if sisa_kembalian_sebelum_membeli_rokok > 30000:
    print('Kakak membeli rokok')
else:
    print('Kakak tidak membeli rokok')
print('setelah membeli rokok uang tersisa', sisa_kembalian_sebelum_membeli_rokok-harga_rokok)

if sisa_setelah_membeli_rokok > 20000:
    print('karena uang tersisa 25000 kakak jadi membeli Fanta 1 Ltr 2 seharga', harga_fanta_1_lt*2)
else:
    print('Kakak membeli Tea Jus 4')

print('Kakak kembali kerumah dan memberikan laporan pengeluarannya')
print('Bakso telur', harga_bakso_telur, 'dikali 2 jadi', harga_bakso_telur*2)
print('Mie Ayam', harga_mie_ayam)
print('Mie Ayam Pangsit', harga_mie_ayam_pangsit)
print('Bapak tadi kasih 100000 dikurang yang tadi jadi sisa', uang_bapak-harga_bakso_telur*2-harga_mie_ayam-harga_mie_ayam_pangsit)
print('Terus beli rokok', harga_rokok, 'jadi', sisa_kembalian_sebelum_membeli_rokok-harga_rokok)
print('Karena sisa', sisa_setelah_membeli_rokok, 'Kakak jadi beli Fanta seharga', harga_fanta_1_lt)
print('Beli dua jadi', harga_fanta_1_lt*2)
print('sisa uang bapak jadi', uang_bapak-harga_bakso_telur-harga_mie_ayam-harga_mie_ayam_pangsit-harga_rokok-harga_fanta_1_lt*2)
