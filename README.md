# Tugas_4

### Jawaban dari pertanyaan

- **Django UserCreationForm**: 
  Adalah form bawaan Django untuk proses pendaftaran. Form ini punya keunggulan karena sudah terintegrasi dengan model User Django dengan validasi yang telah disediakan dari sumber. Namun, kadang kurang fleksibel untuk kebutuhan khusus pengguna atau developer.

- **Autentikasi vs Otorisasi**: 
  Autentikasi berfokus pada verifikasi identitas pengguna, sedangkan otorisasi menentukan hak akses yang dimiliki pengguna. Kedua hal ini penting untuk tujuan menjaga keamanan aplikasi.

- **Cookies**: 
  Cookies adalah potongan data yang disimpan di browser pengguna dan dikirim kembali ke server setiap kali browser mengakses server tersebut. Django menggunakan cookies, khususnya session cookies, untuk mengelola data sesi pengguna.

- **Keamanan Cookies**: 
  Sangat penting untuk berhati-hati saat menyimpan informasi sensitif di cookies. Sebaiknya, informasi tersebut harus dienkripsi.

# Implementasi Autentikasi, Session, dan Cookies pada Django

## Langkah-Langkah Pembuatan

### 1. Membuat Fungsi Autentikasi

**a. Membuat Fungsi Registrasi**

- Buat file baru dengan nama `registration.py`.
- Implementasikan `UserCreationForm` untuk formulir registrasi.

**b. Membuat Fungsi Login**

- Buat file baru dengan nama `login.py`.
- Gunakan Django Authentication untuk memverifikasi pengguna.

**c. Membuat Fungsi Logout**

- Dalam `login.py`, tambahkan fungsi untuk logout.
- Gunakan `logout()` dari Django Authentication.

### 2. Membuat Data Dummy

- Buka Django Admin.
- Buat dua akun pengguna dengan masing-masing tiga data dummy.

### 3. Menghubungkan Model Item dengan User

- Buka file model (misalnya `models.py`).
- Tambahkan relasi ForeignKey antara model `Item` dan `User`.

### 4. Menampilkan Informasi Pengguna

- Dalam file views (misalnya `views.py`), gunakan `request.user` untuk mendapatkan informasi pengguna saat ini.
- Tampilkan informasi seperti username dan waktu login terakhir pada halaman utama aplikasi.




### Step by Step Penjelasan


## 1. registration.py
File yang berfungsi untuk proses registrasi sesuai ketentuan tugas.

- Menggunakan `UserCreationForm` untuk formulir registrasi yang diminta.
- Menghandle data dari formulir dan menyimpannya ke database.

## 2. views.py
File untuk menghandle proses login.

- Menerima input username dan password sesuai dengan keterangan tugas.
- Verifikasi dengan data yang ada di database.

## 3. views.py
File untuk proses logout.

- Menggunakan `logout()` dari Django untuk mengakhiri sesi pengguna.

## 4. models.py
Definisi model database.

- Model `Item` yang dihubungkan dengan model `User` menggunakan relasi ForeignKey.

## 5. views.py
Logika tampilan aplikasi.

- Menampilkan informasi pengguna saat ini menggunakan `request.user`.
- Render halaman dengan konteks data yang sesuai dengan keinginan tugas.

## 6. dummy_data.py
Script untuk mengenerate data dummy.

- Membuat dua akun pengguna dengan tiga data dummy untuk setiap akun.

## 7. cookies.py
Menghandle cookies dalam aplikasi.

- Menyimpan informasi seperti waktu login terakhir ke cookies.
- Mengambil data dari cookies untuk ditampilkan ke pengguna.

- ## 8. HTML Templates
- menghandle tampilan data dinamis untuk user

## 8. README.md
Dokumentasi dan jawaban pertanyaan tugas yang diberikan.

