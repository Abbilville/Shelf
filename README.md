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
     
     ```python
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
     ```python
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
1.  Apa perbedaan antara form POST dan form GET dalam Django? <br>
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
|History|Parameter tidak disimpan dalam history browser|Parameters tersimpan di history browser|
|Batasan Panjang Data|Tidak ada batasan|Ada batasan, ketika mengirim data, GET method menambahkan data ke URL; dan panjang URL terbatas (batasa maksimumnya 2048 karakter)|
|Batasan Tipe Data|Tidak ada batasan|Hanya boleh ASCII characters|
|Security|Lebih aman|Kurang aman dibandingkan POST|
|Visibility|Data tidak ditampilkan di URL|Data terlihat oleh semua orang di URL|

2.  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
    &nbsp;&nbsp;&nbsp;&nbsp; Perbedaan yang mendasar antara XML, JSON, dan HTML adalah XML dan JSON digunakan untuk menyimpan data dan transaksi data sedangkan HTML digunakan untuk menjelaskan bagaimana data-data tersebut akan ditampilkan. Fungsi utama mengapa XML dan JSON dibedakan dengan HTML adalah agar data yang berubah secara dinamis dapat diakomodasi tanpa harus terus-menerus memodifikasi kode yang digunakan untuk menampilkan data. <br>
    &nbsp;&nbsp;&nbsp;&nbsp; Secara singkat, HTML menjadi landasan utama dalam web development dan digunakan untuk membangun webpagenya. XML dan JSON digunakan untuk mengirim data antar server dan sering digunakan bersamaan dengan HTML atau aplikasi lainnya. Berikutnya merupakan perbedaan utama antara XML dan JSON yang saya ambil dari [DeltaXML](https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/) <br>

|XML|JSON|
|---|---|
|eXtensible Markup Language|JavaScript Object Notation|
|Berasal dari SGML|berasal dari JavaScript|
|Markup language dan menggunakan tag structure untuk merepresentasikan data items|Cara untuk merepresentasikan object|
|Bisa menggunakan namespaces|Tidak bisa menggunakan namespaces|
|Tidak bisa menggunakan arrays|Bisa menggunakan arrays|
|Dokumennya sulit dibaca dan diiterpretasikan|Lebih mudah untuk dibaca|
|Harus diakhiri end tag|Tidak perlu diakhiri end tag|
|Lebih aman dari JSON|Kurang aman dibanding XML|
|Bisa diberi comment|Tidak bisa diberi comment|
|bisa menggunakan banyak encoding|hanya menggunakan UTF-8 encoding|
    
3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
    Ada banyak alasan mengapa JSON lebih umum digunakan dalam pertukaran data: <br>
    + JSON memiliki format yang lebih ringan dan readable untuk manusia. Bentuknya yang seperti Dictionary dalam python membuat kita juga lebih familiar dengan JSON dibandingkan dengan XML atau yang lainnya. <br>
    + JSON cenderung menghasilkan data yang lebih kompak dibandingkan dengan XML. Hal ini dapat mengurangi beban bandwidth dan waktu transfer data. <br>
    + Browser modern memiliki dukungan bawaan untuk parsing dan mengonversi data JSON menjadi objek JavaScript, sehingga mempermudah pengolahan data di sisi klien. <br> <br>
4.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    + Langkah pertama, seperti biasa ketika kita ingin memulai untuk melanjutkan mengerjakan project kita, jangan lupa untuk mengaktifkan virtual environment agar project kita tidak tidak bertabrakan dengan dependencies yang lain. Jalankan kode ini di terminal. <br>
      ```
      env\Scripts\activate.bat
      ```
    + Selanjutnya, buat folder `templates` di root folder dan buat juga file `base.html` yang isinya dapat dilihat di [sini](https://github.com/Abbilville/Shelf/blob/main/templates/base.html). kegunaan base.html ini adalah sebagai template dasar untuk file html lainnya. <br>
    + Pergi ke `settings.py` lalu ke variable `TEMPLATES`, tambahkan kode `BASE_DIR / 'templates'` di dalam list `DIRS` <br>
    + Buat file baru `forms.py` pada folder `main` dan isi filenya dengan: <br> <br>
     ```python
     from django.forms import ModelForm
     from main.models import Item

     class ItemForm(ModelForm):
        class Meta:
           model = Item
           fields = ["name", "amount", "price", "description", "category"]
     ```
    + Pada folder `templates` pada `main`, tambahkan file `create_item.html` dan isi dengan kode berikut: <br> <br>
     ```HTML
      {% extends 'base.html' %} 
   
      {% block content %}
      <h1>Add New Item</h1>

      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Item"/>
                  </td>
              </tr>
          </table>
      </form>
      
      {% endblock %}
     ```
    + Buka file `views.py` pada folder `main` dan tambahkan kode ini di paling atas: <br> <br>
     ```python
     from django.http import HttpResponseRedirect, HttpResponse
     from main.forms import ProductForm
     from django.urls import reverse
     from django.core import serializers
     from main.models import Item
     ```
   + Ubah function `show_main` menjadi seperti ini: <br> <br>
     ```python
     def show_main(request):
        item = Item.objects.all()

        context = {
           'name': 'Abbilhaidar Farras Zulfikar',
           'class': 'PBP F',
           'item' : item,
        }

        return render(request, "main.html", context)
     ```
     + Tambahkan 5 function berikut pada `views.py`: <br> <br>
     ```python
     # Function untuk menampilkan create_item.html
     def create_item(request):
         form = ItemForm(request.POST or None)

         if form.is_valid() and request.method == "POST":
             form.save()
             return HttpResponseRedirect(reverse('main:show_main'))

         context = {'form': form}
         return render(request, "create_product.html", context)
     ```

     ```
      def show_xml(request):
          data = Item.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```

     ```
      def show_json(request):
          data = Item.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```

     ```
      def show_xml_by_id(request, id):
          data = Item.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```

     ```
      def show_json_by_id(request, id):
          data = Item.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
     + Pada file `urls.py` di `main`, tambahkan import function yang sudah kita buat tadi di `views.py` dan tambahkan juga `urlpatterns`nya jadi seperti ini: <br> <br>
     ```python
      from django.urls import path
      from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
      
      app_name = 'main'
      
      urlpatterns = [
          path('', show_main, name='show_main'),
          path('create-item', create_item, name='create_item'),
          path('xml/', show_xml, name='show_xml'),
          path('json/', show_json, name='show_json'),
          path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
      ]
     ```
   + Jalankan `python manage.py runserver` untuk mencoba semuanya. <br>
5.  Akses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman
   + /create-item <br>
    ![image](https://github.com/Abbilville/Shelf/assets/119837732/3bbc695d-a854-4fa8-8483-5efba610387f)
   + /json/ <br>
    ![image](https://github.com/Abbilville/Shelf/assets/119837732/15ba247f-201f-4791-8e17-633c100aeed8)
   + /xml/ <br>
    ![image](https://github.com/Abbilville/Shelf/assets/119837732/da090eab-707f-424a-bdc3-7cc7924a7b82)
   + /json/60f0fa69-89fe-4017-948c-ee02a936b665 <br>
    ![image](https://github.com/Abbilville/Shelf/assets/119837732/bbe1cbd1-0a45-4125-980f-261208b06557)
   + /xml/99072892-9bff-4075-8df7-354872ea4dd1 <br>
    ![image](https://github.com/Abbilville/Shelf/assets/119837732/b3a9ecf8-414b-4f2a-905b-b3329c41b1d8)

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
