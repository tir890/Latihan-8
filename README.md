# Latihan-8

Nama: Tiara Hayatul Khoir

NIM: 312410474

Kelas: TI.24.A.5

Mata Kuliah: Bahasa Pemrograman

## Membuat Program Sederhana Daftar Mahasiswa dengan Object-Oriented Programming (OOP)

### **Konsep Dasar Program**
Program ini sekarang mengimplementasikan empat konsep dasar OOP:  
- **Class dan Instance Class**: Class `Mahasiswa` dan subclass `MahasiswaLanjut` sebagai instance class-nya.  
- **Enkapsulasi**: Atribut `self.data_mahasiswa` dilindungi dalam class. Data hanya bisa diakses lewat method seperti `tambah`, `hapus`, dll.  
- **Inheritance**: Class `MahasiswaLanjut` mewarisi semua atribut dan method dari class `Mahasiswa`.  
- **Polimorfisme**: Method `tampilkan` di `MahasiswaLanjut` bisa menampilkan data dalam dua format berbeda (lengkap dan ringkas), tergantung argumen yang diberikan.

---

### **Fitur Program**
1. **Tambah Data**  
   - Input: Nama, NIM, nilai tugas, UTS, dan UAS.  
   - Data disimpan dalam dictionary `self.data_mahasiswa`.  

2. **Tampilkan Data**  
   - **Format Lengkap**: Menampilkan semua data mahasiswa dengan nilai akhir.  
   - **Format Ringkas**: Menampilkan hanya nama dan NIM mahasiswa.  

3. **Hapus Data**  
   - Menghapus data mahasiswa berdasarkan nama.

4. **Ubah Data**  
   - Mengubah nilai tugas, UTS, dan UAS mahasiswa berdasarkan nama.

5. **Informasi Tambahan (Class `MahasiswaLanjut`)**  
   - Method `info` memberikan keterangan tambahan bahwa ini adalah class untuk mahasiswa tingkat lanjut.  

---

### **Atribut yang Digunakan**
- **`self.data_mahasiswa`** (dalam class `Mahasiswa`):  
  Dictionary untuk menyimpan data mahasiswa.  
  Struktur:  
  ```python
  {
      "Nama": {"nim": "NIM", "tugas": tugas_value, "uts": uts_value, "uas": uas_value}
  }
  ```

---

### **Alur Program**
1. Program mulai dengan membuat instance `MahasiswaLanjut`:
   ```python
   daftar_nilai = MahasiswaLanjut()
   ```
2. **Menu Pilihan**  
   - `(L)ihat`:  
     - User diberikan pilihan dengan format lengkap (`y`) atau ringkas (`n`).  
     - Format lengkap menampilkan nilai rata-rata, sedangkan ringkas hanya nama dan NIM.  
   - `(T)ambah`: Input data mahasiswa baru.  
   - `(U)bah`: Ubah data mahasiswa berdasarkan nama.  
   - `(H)apus`: Hapus data mahasiswa berdasarkan nama.  
   - `(K)eluar`: Keluar dari program.  

3. **Interaksi dengan Data**  
   - Semua operasi (tambah, hapus, ubah, lihat) dilakukan dengan memanipulasi atribut `self.data_mahasiswa`.
  
# Hasil Kode Program
![Latihan-8](https://github.com/tir890/Latihan-8/blob/a55fd9d4bb54930dba35b1964acddb377b625910/Screenshot%202024-12-10%20145115.png)

# Gambar Flowchart
![]()
