#User Input
Nik = int(input("Nik: "))
Nama_Karyawan = str(input("Nama Karyawan: "))
Alamat_Karyawan = str(input("Alamat Karyawan: "))
Gol = int(input("Golongan: "))
Jam_Kerja = int(input("Jam Kerja: "))

#Gol Conditions
if(Gol == 1):
    Uang_Harian = 20000 
    Uang_lembur = 10000
elif(Gol == 2):
    Uang_Harian = 15000 
    Uang_lembur = 7500
elif(Gol == 3):
    Uang_Harian = 10000 
    Uang_lembur = 5000

#Work Hours Condition
if(Jam_Kerja > 8):
    (Jam_Kerja - 8) * Uang_lembur 
else:
    Uang_lembur = 0

#Tunjangan && Upah Total Calculations
Tunjangan = Uang_Harian * 15/100
Upah_Total =(Uang_Harian * Jam_Kerja) + Tunjangan + Uang_lembur

#Print output
print("==================================")
print("          Upah Karyawan           ")
print("==================================")
print("Nik: ", Nik)
print("Nama Karyawan", Nama_Karyawan)
print("Alamat Karyawan: ", Alamat_Karyawan)
print("Golongan: ", Gol)
print("Uang Harian: ", Uang_Harian)
print("Jam Kerja:  ", Jam_Kerja)
print("Lembur: ", Uang_lembur)
print("Tunjangan: ", Tunjangan)
print("Upah Total: ", Upah_Total)
print("==================================")
