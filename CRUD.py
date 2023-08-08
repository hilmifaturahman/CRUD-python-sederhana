"""
Created by Hilmi Faturahman Akbar
8 Agustus 2023
Tugas Soal Unjuk Pelatihan Python
Create Read Update Delete dengan module CSV
Program Sederhana dengan mengimplementasikan fungsi Create Read Update Delete
"""

import os
import csv

# fungsi bersihkan layar
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

# fungsi judul_barang
def judulbarang():
        judul = ["NAMA BARANG", "JUMLAH STOK", "HARGA SATUAN"]
        with open("daftar_barang.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(judul)
            
# fungsi buat_file_baru dan panggil fungsi judul_barang
def buat_file_baru():

    # jika file tidak ada maka buat file baru
    # jika sudah ada abaikan
    if os.path.exists("daftar_barang.csv"):
        cek_file = "ada"
    else:
        cek_file = "tidak ada"
    if cek_file == "tidak ada":
        buat_file = open("daftar_barang.csv", 'x')
        judul_barang()
        
# fungsi menu utama
def menu_utama():
    while True:
        print("=" * 60)
        print("Program untuk mengelola stok barang")
        print("=" * 60)
        print("[1]Tambah Barang\n[2]Cek Barang\n[3]Update Barang\n[4]Hapus barang\n[5]Keluar")
        print("=" * 60)
        
        valid_input = False
        while not valid_input:
            try:
                pilihan_menu = int(input("Silahkan Masukkan pilihan anda[1-5]:\n"))
                print("=" * 60)
                valid_input = True
            except ValueError:
                print("Maaf pilihan yang anda masukkan salah, silahkan coba lagi")
        while pilihan_menu > 6 or pilihan_menu < 1:
            try:
                print("Maaf pilihan yang anda masukkan salah, silahkan coba lagi")
                pilihan_menu = int(input("Silahkan Masukkan pilihan anda[1-5]:\n"))
                print("=" * 60)
            except ValueError:
                print()
        if pilihan_menu == 1:
            tambah_data_barang()
            while True:
                pilihan_tambah_barang = input("\nMau tambah barang lagi atau tidak?\n[ya][tidak]:\n")
                if pilihan_tambah_barang == "ya":
                    bersihkan_layar()
                    tambah_data_barang()
                    bersihkan_layar()
                elif pilihan_tambah_barang == "tidak":
                    bersihkan_layar()
                    break
                    menu_utama()
                else:
                    bersihkan_layar()
                    print("Maaf pilihan anda salah, silahkan coba lagi")
        elif pilihan_menu == 2:
            bersihkan_layar()
            cek_data_barang()
            pilihan_cek_barang = input("Tekan ENTER untuk kembali ke menu utama:\n")
            if pilihan_cek_barang == str or int:
                bersihkan_layar()
                menu_utama()                
        elif pilihan_menu == 3:
            bersihkan_layar()
            update_barang()
            while True:
                pilihan_update_barang = input("\nMau update barang lagi atau tidak?\n[ya][tidak]:\n")
                if pilihan_update_barang == "ya":
                    bersihkan_layar()
                    update_barang()
                elif pilihan_update_barang == "tidak":
                    bersihkan_layar()
                    break
                    menu_utama()
                else:
                    bersihkan_layar()
                    print("Maaf pilihan anda salah, silahkan coba lagi")
        elif pilihan_menu == 4:
            bersihkan_layar()
            hapus_barang()
            while True:
                pilihan_hapus_barang = input("\nMau hapus barang lagi atau tidak?\n[ya][tidak]:\n")
                if pilihan_hapus_barang == "ya":
                    bersihkan_layar()
                    hapus_barang()
                elif pilihan_hapus_barang == "tidak":
                    bersihkan_layar()
                    break
                    menu_utama()
                else:
                    bersihkan_layar()
                    print("Maaf pilihan anda salah, silahkan coba lagi")
        elif pilihan_menu == 5:
            break
        else:
            print("Maaf pilihan yang anda masukkan salah, silahkan coba lagi")
            pilihan_menu = int(input("Silahkan Masukkan pilihan anda[1-5]:\n"))

# fungsi tambah data barang
def tambah_data_barang():
    nama = str(input("Masukkan nama barang\t:"))
    nama = nama.upper()
    with open('daftar_barang.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].upper() == nama.upper():
                print("Nama Barang sudah ada")

    # jika user memasukkan input selain int maka kembali ke menu utama
    try:
        jumlah_barang = int(input("Masukkan jumlah barang\t:"))
    except:
        bersihkan_layar()
        print("Input yang anda masukkan salah")
        menu_utama()
    try:
        harga = int(input("Masukkan harga barang\t:"))
    except:
        bersihkan_layar()
        print("Input yang anda masukkan salah")
        menu_utama()
        
    with open('daftar_barang.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].upper() == nama.upper():
                jumlah_barang = int(row[1]) + int(jumlah_barang)
                break
        else:
            with open('daftar_barang.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama, jumlah_barang, harga])
            print(f"{nama} berhasil ditambahkan ke dalam database")
            return

    with open('daftar_barang.csv', 'r') as file:
        rows = list(csv.reader(file))

    for i, row in enumerate(rows):
        if row[0].upper() == nama.upper():
            rows[i][1] = str(jumlah_barang)
            break

    # buat data baru
    # jika nama barang sudah ada maka tambahkan jumlah barang saja
    with open('daftar_barang.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"\nNama barang sudah ada\nJumlah barang berhasil ditambahkan ke dalam jumlah stok {nama}")

# fungsi cek_barang
def cek_data_barang():
    # Buat data isi barang menjadi list
    isi_barang = []

    # baca data file yang telah di buat
    with open("daftar_barang.csv", "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        # Menghitung panjang maksimum setiap kolom
        max_length = [len(header[i]) for i in range(len(header))]

        # Membaca data dan mengupdate panjang maksimum untuk setiap kolom
        for row in csv_reader:
            isi_barang.append(row)
            max_length = [max(max_length[i], len(row[i])) for i in range(len(row))]

        # Menampilkan Judul    
        print(' | '.join([header[i].ljust(max_length[i]) for i in range(len(header))]))

        # Menampilkan baris pemisah antara judul dan isi barang
        print("=" * (sum(max_length) + (3 * (len(max_length) - 1))))

        # menampilkan setiap baris isi data
        for row in isi_barang:
            print(' | '.join([row[i].ljust(max_length[i]) for i in range(len(row))]))
        print("=" * (sum(max_length) + (3 * (len(max_length) - 1))))

# fungsi update barang
def update_barang():
    cek_data_barang()
    nama = input("Masukkan Nama barang yang akan di update:")
    nama = nama.upper()
    jumlah_barang = input("Masukkan jumlah stok baru\t\t:")
    harga = input("Masukkan Harga baru\t\t\t:")

    isi_barang = []
    with open("daftar_barang.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == nama.upper():
                row[1] = jumlah_barang
                row[2] = harga
            isi_barang.append(row)  
    if not any(row[0] == nama.upper() for row in isi_barang):
        print(f"{nama} tidak di temukan dalam database")
        return
    with open("daftar_barang.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(isi_barang)
    print(f"Data {nama} berhasil di update")

# fungsi hapus barang
def hapus_barang():
    cek_data_barang()
    nama = str(input("Masukkan Nama barang yang ingin di hapus:\n"))
    nama = nama.upper()
    isi_barang = []
    ditemukan = False
    with open("daftar_barang.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != nama:
                isi_barang.append(row)
            else:
                ditemukan = True
    if ditemukan:
        with open("daftar_barang.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(isi_barang)
        print(f"Data {nama} berhasil dihapus")
    else:
        print(f"Maaf {nama} tidak ada dalam database")

        
# panggil fungsi buat_file_baru kalau file tidak ada
buat_file_baru()

# panggil fungsi menu utama
menu_utama()


































        
              
    


















            
    
