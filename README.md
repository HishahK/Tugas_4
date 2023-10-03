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

# Tugas_5

## Element Selector dalam CSS
Element Selector dalam CSS adalah pengidentifikasi yang digunakan untuk mengaplikasikan styling ke elemen HTML tertentu. Berikut beberapa contoh dan penggunaannya:

### 1. **Type Selector**: 
- **Manfaat**: Mengaplikasikan styling ke semua elemen dengan tipe tertentu.
- **Kapan Digunakan**: Ketika Anda ingin menerapkan styling umum ke elemen yang sama.

### 2. **Class Selector**: 
- **Manfaat**: Mengaplikasikan styling ke elemen dengan kelas tertentu.
- **Kapan Digunakan**: Ketika beberapa elemen berbagi styling yang sama.

### 3. **ID Selector**: 
- **Manfaat**: Mengaplikasikan styling ke elemen dengan ID tertentu.
- **Kapan Digunakan**: Untuk styling elemen unik.

## HTML5 Tags
HTML5 memperkenalkan sejumlah tag baru yang meningkatkan semantik dan fungsionalitas dokumen web:

- `<article>`: Merepresentasikan konten yang independen dan dapat digunakan secara terpisah dari konten sekitarnya.
- `<section>`: Membagi dokumen menjadi bagian atau bab.
- `<nav>`: Digunakan untuk navigasi.
- `<header>` dan `<footer>`: Menentukan header dan footer.
- `<figure>` dan `<figcaption>`: Digunakan bersama untuk menyediakan keterangan untuk gambar.

## Perbedaan antara Margin dan Padding
- **Margin**: Merupakan ruang di luar batas elemen, digunakan untuk mengatur jarak antar elemen.
- **Padding**: Merupakan ruang di dalam batas elemen, digunakan untuk mengatur jarak antara batas elemen dan kontennya.

## Perbedaan Tailwind dan Bootstrap
- **Tailwind CSS**: 
  - Framework CSS yang berfokus pada utilitas, memungkinkan desain cepat dan fleksibel.
  - Lebih fleksibel dan memungkinkan kustomisasi yang lebih besar.
  - Kurva pembelajaran lebih curam untuk pemula.

- **Bootstrap**: 
  - Menawarkan komponen desain pre-styled.
  - Kurva pembelajaran lebih landai.
  - Mungkin kurang fleksibel dibandingkan Tailwind dalam hal kustomisasi.

### Kapan Menggunakan Bootstrap atau Tailwind:
- **Bootstrap**: Cocok untuk prototyping cepat atau ketika Anda memerlukan desain yang konsisten dengan usaha minimal.
- **Tailwind**: Pilihan baik untuk desain yang unik dan kustom.

## Implementasi Checklist
1. **Desain Halaman**: Menggunakan Bootstrap untuk desain halaman dengan cepat menggunakan komponen pre-styled.
2. **Custom CSS**: Menambahkan styling kustom melalui CSS inline atau file eksternal untuk detil yang lebih spesifik.
3. **Kode HTML5**: Mengimplementasikan tag HTML5 untuk struktur konten yang lebih semantik dan aksesibilitas yang lebih baik.
4. **Implementasi Bonus**: Menambahkan kelas CSS kustom ke elemen terakhir dengan JavaScript atau logika templating untuk memenuhi kriteria bonus.


