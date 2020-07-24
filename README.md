<h1> THIS README WILL BE CHANGED IN THE FUTURE BECAUSE OF THE CHANGES IN THE CODE. READ AT YOUR OWN RISK </h1>

# MAS-PartO

Mesin Absensi SPARTA Otomatis (MAS-PartO) digunakan untuk mengedit worksheet "Presensi" pada google sheet presensi SPARTA secara otomatis berdasarkan file chat ZOOM yang digunakan.

<h3>Requirement</h3>

Program menggunakan bahasa Python ver 3.7
Selain itu, digunakan beberapa <i>library</i> eksternal pada Python. <i>Library-library</i> eksternal yang digunakan dapat dilihat pada file `requirements.txt`. Anda dapat memasang semua <i>library</i> dengan menjalankan perintah berikut pada CLI root folder proyek:
```
pip install -r requirements.txt
```

Daftar <i>library</i> internal Python yang tidak terdapat di requirements:
- re
- time

<h3>Penggunaan</h3>

1. Pastikan anda sudah memiliki service-account dan service-account anda sudah memiliki role sebagai Editor di proyek bot-sparta
2. Pastikan service-account yang digunakan memiliki akses edit ke sheets "Presensi Peserta SPARTA 2019 v2"
3. Pastikan terdapat file `client_key.json` pada folder root proyek yang berisikan <i>key</i> dari service-account yang digunakan
4. Masukkan file chat ZOOM ke dalam folder file-chat
5. Jalankan CLI pada root, jalankan perintah berikut (Note: `py` dapat diganti dengan `python3` atau `python`, tergantung penamaan di PC anda):
```
py absensi.py
```
6. Masukkan data-data yang dibutuhkan, seperti nama file chat, day dan sesi ke berapa, serta waktu awal dan waktu akhir presensi
7. Tunggu hingga program selesai
7. Bila muncul error code 429 dan program terhenti, silahkan tunggu sekitar 1-2 menit lalu coba jalankan program kembali

Semangat MSDM Kader!!!! :fist: :fist:

<h6>Rafael Sean Putra 13518119</h6>
