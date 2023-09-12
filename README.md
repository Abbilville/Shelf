# Shelf
https://shelf.adaptable.app/main/ <br>
---
### Pertanyaan untuk Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   + Langkah pertama, saya membuat folder baru untuk menempatkan project django saya dengan menamakan foldernya `Shelf`.
   + Lalu, buka terminal dan jalankan kode berikut untuk membuat virtual environmentnya <br>
     ```
     python -m venv env
     ```
     Aktifkan virtual environment dengan menjalankan kode berikut di terminal
     ```
     env\Scripts\activate.bat
     ```
     Kegunaan virtual environment akan dijelaskan pada pertanyaan ketiga.
   + Selanjutnya, kita perlu menginstall package-package yang diperlukan tapi karena sudah pernah pada tutorial sebelumnya sehingga kita tidak perlu install lagi.
   + Setelah itu, buat django project yang saya beri nama `Shelf` dengan menjalankan kode berikut di termimnal <br>
     ```
     django-admin startproject Shelf .
     ```
     Maka akan terbentuk folder baru yang bernama `Shelf` dan isinya kumpulan file yang muncul saat pertama kali membuat django project.
   + Buka file `settings.py` dan cari variable `ALLOWED_HOSTS` dan tambahkan `"*"` kedalam list, ini bertujuan agar semua host dapat mengakses aplikasi web.
   + Sekarang mulai untuk membuat aplikasi yang diberi nama `main` dengan menjalankan kode berikut
     ```
     python manage.py startapp main
     ```
     Maka akan terbentu folder baru yang bernama `main` dan isinya kumpulan file yang muncul saat pertama kali membuat django app
   + Jangan lupa, setiap membuat aplikasi, daftarkan aplikasi tersebut ke dalam `INSTALLED_APPS` yang ada pada file `settings.py` di direktori utama (direktori project)
     
     ```
     INSTALLED_APPS = [
     ...,
     'main',
     ...
     ]
     ```
   + Selanjutnya, buat folder baru di folder `main` yang diberi nama `templates` dan buat juga file yang diberi nama `main.html` di dalam folder tersebut
   + `main.html` bisa diisi seperti [ini](../main/templates/main.html)
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
