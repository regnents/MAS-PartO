# MAS-PartO

---

Mesin Absensi SPARTA Otomatis (MAS-PartO) digunakan untuk mengedit worksheet "Presensi" pada google sheet presensi SPARTA secara otomatis berdasarkan file chat ZOOM atau hasil <i>copy-paste</i> dari chat di Google Meet yang digunakan.

<h3>Requirement</h3>



Program menggunakan bahasa Python ver 3.7
Selain itu, digunakan beberapa <i>library</i> eksternal pada Python. <i>Library-library</i> eksternal yang digunakan dapat dilihat pada file `requirements.txt`. Anda dapat memasang semua <i>library</i> dengan menjalankan perintah berikut pada CLI root folder proyek:
```
pip install -r requirements.txt
```

Daftar <i>library</i> internal Python yang tidak terdapat di requirements:
- re
- time

<h3>What to Do Before</h3>

<h5>A. Using ZOOM</h5>

1. Simpan chat yang ingin digunakan dari ZOOM
2. Pindahkan file chat tersebut ke dalam folder `file-chat`

<h5>B. Using Google Meet</h5>

1. <i>Select all</i> chat dari Google Meet, pastikan username dan waktu pengiriman pesan juga ter-<i>select</i>
2. <i>Copy</i> dan <i>paste</i> chat yang sudah di-<i>select</i> ke sebuah file .txt
3. Pindahkan file tempat menyalin chat ke dalam folder `file-chat`

<h3>Penggunaan</h3>

1. Pastikan anda sudah memiliki service-account dan service-account anda sudah memiliki role sebagai Editor di proyek bot-sparta
2. Pastikan service-account yang digunakan memiliki akses edit ke sheets "Presensi Peserta SPARTA 2019 v2"
3. Pastikan terdapat file `client_key.json` pada folder root proyek yang berisikan <i>key</i> dari service-account yang digunakan
4. Masukkan file chat ZOOM ke dalam folder file-chat
5. Jalankan CLI pada root, jalankan perintah berikut (Note: `py` dapat diganti dengan `python3` atau `python`, tergantung penamaan di PC anda):
```
py absensi.py
```
6. Pilih jenis file sumber yang digunakan, apakah menggunakan file chat ZOOM maupun file tempat salinan chat Google Meet
7. Masukkan data-data yang dibutuhkan, seperti nama file chat, day dan sesi ke berapa, serta waktu awal dan waktu akhir presensi
8. Tunggu hingga program selesai, file hasil proses presensi akan disimpan di folder `hasil-absensi`
9. Bila muncul error code 429 dan program terhenti, silahkan tunggu sekitar 1-2 menit lalu coba jalankan program kembali

Semangat MSDM Kader!!!! :fist: :fist:

<h6>Rafael Sean Putra 13518119</h6>
