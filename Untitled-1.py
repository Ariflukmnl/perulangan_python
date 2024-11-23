#kalimat yang akan dihitung jumlah huruf vokalnya
kalimat="saya adalah mahasiswa universitas perjuangan tasikmalaya program studi teknik informatika"
#daftar huruf vokal
vokal="aiueoAIUEO" 
#inisialisasi variabel untuk menghitung jumlah huruf vokal
jumlah_vokal=0
#perulangan untuk memeriksa setiap karakter dalam kalimat
for i in kalimat:
    if i in vokal:
        jumlah_vokal += 1
#output jumlah huruf vokal
print("jumlah huruf vokal dalam kalimat adalah:", jumlah_vokal)        
