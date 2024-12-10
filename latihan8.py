class Mahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self):
        nama, nim = input("Nama: ").strip(), input("NIM: ").strip()
        try:
            tugas, uts, uas = (float(input(f"Nilai {k}: ")) for k in ["Tugas", "UTS", "UAS"])
            self.data_mahasiswa[nama] = {'nim': nim, 'tugas': tugas, 'uts': uts, 'uas': uas}
            print("Data berhasil ditambahkan!")
        except ValueError:
            print("Nilai harus berupa angka!")

    def tampilkan(self):
        print("\nDaftar Nilai")
        print("="*66)
        print("| NO |       NAMA      |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
        print("="*66)
        if self.data_mahasiswa:
            for no, (nama, data) in enumerate(self.data_mahasiswa.items(), start=1):
                akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
                print(f"| {no:<2} | {nama:<15} | {data['nim']:<8} | {data['tugas']:<5.0f} | {data['uts']:<3.0f} | {data['uas']:<3.0f} | {akhir:<7.2f} |")
        else:
            print("|                       TIDAK ADA DATA                      |")
        print("="*66)

    def hapus(self, nama):
        if self.data_mahasiswa.pop(nama, None):
            print(f"Data {nama} berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    def ubah(self, nama):
        if nama in self.data_mahasiswa:
            try:
                tugas, uts, uas = (float(input(f"Nilai baru {k}: ")) for k in ["Tugas", "UTS", "UAS"])
                self.data_mahasiswa[nama].update({'tugas': tugas, 'uts': uts, 'uas': uas})
                print("Data berhasil diubah!")
            except ValueError:
                print("Nilai harus berupa angka!")
        else:
            print("Data tidak ditemukan!")

class MahasiswaLanjut(Mahasiswa):
    def info(self):
        return "Ini adalah class untuk mahasiswa tingkat lanjut"
    def tampilkan(self, format_lengkap=True):
        if format_lengkap:
            super().tampilkan()
        else:
            print("\nDaftar Nilai Mahasiswa Tingkat Lanjut")
            print("="*31)
            print("|       NAMA      |    NIM    |")
            print("="*31)
            if self.data_mahasiswa:
                for nama, data in self.data_mahasiswa.items():
                    print(f"| {nama:<15} | {data['nim']:<8} |")
            else:
                print("|        TIDAK ADA DATA        |")
            print("="*31)

if __name__ == "__main__":
    daftar_nilai = MahasiswaLanjut()
    while True:
        menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar] Pilih menu: ").lower()
        if menu == 'l': 
            format_pilihan = input("Tampilkan format lengkap? (y/n): ").strip().lower()
            daftar_nilai.tampilkan(format_lengkap=(format_pilihan == 'y'))
        elif menu == 't': daftar_nilai.tambah()
        elif menu == 'h':
            nama = input("Nama yang akan dihapus: ").strip()
            daftar_nilai.hapus(nama)
        elif menu == 'u':
            nama = input("Nama yang akan diubah: ").strip()
            daftar_nilai.ubah(nama)
        elif menu == 'k':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")
