#User Input
Nama_Pasien = str(input("Nama Pasien: "))
Kelas = int(input("Kelas(1/2/3): "))
Lama = int(input("Lama_Perawatan: "))

#Calculations
if(Kelas == 1):
    Biaya_Kamar = 30000 * Lama
    Biaya_Dokter = 10000
    Diskon = 10/100* Lama *(Biaya_Kamar+Biaya_Dokter)
    Total_Pembayaran = Lama *(Biaya_Kamar + Biaya_Dokter) - Diskon

elif(Kelas == 2):
    Biaya_Kamar = 20000 * Lama
    Biaya_Dokter = 7000
    Diskon = 15/100* Lama *(Biaya_Kamar+Biaya_Dokter)
    Total_Pembayaran = Lama *(Biaya_Kamar + Biaya_Dokter) - Diskon

elif(Kelas == 3):
    Biaya_Kamar = 10000 * Lama
    Biaya_Dokter = 5000
    Diskon = 15/100 * Lama *(Biaya_Kamar+Biaya_Dokter)
    Total_Pembayaran = Lama *(Biaya_Kamar + Biaya_Dokter) - Diskon


#Print Output
print("         RUMAH SAKIT DAERAH Dr.SOETOMO         ")
print("Nama Pasien: ", Nama_Pasien)
print("Kelas: ", Kelas)
print("Lama Perawatan: ", Lama)
print("Biaya Kamar: ", Biaya_Kamar)
print("Biaya Dokter: ", Biaya_Dokter)
print("Diskon: ", Diskon)
print("Total Pembayaran: ", Total_Pembayaran)
