# Shelf
### An online shopping website 
---
#### Creator: Abbilhaidar Farras Zulfikar
#### Students ID: 2206026012
#### Link: https://shelf.adaptable.app/main/
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
![Django Architecture](https://github.com/Abbilville/Shelf/assets/119837732/4f7e25a9-3115-43b5-a672-77b51e2ddb38 "Django Architecture_AbbilhaidarFarrasZulfikar_2206026012")

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
&nbsp;&nbsp;&nbsp;&nbsp; Virtual environment diperlukan sebab kita tidak ingin project yang sedang kita kerjakan 'bertabrakan' dengan project yang lain entah itu packagesnya atau dependenciesnya sehingga projectnya akan menjadi lebih aman. <br>
&nbsp;&nbsp;&nbsp;&nbsp; Ya, kita tetap bisa membuat aplikasi web berbasis Django walaupun tanpa menggunakan virtual environment, tapi hal ini sangat tidak direkomendasikan karena bisa saja terjadi error yang tidak diinginkan seperti ketidaksesuaian versi packages yang digunakan dan lain-lain.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya! <br>
   + **MVC (Model-View-Controller)** <br>
     MVC merupakan konsep architecture yang digunakan untuk mengimplementasikan interface pengguna dan memfokuskan pada pemisahan representasi data dari komponen-komponen yang berinteraksi atau memproses data.
   + **MVT (Model-View-Template)** <br>
     MVT merupakan konsep architecture yang mirip dengan MVC namun Controller sudah diurus oleh framework yang kita gunakan, dalam hal ini maka Controller sudah diurus oleh Django.
   + **MVVM (Model-View-ViewModel)** <br>
     MVVM merupakan konsep architecture yang terstruktur untuk memisahkan logika program dengan control interface pengguna.
     

|MVC|MVT|MVVM|
|---|---|---|
|Web applications, desktop applications, GUI-based apps|Web applications, Django framework (Python)|Modern single-page web apps|
|Controller: Menerima input user dan memanipulasi Model/View sesuai kebutuhan|Template: Menentukan cara data ditampilkan dalam View.|ViewModel: Menjadi media antara Model dan View, menangani input user, dan menghandle data untuk ditampilkan.|

---
### Pertanyaan untuk Tugas 3
1.  Apa perbedaan antara form POST dan form GET dalam Django?
    Form POST dan form GET merupakan method pada HTTP ketika kita sedang berurusan dengan form. <br> <br>
    POST method membuat browser mengemas data form, meng-encode datanya untuk ditransmisikan, mengirimkannya ke server, dan kemudian menerima responnya kembali. <br> <br>
    GET method membuat browser mengemas data yang disubmit menjadi string, dan menggunakannya untuk menghasilkan URL. The URL berisi alamat di mana data harus dikirim. <br> <br>
    Untuk lebih jelasnya, berikut perbedaan POST dan GET yang saya ambil dari web [W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp "W3Schools") <br>
    
|Type|POST|GET|
|---|---|---|
|Tombol kembali / Reload|Data akan disubmit ulang (Browser memperingatkan pengguna bahwa datanya akan disubmit ulang)|Tidak berbahaya|
|Bookmarked|Tidak bisa dibookmarked|Bisa dibookmarked|
|Cached|Tidak dicached|Bisa dicached|
|Tipe Encoding|application/x-www-form-urlencoded or multipart/form-data. Use multipart encoding for binary data|application/x-www-form-urlencoded|
|History|Parameters are not saved in browser history|Parameters remain in browser history|
|Restrictions on data length|No restrictions|Yes, when sending data, the GET method adds the data to the URL; and the length of a URL is limited (maximum URL length is 2048 characters)|
|Restrictions on data type|No restrictions. Binary data is also allowed|Only ASCII characters allowed|
|Security|GET is less secure compared to POST because data sent is part of the URL <br> Never use GET when sending passwords or other sensitive information!|POST is a little safer than GET because the parameters are not stored in browser history or in web server logs|
|Visibility|Data is not displayed in the URL|Data is visible to everyone in the URL|

2.  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    
3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    
4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

5.  Akses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
    
---
## References
1. [Django Architecture](https://data-flair.training/blogs/django-architecture/ "Data Flair")
2. [Python Virtual Environment](https://www.geeksforgeeks.org/python-virtual-environment/ "GeeksForGeeks")
3. [Difference between MVC and MVT design patterns](https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/ "GeekForGeeks")
4. [MVC, MVP, MVVM: Which One to Choose?](https://www.makeuseof.com/mvc-mvp-mvvm-which-choose/ "MakeUsOf")
5. [Working with Forms](https://docs.djangoproject.com/en/4.2/topics/forms/ "DjangoProject")
6. [HTTP Request Methods](https://www.w3schools.com/tags/ref_httpmethods.asp "W3Schools")
7. [What’s the Relationship Between XML, JSON, HTML and the Internet?](https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet "DeltaXML")
8. [XML Vs JSON: Which Is The Better Data Transfer Format?](https://openxmldeveloper.org/xml-vs-json-which-is-the-better-data-transfer-format/ "OpenXMLDeveloper")
