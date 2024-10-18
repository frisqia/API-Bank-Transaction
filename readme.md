# membuat API transaksi antar bank

cara menjalankannya :

1. pipenv install
2. pipenv shell
3. python app.py
4. buka apidocs




## tool 

- sqlAlchemy
  SQLAlchemy adalah library untuk ORM (Object Relational Mapper) yang memudahkan interaksi dengan database dalam bahasa Python. Dengan SQLAlchemy, kita bisa memetakan tabel-tabel database ke dalam model Python, sehingga lebih mudah untuk menulis query database tanpa perlu menulis query SQL mentah.

  - ORM (Object Relational Mapping): SQLAlchemy menggunakan konsep ORM untuk memetakan objek Python ke tabel database. Objek seperti kelas User bisa langsung dipetakan ke tabel di database.
  - Session: Session adalah titik interaksi antara aplikasi Python dan database. SQLAlchemy menyediakan sessionmaker untuk menangani transaksi dan menjaga koneksi ke database secara efisien.
    saya juga menggunakan sessionmaker untuk membuat session untuk berinteraksi dengan database.
  - DeclarativeBase: DeclarativeBase digunakan sebagai basis dari model yang akan dibuat. Semua kelas model (seperti User) harus mewarisi dari kelas ini.
  
  ### Instalasi
  `` pipenv install sqlalchemy ``

- cerberus

  - Cerberus adalah library validasi data untuk Python yang memungkinkan kamu untuk memastikan bahwa data input yang diterima sesuai dengan aturan dan skema yang telah ditentukan. Cerberus mendukung validasi berbagai jenis data seperti string, integer, list, dll, dan bisa digunakan untuk validasi input pada API atau formulir pengguna.

  - Fitur utama:

    1. Mendefinisikan skema validasi yang kompleks dengan mudah
    2. Mendukung validasi tipe data, panjang, format, dan aturan lainnya
    3. Cocok untuk penggunaan pada API dan form untuk memvalidasi input dari pengguna

dan Di sini, Cerberus digunakan untuk memvalidasi input dari pengguna sebelum data disimpan ke database.
   ### instalasi
   `` pipenv install cerberus ``

- Flask Blueprint
  Blueprint dalam Flask memungkinkan pemisahan logika aplikasi ke dalam modul-modul terpisah. Blueprint berguna untuk membagi aplikasi besar menjadi beberapa bagian yang lebih kecil dan modular. Misalnya, setiap bagian seperti otentikasi, administrasi, atau pengguna bisa dipisah menggunakan blueprint untuk menjaga struktur aplikasi tetap terorganisir.

  - Fitur Utama:

    1. Membantu dalam membagi aplikasi besar menjadi bagian-bagian yang lebih modular
    2. Setiap blueprint bisa diatur dengan route, middleware, atau konfigurasi sendiri
    3. Mudah digunakan untuk mengelola route secara terpisah

    Dengan Blueprint, kamu dapat mengelola berbagai bagian aplikasi secara modular, menjadikan kode lebih bersih dan mudah dikelola.


- Flask Login
  Flask-Login adalah extension untuk Flask yang memudahkan otentikasi pengguna di aplikasi web. Library ini menyediakan cara sederhana untuk mengelola sesi pengguna, mengatur login, logout, dan akses ke halaman yang memerlukan otentikasi.

  - Fitur Utama:

    1.  Mempermudah otentikasi pengguna
    2. Menyimpan status login pengguna di sesi
    3. Melindungi route yang memerlukan login
   ### instalasi
   `` pipenv install flask-login ``

- Flasgger
Flasgger adalah library untuk menghasilkan dokumentasi Swagger API secara otomatis dari aplikasi Flask kamu. Swagger adalah standar untuk mendokumentasikan API sehingga developer lain dapat melihat endpoint, parameter, dan respons API yang tersedia.

  - Fitur Utama:

    1. Membuat dokumentasi API interaktif menggunakan Swagger
    2. Mendukung auto-generated API docs berdasarkan spesifikasi
    3. Menyediakan UI untuk menguji endpoint API langsung dari browser

    Dengan Flasgger, dokumentasi API kamu akan secara otomatis ter-generate dan bisa diakses melalui browser untuk referensi developer lain.

### instalasi

`` pipenv install flasgger ``

