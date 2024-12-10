# Latihan-8

Nama: Tiara Hayatul Khoir
NIM: 312410474
Kelas: TI.24.A.5
Mata Kuliah: Bahasa Pemrograman

## Membuat Program Sederhana Daftar Mahasiswa dengan Object-Oriented Programming (OOP)

Program ini memanfaatkan **Object-Oriented Programming (OOP)**, yaitu pendekatan pemrograman yang mengorganisasi kode dalam bentuk **class** dan **object**. Konsep OOP yang digunakan:  
- **Class**: Wadah yang mendefinisikan atribut dan method. Di sini ada class `Mahasiswa`.  
- **Method**: Fungsi yang ada di dalam class untuk melakukan tindakan tertentu (contoh: `tambah()`, `tampilkan()`, dll.).  
- **Encapsulation**: Data mahasiswa disimpan dalam atribut khusus `self.data_mahasiswa` di dalam class, sehingga terorganisasi dengan baik.  

---
## Penjelasan Alur Kode

### **Fitur Program**
1. **Tambah Data**  
   - Input: Nama, NIM, nilai tugas, UTS, dan UAS.  
   - Data disimpan dalam dictionary dengan struktur:  
     ```python
     {
         "nama": {
             "nim": "nim_value",
             "tugas": tugas_value,
             "uts": uts_value,
             "uas": uas_value
         }
     }
     ```
2. **Tampilkan Data**  
   - Menampilkan daftar mahasiswa dengan perhitungan nilai akhir (30% tugas, 35% UTS, 35% UAS).  
3. **Hapus Data**  
   - Menghapus data mahasiswa berdasarkan nama.  
4. **Ubah Data**  
   - Mengubah nilai tugas, UTS, dan UAS mahasiswa berdasarkan nama.  

---

### **Atribut yang Digunakan**
- **`self.data_mahasiswa`**: Dictionary untuk menyimpan data mahasiswa.  
  - Key: Nama mahasiswa (string).  
  - Value: Dictionary berisi NIM, tugas, UTS, dan UAS.  

Contoh data:  
```python
{
    "Tiara": {"nim": "12345", "tugas": 80, "uts": 80, "uas": 80}
}
```

---

### **Cara Menjalankan Program**
1. **Salin kode ke editor Python**  
   Gunakan IDE seperti **IDLE**, **VS Code**, atau **Jupyter Notebook**.
   
2. **Jalankan Program**  
   Ketik perintah `python nama_file.py` di terminal/command prompt kalau pakai editor berbasis file.  

3. **Interaksi dengan Program**  
   Setelah program jalan, Anda akan disuguhkan pilihan menu:  
   - `(L)ihat`: Menampilkan data mahasiswa.  
   - `(T)ambah`: Menambah data mahasiswa.  
   - `(U)bah`: Mengubah data mahasiswa berdasarkan nama.  
   - `(H)apus`: Menghapus data mahasiswa berdasarkan nama.  
   - `(K)eluar`: Keluar dari program.  

4. **Input Data**  
   Saat memilih tambah data (`T`), Anda harus input:  
   - Nama  
   - NIM  
   - Nilai tugas  
   - Nilai UTS  
   - Nilai UAS  

5. **Cek Hasil**  
   Pilih `(L)` untuk menampilkan data dan lihat apakah data Anda sudah benar tersimpan.
