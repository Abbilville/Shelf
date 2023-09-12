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
   + Selanjutnya, kita perlu menginstall package-package yang diperlukan tapi karena sudah pernah pada tutorial sebelumnya sehingga kita tidak perlu install lagi. Tapi tidak apa tambahkan saja file `requirements.txt` yang isinya
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
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
     Maka akan terbentuk folder baru yang bernama `main` dan isinya kumpulan file yang muncul saat pertama kali membuat django app.
   + Jangan lupa, setiap membuat aplikasi, daftarkan aplikasi tersebut ke dalam `INSTALLED_APPS` yang ada pada file `settings.py` di direktori utama (direktori project)
     
     ```
     INSTALLED_APPS = [
     ...,
     'main',
     ...
     ]
     ```
   + Selanjutnya, buat folder baru di folder `main` yang diberi nama `templates` dan buat juga file yang diberi nama `main.html` di dalam folder tersebut.
   + `main.html` bisa diisi seperti [ini](https://github.com/Abbilville/Shelf/blob/main/main/templates/main.html).
   + Lalu pada file `models.py` bisa tambahkan class `Item` yang memiliki attribute `name`, `amount`, `description`, `price`, `category`, dan `id` yang implementasinya bisa dilihat di [sini](https://github.com/Abbilville/Shelf/blob/main/main/models.py).
   + Jangan lupa juga, setiap melakukan perubahan apapun pada file `models.py` kita perlu melakukan **migration** dengan cara menjalankan kode berikut di terminal.
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```
   + Selanjutnya pergi ke file `views.py` dan import `render` kedalamnya agar dapat menghubungkan `templates` dengan data yang ada di `views` seperti [ini](https://github.com/Abbilville/Shelf/blob/main/main/views.py)
   + Langkah berikutnya kita perlu untuk mengkofigurasi *routing* urls, yaitu agar urls aplikasi kita terhubung dengan urls pada project `Shelf`
   + Buat file `urls.py` di `main` dan isi dengan kode berikut.
     ```
     from django.urls import path
     from main.views import show_main

     urlpatterns = [
         path('', show_main, name='show_main'),
     ]
     ```
   + Selanjutnya pada `urls.py` di `Shelf` tambahkan `from django.urls import path, include` dan tambahkan `path('main/', include('main.urls')),` di dalam list `urlpatterns`
   + Selesai sudah, selanjutnya kita test apakah webnya berjalan dengan lancar, bisa menjalankan kode berikut di terminal
     ```
     python manage.py runserver
     ```
     dan buka link http://localhost:8000/main/ di browser manapun. Jika sudah terlihat tulisan yang ada pada `main.html` maka sudah aman.
   + Langkah terakhir kita buat test untuk melakukan pengecekan attribute-attribute yang ada di models, buka file `tests.py` yang ada di folder `main`, dan implementasikan test nya dengan cara seperti [ini](https://github.com/Abbilville/Shelf/blob/main/main/tests.py)
   + Jalankan kode berikut di terminal
     ```
     python manage.py test
     ```
     Jika ada tulisan OK di bawah maka test berhasil dan selesai sudah
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