- dotenv
python-dotenv adalah library yang digunakan untuk memuat variabel lingkungan dari file .env ke dalam aplikasi. Ini memudahkan konfigurasi aplikasi, seperti menyimpan informasi sensitif seperti password atau API key di luar kode sumber.

   - Fitur Utama:

     1. Memudahkan pengelolaan variabel lingkungan
     2. Menyimpan informasi sensitif seperti kredensial database atau API key di luar kode sumber
     3. Memuat konfigurasi saat aplikasi dimulai

### instalasi

`` pipenv install python-dotenv ``



# Perbedaan Pip dan Pipenv

1. Pip
pip adalah tool default yang digunakan untuk mengelola paket Python. Dengan pip, kamu bisa menginstal library atau dependensi yang dibutuhkan proyek Python-mu.

 - Kegunaan Utama:

   - Menginstal paket dari PyPI (Python Package Index).
   - Mengelola dependensi proyek secara sederhana.
   - Paket yang diinstal akan masuk ke environment global atau virtual environment jika sudah diaktifkan.
 - Kelebihan:

   - Ringan dan sudah menjadi standar untuk menginstal library Python.
   - Bisa digunakan di dalam virtual environment yang dikelola secara manual (misalnya menggunakan virtualenv atau venv).
 - Kekurangan:

   - Tidak otomatis membuat virtual environment.
   - Tidak mengelola file Pipfile atau Pipfile.lock, sehingga manajemen dependensi kurang terstruktur.

   - contoh :
    `` pip install flask ``

2. Pipenv
pipenv adalah tool manajemen dependensi yang lebih baru dan lebih terstruktur daripada pip. Pipenv menggabungkan fungsionalitas pip dan virtualenv, serta menambahkan beberapa fitur baru untuk manajemen proyek yang lebih baik.

  - Kegunaan Utama:

    - Mengelola virtual environment secara otomatis: Pipenv akan membuat virtual environment setiap kali kamu membuat proyek baru, sehingga memisahkan dependensi proyekmu dari sistem Python global.
    - Menggunakan Pipfile dan Pipfile.lock: Pipenv menggantikan file requirements.txt dengan Pipfile yang lebih mudah dibaca manusia dan Pipfile.lock untuk manajemen versi yang lebih terkontrol.
    - Instalasi paket: Pipenv tetap mengandalkan pip untuk menginstal paket, namun menyediakan lingkungan yang lebih terorganisir dan aman.
  - Kelebihan:

    - Otomatis membuat virtual environment.
    - Pipfile menggantikan requirements.txt dan lebih mudah dibaca.
    - Manajemen versi lebih aman dengan Pipfile.lock, memastikan bahwa semua orang dalam tim menggunakan versi dependensi yang sama.
    - Menyediakan integrasi dengan keamanan dependensi (misalnya, pengecekan apakah ada paket yang memiliki kerentanan keamanan).
  - Kekurangan:

    - Sedikit lebih lambat dibandingkan pip karena membuat virtual environment dan mengelola dua file (Pipfile dan Pipfile.lock).
    - Lebih kompleks untuk proyek kecil atau sederhana yang hanya membutuhkan sedikit dependensi.
  - Contoh:

   - Membuat proyek baru dengan Pipenv:
    `` pipenv install flask ``
    Ini akan membuat virtual environment secara otomatis dan menambahkan flask ke dalam Pipfile.
   - Menjalankan proyek di virtual environment yang dibuat oleh Pipenv:
    `` pipenv shell ``
   - Mengunci dependensi ke Pipfile.lock untuk memastikan semua anggota tim menggunakan versi paket yang sama:
    `` pipenv lock ``

3. Ringkasan Perbedaan Utama


| Fitur                    | Pip                                       | pipenv                                   |
|--------------------------|-------------------------------------------|------------------------------------------|
| Manajemen Virtual Environment | Tidak otomatis (perlu virtualenv atau venv) | Otomatis membuat dan mengelola virtual environment |
| Manajemen Dependensi     | Menggunakan requirements.txt               | Menggunakan Pipfile dan Pipfile.lock     |
| Keamanan                 | Tidak ada pengecekan keamanan otomatis    | Pengecekan keamanan otomatis untuk kerentanan |
| Kecocokan                | Proyek kecil/sederhana                    | Proyek besar dengan banyak dependensi    |
