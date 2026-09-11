# Variabel (tempat penyimpanan sementara / list utama)
jadwal_workout = []   # list kosong, akan diisi list-list jadwal workout

HARI_VALID = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]


# Fungsi bantu (Validasi input)

def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit() and int(nilai) > 0:
            return int(nilai)
        else:
            print("Input tidak valid! Harap masukkan angka lebih dari 0.\n")


def input_hari():
    while True:
        hari = input("Masukkan hari (Senin-Minggu): ").strip()
        if hari.lower() in HARI_VALID:
            return hari.capitalize()
        else:
            print("Hari tidak valid! Contoh yang benar: Senin, Selasa, dst.\n")


def input_teks(teks, nama_field):
    while True:
        nilai = input(teks).strip()
        if nilai != "":
            return nilai
        else:
            print(f"{nama_field} tidak boleh kosong! Coba lagi.\n")




# Fungsi CRUD

def tambah_data():
    print("\n=== TAMBAH JADWAL WORKOUT ===")
    hari = input_hari()

    jenis = input_teks("Masukkan jenis workut: ", "Jenis workout")  

    durasi = input_angka("Masukkan durasi (menit): ")
    set_latihan = input_angka("Masukkan jumlah set: ")
    reps = input_angka("Masukkan jumlah reps per set: ")

    status = input_teks("Masukkan status workout: ", "Status workout")

    data_baru = [hari, jenis, durasi, set_latihan, reps,status]  
    jadwal_workout.append(data_baru)

    print(f"\nBerhasil menambahkan jadwal: {data_baru}")


def tampilkan_data():
    print("\n=== DAFTAR JADWAL WORKOUT ===")

    # Menggunakan Conditional statement: untuk meng cek apakah list masih kosong
    if len(jadwal_workout) == 0:
        print("Belum ada jadwal workout.")
    else:
        print(f"{'No':<4}{'Hari':<10}{'Jenis Olahraga':<25}{'Durasi (menit)':<16}{'Set':<6}{'Reps':<5}{'status'}")
        print("-" * 75)
        # Looping (for) untuk menampilkan setiap data satu per satu
        for i, data in enumerate(jadwal_workout, start=1):
            hari, jenis, durasi, set_latihan, reps,status = data
            print(f"{i:<4}{hari:<10}{jenis:<25}{durasi:<16}{set_latihan:<6}{reps:<5}{status}")


def ubah_data():
    print("\n=== UBAH JADWAL WORKOUT ===")

    if len(jadwal_workout) == 0:
        print("Belum ada jadwal yang bisa diubah.")
        return

    tampilkan_data_ringkas()
    nomor = input_angka("Masukkan nomor jadwal yang ingin diubah: ")

    # Menggunakan Conditional statement: validasi nomor sesuai jumlah data
    if nomor < 1 or nomor > len(jadwal_workout):
        print("Nomor tidak ditemukan dalam daftar!")
        return

    index = nomor - 1
    data_lama = jadwal_workout[index]
    print(f"Data lama: {data_lama}")
    print("(Kosongkan input lalu tekan 'ENTER' jika tidak ingin mengubah field tersebut)")

    hari_baru = input(f"Hari baru [{data_lama[0]}]: ").strip()
    jenis_baru = input(f"Jenis olahraga baru [{data_lama[1]}]: ").strip()
    durasi_baru = input(f"Durasi baru (menit) [{data_lama[2]}]: ").strip()
    set_baru = input(f"Jumlah set baru [{data_lama[3]}]: ").strip()
    reps_baru = input(f"Jumlah reps baru [{data_lama[4]}]: ").strip()
    status_baru= input(f"Status workout baru [{data_lama[5]}]:").strip()

    # Menggunakan Conditional statement untuk masing-masing field
    if hari_baru != "":
        if hari_baru.lower() in HARI_VALID:
            jadwal_workout[index][0] = hari_baru.capitalize()
        else:
            print("Hari tidak valid, hari lama tetap dipakai.")

    if jenis_baru != "":
        jadwal_workout[index][1] = jenis_baru

    if durasi_baru != "":
        if durasi_baru.isdigit() and int(durasi_baru) > 0:
            jadwal_workout[index][2] = int(durasi_baru)
        else:
            print("Durasi tidak valid, durasi lama tetap dipakai.")

    if set_baru != "":
        if set_baru.isdigit() and int(set_baru) > 0:
            jadwal_workout[index][3] = int(set_baru)
        else:
            print("Jumlah set tidak valid, set lama tetap dipakai.")

    if reps_baru != "":
        if reps_baru.isdigit() and int(reps_baru) > 0:
            jadwal_workout[index][4] = int(reps_baru)
        else:
            print("Jumlah reps tidak valid, reps lama tetap dipakai.")

    if status_baru !="":
        jadwal_workout[index][5] = status_baru.capitalize()

    print(f"\n Data berhasil diubah menjadi: {jadwal_workout[index]}")


def hapus_data():
    print("\n=== HAPUS JADWAL WORKOUT ===")

    if len(jadwal_workout) == 0:
        print("Belum ada data yang bisa dihapus.")
        return

    tampilkan_data_ringkas()
    nomor = input_angka("Masukkan nomor data yang ingin dihapus: ")

    if nomor < 1 or nomor > len(jadwal_workout):
        print("Nomor tidak ditemukan dalam daftar!")
        return

    index = nomor - 1
    data_terhapus = jadwal_workout[index]

    # Konfirmasi sebelum menghapus, dengan validasi looping (y/n)
    while True:
        konfirmasi = input(f"Yakin ingin menghapus {data_terhapus}? (y/n): ").strip().lower()
        if konfirmasi in ["y", "n"]:
            break
        else:
            print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    if konfirmasi == "y":
        jadwal_workout.pop(index)
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def tampilkan_data_ringkas():
    for i, data in enumerate(jadwal_workout, start=1):
        print(f"{i}. hari :{data[0]} - jenis :{data[1]} - waktu :{data[2]} menit - {data[3]} set x {data[4]} reps - status: {data[5]}")
    print()


# MENU UTAMA (Looping while Sampai USer Pilih KELUAR)

def tampilkan_menu():
    print("\n========================================")
    print("   SISTEM PENGELOLAAN JADWAL WORKOUT")
    print("=" * 40)
    print("1. Tambah Jadwal Workout")
    print("2. Lihat Semua Jadwal")
    print("3. Ubah Jadwal Workout")
    print("4. Hapus Jadwal Workout")
    print("5. Keluar")
    print("=" * 40)


def main():
    print("Sistem Pengelolaan Jadwal Workout!")

    while True: 
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        # Menggunakan Conditional statement untuk validasi & pengecekan menu
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("\nSemangat Pemuda Workout!! >_<")
            break   
        else:
            print(" Pilihan tidak valid! Silakan pilih angka 1-5.")


if __name__ == "__main__":
    main()

