# Shelf
### An online shopping website 
---
#### Creator: Abbilhaidar Farras Zulfikar
#### Students ID: 2206026012
#### Link: http://abbilhaidar-farras-tugas.pbp.cs.ui.ac.id
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
        item_sum = 0
        for item in items:
            item_sum += item.amount

        context = {
           'name': 'Abbilhaidar Farras Zulfikar',
           'class': 'PBP F',
           'item' : items,
           'message': f"You have {item_sum} items in the shelf",
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
          path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
      ]
     ```
   + Pada file `main.html` di folder `templates` pada `main` ubah kodenya menjadi: <br> <br>
     ```HTML
      {% extends 'base.html' %}

      {% block content %}
          <h1>Shelf Page</h1>
      
          <h5>Name:</h5>
          <p>{{name}}</p>
      
          <h5>Class:</h5>
          <p>{{class}}</p>
      
          <table>
              <tr>
                  <th>Name</th>
                  <th>Amount</th>
                  <th>Price</th>
                  <th>Description</th>
                  <th>Category</th>
                  <th>Date Added</th>
              </tr>
          
              {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
              {{message}}
              {% for item in items %}
                  <tr>
                      <td>{{item.name}}</td>
                      <td>{{item.amount}}</td>
                      <td>{{item.price}}</td>
                      <td>{{item.description}}</td>
                      <td>{{item.category}}</td>
                      <td>{{item.date_added}}</td>
                  </tr>
              {% endfor %}
          </table>
          
          <br />
          
          <a href="{% url 'main:create_item' %}">
              <button>
                  Add New Item
              </button>
          </a>
    
      {% endblock content %}
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
### Pertanyaan untuk Tugas 4
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
   Kelebihan dalam menggunakan `UserCreationForm` adalah kita tidak perlu menghandle lagi password yang tidak sesuai dengan ketentuan atau nama *user* yang duplikat, oleh karena itu sebagai *software engineer*, dengan adanya fitur ini sangat mempermudah hidup. <br>
   Kekurangan dalam menggunakan `UserCreationForm` mungkin ketika membuat akun, limitasi passwordnya sangat strict sehingga membuat *user* bingung mau bikin password apa. <br>
   
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
   Autentikasi adalah proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna yang mencoba mengakses aplikasi web adalah orang tepat. Sedangkan Otorisasi adalah proses yang mengatur akses pengguna terotentikasi ke sumber daya atau fungsi tertentu dalam aplikasi web. Ini menentukan apa yang dapat dilakukan oleh pengguna yang sudah terotentikasi. <br>
   Mereka berdua penting karena autentikasi dan otorisasi dapat memastikan bahwa aplikasi web menjadi aman, data sensitif terlindungi, dan *user* memiliki akses yang sesuai dengan function yang diberikan. <br>
   
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookie adalah informasi yang disimpan dalam web pengguna. Cookies digunakan untuk menyimpan data pengguna dalam sebuah file secara permanen (atau untuk jangka waktu tertentu). Cookies memiliki tanggal dan waktu kedaluwarsa dan akan dihapus secara otomatis ketika waktu kedaluwarsanya tiba. Django menyediakan metode bawaan untuk mengatur dan mengambil cookies. <br>
   Dalam Django sendiri, kita dapat mengakses Cookies dengan mengambil saja value yang ada di dictionary COOKIES menggunakan key yang ada misalnya pada tugas ini keynya yaitu 'last_login' dan akan mengembalikkan value kapan terakhir kali user login. <br>
   
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
   Data dalam cookies itu tidak berbahaya dan tidak dapat menginfeksi sistem atau situs web dengan aplikasi apapun. Password juga tidak akan disimpan dalam cookie jadi akan aman-aman saja. Namun jika cookies tidak diatur dengan baik, hal ini dapat menjadi pelanggaran privasi pengguna, terutama jika informasi pribadi seperti nama, alamat, atau data sensitif lainnya tersimpan dalam cookies. <br>
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   + Langkah pertama untuk mengimplementasikan fungsi login, registrasi, dan logout adalah dengan menambahkan fungsi di views.py, untuk registrasinya sendiri disini menggunakan `UserCreationForm` agar dapat mempermudah hidup. untuk implementasinya bisa tambahkan kode berikut di `views.py` <br>
   ```python
   ...
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages

   ...

   def register(request):
       form = UserCreationForm()
   
       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
   ```
   + Untuk fungsi login dan logoutnya bisa tambahkan kode berikut di `views.py` <br>
   ```python
   ...
   from django.contrib.auth import authenticate, login, logout
   from django.contrib.auth.decorators import login_required

   @login_required(login_url='/login')
   def show_main(request):
   ...

   def login_user(request):
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('main:show_main')
           else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```
     `@login_required(login_url='/login')` berguna agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
   + Setelah membuat fungsinya, sekarang buat htmlnya agar registrasi dan login memiliki tampilannya. Buat file `register.html` dan `login.html` pada directori `main/templates/` dan dapat diimplementasikan seperti ini: [register.html](https://github.com/Abbilville/Shelf/blob/main/main/templates/register.html) [login.html](https://github.com/Abbilville/Shelf/blob/main/main/templates/login.html) <br>
   + Setelah itu tambahkan juga path masing-masing ke `urls.py` pada direktori `main` <br>
   ```python
   urlpatterns = [
       ...
       path('register/', register, name='register'), 
       path('login/', login_user, name='login'),
       path('logout/', logout_user, name='logout'),
       ...
   ]
   ```
   + Selanjutnya jalankan `python manage.py runserver` dan buka `http://localhost:8000/` pada web untuk mencoba fitur-fitur yang baru saja ditambahkan. <br>
   + Lalu pada ceklis *checklist* kedua disuruh untuk membuat dua *dummy* account dengan masing-masing tiga *dummy* data. Untuk saat ini semua akun akan terhubung ke data yang sama entah siapapun yang membuatnya. Sekarang kita akan membuat user menjadi bagian dari models agar setiap account memiliki datanya masing-masing. Tabi sebelum itu bikin dulu 1 akun untuk langkah selanjutnya<br>
   + Pada `models.py` di direktori `main`, tambahkan `user` pada class Item <br>
   ```python
   ...
   from django.contrib.auth.models import User

   class Item(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
   ...
   ```
   + Lalu ubah function `show_main` dan `create_product` pada `views.py` di direktor `main`<br>
   ```python
   ...
   
   def show_main(request):
       products = Product.objects.filter(user=request.user)
   
       context = {
           'name': request.user.username,
            ...
   ...
   
   def create_product(request):
       form = ProductForm(request.POST or None)
      
       if form.is_valid() and request.method == "POST":
           product = form.save(commit=False)
           product.user = request.user
           product.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   ...
   ```
   + Karena sekarang user dan models sudah saling terhubung maka sudah bisa untuk masing-masing akun memiliki datanya masing-masing. <br>
   + Selanjutnya, karena kita mengubah `models.py` maka kita perlu melakukan migrasi dengan menjalankan `python manage.py makemigrations` kemudian `python manage.py migrate`. <br>
   + Untuk mengimplementasikan *checklist* keempat, kita perlu memanfaatkan cookies yang ada pada Django. Pada `views.py` di direktori `main` tambahkan `import datetime`. <br>
   + Setelah itu ubah fungsi `login_user` agar men-set cookies dengan key `last_login` dengan waktu sekarang <br>
   ```python
   def login_user(request):
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main")) 
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
           else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
   ```
   + Pada fungsi `show_main`, tambahkan variable `last_login` di dalam `context` dan ambil datanya dari COOKIES <br>
   ```python
   def show_main(request):
       items = Item.objects.filter(user=request.user)
       item_sum = 0
       for item in items:
           item_sum += item.amount
   
       context = {
           'name': request.user.username,
           'class': 'PBP F',
           'items' : items,
           'message': f"You have {item_sum} items in the shelf",
           'last_login': request.COOKIES['last_login'], # <---- Ini
       }

    return render(request, "main.html", context)
   ```
   + Ubah juga function `logout_user` <br> 
   ```python
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
   ```
   + Tambahkan juga kode ini di `main.html` pada direktori `main/templates` di antara tabel dengan tombol <br>
   ```HTML
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```
   + Nah sekarang jika login maka akan terlihat tulisan kapan terakhir loginnya <br>
---
### Pertanyaan untuk Tugas 5
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
   + **Element Selector** <br>
      Element selector memilih elemen-elemen yang ada di HTML berdasarkan nama elemennya. i.e. p, h1, h2, div, body. Element selector tepat digunakan jika kita ingin menstyle 1 element yang diinginkan secara keseluruhan.
   + **Id Selector** <br>
      Id selector menggunakan atribut id dari sebuah elemen HTML untuk memilih elemen tertentu. Id dari sebuah elemen bersifat unik dalam sebuah halaman, sehingga selektor id dapat digunakan untuk memilih elemen-elemen yang sifatnya unik. Untuk memilih sebuah elemen dengan id tertentu, dapat menggunakan pagar (#), diikuti oleh id dari elemen tersebut. Id selector tepat digunakan jika kita ingin menstyle beberapa elemen dengan id yang sama. contoh `<div id="button>` maka di file css nantinya untuk memilih div dengan id "button" hanya perlu menulis `#button {...}`.
   + **Class Selector** <br>
      Class selector memilih elemen-elemen HTML berdasarkan atribut kelasnya. Untuk memilih elemen-elemen berdasarkan kelasnya, dapat menggunakan karakter titik (.), diikuti oleh nama kelas. Class selector tepat digunakan jika kita ingin menstyle beberapa elemen dengan class yang sama. contoh `<div class="btn-class">` maka di file css nantinya untuk memilih div dengan class "btn-class" hanya perlu menulis `.btn-class {...}`.
   + **Universal Selector**
      Universal selector (*) memilih semua elemen yang ada di HTML. Universal Selector tepat digunakan jika kita ingin menstyle semua elemen yang ada di HTML. maka yang ada di file css nantinya adalah`* {...}`.
   + **Grouping Selector**
     Grouping selector intinya adalah kita dapat memberikan tanda koma (,) pada css file nantinya agar selectornya mendapatkan perilaku yang sama. Grouping selector tepat digunakan jika ada beberapa elemen berbeda namun ingin dibuat dengan style yang sama. `p, h1, h1 {...}`.
     
2. Jelaskan HTML5 Tag yang kamu ketahui. <br>

|Tag|Deskripsi|
|---|---------|
|`<!--...-->`|Comment pada HTML|
|`<a>`|Anchor, biasanya untuk link|
|`<body>`|Body dari HTMLnya|
|`<br>`|Line break|
|`<button>`|Tombol|
|`<div>`|Section dalam HTML|
|`<form>`|Untuk form|
|`<h1> to <h6>`|Header 1 sampai 6|
|`<html>`|Memberitahu kalo ini dokumen HTML|
|`<img>`|Menampilkan gambar|
|`<nav>`|Untuk navigation bar|
|`<p>`|Untuk paragraph|
|`<table>`|Membuat table|
|`<td>`|Table Cell|
|`<tr>`|Table Row|

3. Jelaskan perbedaan antara margin dan padding. <br>
   Margin digunakan untuk memberikan jarak di sekitar elemen, **di luar border** yang telah didefinisikan.<br>
   Padding digunakan untuk memberikan jarak di sekitar elemen, **di dalam border** yang telah didefinisikan.<br>
![1_L5bN2lty8lg5F50PTo4jtw](https://github.com/Abbilville/Shelf/assets/119837732/6b6b8c75-5044-4af1-8cda-4fee12cee202)

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? <br>

|Aspek|Tailwind CSS|Bootstrap|
|---|---|---|
|Filosofi|Utility-first, konfigurasi kustom|Komprehensif, desain bawaan|
|Kelengkapan Komponen|Terbatas, memerlukan pengembangan|Kaya akan komponen desain|
|Desain Visual|Tergantung pada penggunaan kelas CSS|Desain bawaan yang konsisten|
|Kustomisasi|Tinggi, mudah disesuaikan|Terbatas, memerlukan penyesuaian yang lebih besar|
|Ukuran Bundle|Lebih kecil, hanya memuat apa yang diperlukan|Lebih besar karena banyak komponen|
|Pengembangan Cepat|Lebih cepat karena kelas utilitas|Lebih lambat karena perlu menyesuaikan komponen|
|Penggunaan untuk Proyek Kecil|Tidak efisien karena banyak kelas CSS|Efisien karena komponen bawaan|
|Penggunaan untuk Proyek Besar|Efisien karena mudah disesuaikan|Tidak selalu efisien karena banyak komponen bawaan|
|Komunitas dan Dukungan|Cepat berkembang, banyak sumber daya|Stabil, komunitas besar dan dokumentasi lengkap|

#### Kapan sebaiknya menggunakan Bootstrap
   + Bootstrap cocok digunakan jika ingin mengembangkan proyek dengan cepat dan memerlukan banyak komponen desain yang telah ada. <br>
   + Jika memiliki anggaran waktu dan sumber daya yang terbatas, Bootstrap dapat menghemat waktu dengan desain bawaan yang responsif. <br>
   + Bootstrap juga cocok untuk proyek yang memerlukan dukungan yang stabil dan memiliki dokumentasi yang lengkap. <br>

#### Kapan sebaiknya menggunakan Tailwind
   + Tailwind CSS merupakan pilihan yang baik jika ingin memiliki kontrol penuh atas desain dan tidak ingin terikat dengan gaya desain bawaan. <br>
   + Cocok untuk proyek-proyek yang memerlukan desain yang sangat kustom dan fleksibel. <br>
   + Jika ingin mengoptimalkan ukuran bundle (load time) proyek, Tailwind mungkin merupakan pilihan yang lebih baik karena hanya memuat apa yang diperlukan. <br>
   + Tailwind cocok untuk developer yang memiliki pemahaman yang baik tentang CSS. <br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   + Langkah pertama seperti biasa jalankan `env\Scripts\activate.bat` <br>
   + Lalu untuk mengimplementasikan css pada setiap file HTML secara external, buatlah folder baru pada `main` dan beri nama `static`. Buat juga folder baru yang bernama `css` untuk menampung file css dan saya juga buat folder `icon` untuk menampung file `.png` untuk icon pada page saya. <br>
   + Lalu buat semua style yang sesuai dengan HTMLnya. Misal ingin memberi style pada file `main.html`, maka buat file `main.css` pada `main/static/css` dan mulailah memberi style pada file tersebut. <br>
   + Untuk menghubungkan file css dengan html yang diinginkan tambahkan kode berikut di bagian atas html yang diinginkan: <br>
   ```
   ...
   {% load static %}
   <head>
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
   </head>
   ```
   + Kode tersebut berfungsi untuk meload static yang mana akan mengarah ke folder static, dan stylesheet mengarah pada `css/main.css` pada folder static.
   + Lakukan hal yang sama untuk page login, register, add_item, dan edit_item. <br>
   + Jalankan `python manage.py runserver` untuk melihat perubahan pada html. <br>
---
### Pertanyaan untuk Tugas 6
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.<br>
   Asynchronous Programming mengizinkan program untuk melanjutkan menjalankan tugas lain sementara operasi I/O atau tugas berkepanjangan sedang berlangsung. Ini meningkatkan responsivitas aplikasi dan efisiensi karena program tidak harus menunggu. Namun, asynchronous programming bisa lebih kompleks dalam desain dan memerlukan pemahaman yang lebih dalam tentang konsep seperti callback, promise, atau async/await.<br>
   Synchornous Programming pada dasarnya menjalankan operasi I/O atau tugas satu per satu, mengharuskan program menunggu hingga satu operasi selesai sebelum melanjutkan ke yang berikutnya. Meskipun sederhana untuk dipahami, synchronous programming cenderung kurang responsif dan mungkin terasa lambat dalam situasi di mana ada I/O yang memakan waktu.<br>

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.<br>
   Paradigma event-driven programming adalah pendekatan dalam pemrograman yang fokus pada pengelolaan dan pemrosesan peristiwa (events) yang terjadi dalam program atau aplikasi dan biasanya sering digunakan dalam JavaScript dan AJAX (Asynchronous JavaScript and XML). <br><br>
   Pada tugas ini, event-driven programming diimplementasi menggunakan button. Button tersebut contohnya, increment item, decrement item, edit item, delete item, add item, login, logout, dll.<br>

3. Jelaskan penerapan asynchronous programming pada AJAX.<br>
   Dalam AJAX, asynchronous programming diimplementasikan melalui berbagai metode seperti penggunaan XMLHttpRequest dengan callback, penggunaan fetch API dengan promise, dan penggunaan fetch API dengan async/await. Callback digunakan untuk menjalankan kode secara asinkron, sehingga program tidak harus menunggu kode sebelumnya selesai sebelum menjalankan kode berikutnya; sebaliknya, kode berikutnya dapat dieksekusi segera setelah kode sebelumnya diinisialisasi, dan ketika kode tersebut selesai, fungsi callback akan dipanggil. Sementara itu, promise memiliki prinsip kerja yang mirip dengan callback, namun memberikan pendekatan yang lebih terstruktur dan mudah dimengerti. Terakhir, async/await mengubah kode asynchronous sehingga eksekusinya menyerupai kode synchronous, membuatnya lebih mudah dipahami dan dikelola dalam hal pembacaan dan pemeliharaan kode. <br>
   
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.<br>

|Fitur dan Aspek|Fetch API|jQuery|
|---|---|---|
|Kebutuhan Tambahan|Tidak memerlukan pustaka tambahan.|Memerlukan pustaka jQuery.|
|Kompatibilitas dengan Browser|Mendukung sebagian besar browser modern.|Mendukung sebagian besar browser modern.|
|Kemampuan Promises|Menggunakan Promise, yang memungkinkan penggunaan async/await.|Menggunakan callback.|
|Kode yang Lebih Ringkas|Membutuhkan kode yang lebih banyak dan terstruktur saat menangani respons HTTP.|Dapat menggunakan shorthand method untuk melakukan AJAX dengan kode yang lebih ringkas.|
|Pembuatan Permintaan HTTP|Memerlukan sedikit lebih banyak kode untuk membuat permintaan HTTP, termasuk menangani respons HTTP.|Mudah digunakan dengan metode `.ajax()` yang telah ada.|
|Error Handling|Error handling memerlukan penanganan khusus dengan try-catch atau `.catch()` dalam Promise.|Mudah mengatasi kesalahan dengan metode `.fail()` atau callback error.|
|Kelebihan|Lebih modern dan mendukung async/await. Lebih fleksibel untuk penggunaan terstruktur.|Lebih mudah digunakan untuk tugas sederhana dan dalam proyek-proyek yang lebih lama.|
|Kerumitan|Lebih cocok untuk pengembangan aplikasi besar dan kompleks.|Lebih sederhana untuk pengembangan aplikasi kecil hingga menengah.|

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
   + Untuk mengimplementasikan AJAX GET, pertama saya membuat fungsi di `views.py` dengan nama `get_item_ajax`, implementasikan dengan cara seperti ini: <br>
   ```python
   def get_item_ajax(request):
    if request.method == 'GET':
        product_item = Item.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', product_item))
    
    return HttpResponseNotFound()
   ```
   + Setelah itu sambungkan ke urls, lalu buat juga script di `main.html` untuk mengambil itemnya. <br>
   ```javascript
   <script>
      async function getItems() {
       return fetch("{% url 'main:get_item_ajax' %}").then((res) => res.json())
      }
      async function refreshItems() {
       document.getElementById("item_table").innerHTML = ""
       const items = await getItems()
       let htmlString = `<div class="card-container">`
       items.forEach((item, index) => {
        const isLastItem = index === items.length - 1;
        const cardClass = isLastItem ? 'card last-item' : 'card';
        htmlString += `\n
        <div class="${cardClass}" style="width: 18rem;">
          <div class="card-body">
            <div class="item-name">
              <div class="left-content">
                <h5 class="card-title">${item.fields.name} | ${item.fields.category}</h5>
              </div>
              <div class="right-content">
                <a href="delete-item/${item.pk}/">
                  <img src="{% static 'icon/delete_icon.png' %}" alt="Delete">
                </a>
              </div>
            </div>
            <h6 class="card-subtitle mb-2 text-body-secondary">${item.fields.amount} | Rp${item.fields.price}</h6>
            <p class="card-text">${item.fields.description}</p>
            <div class="button-wrap">
              <a href="decrement-item/${item.pk}/"><button type="button" class="btn btn-outline-primary">-</button></a>
              <a href="edit-item/${item.pk}/"><button type="button" class="btn btn-outline-primary">Edit</button></a>
              <a href="increment-item/${item.pk}/"><button type="button" class="btn btn-outline-primary">+</button></a>
            </div>
          </div>
        </div>` 
       })
       htmlString += `</div>`
       
       document.getElementById("item_table").innerHTML = htmlString
     }

     refreshItems()
   </script>
   ```
   + Untuk mengimplementasikan AJAX POST, buat juga fungsi di `views.py` dengan nama `create-ajax`, implementasikan dengan cara seperti ini: <br>
   ```python
   @csrf_exempt
   def add_item_ajax(request):
       if request.method == 'POST':
           name = request.POST.get("name")
           amount = request.POST.get("amount")
           description = request.POST.get("description")
           price = request.POST.get("price")
           category = request.POST.get("category")
           user = request.user
   
           new_product = Item(name=name, amount=amount, description=description, price=price, category=category, user=user)
           new_product.save()
   
           return HttpResponse(b"CREATED", status=201)
       return HttpResponseNotFound()
   ```
   + Setelah itu sambungkan ke urls, lalu buat tambahkan function di script pada `main.html` untuk menambah item. <br>
   ```javascript
   <script>
      ...
      function addItems() {
         fetch("{% url 'main:create_ajax' %}", {
             method: "POST",
             body: new FormData(document.querySelector('#form'))
         }).then(refreshItems)
   
         document.getElementById("form").reset()
         return false
      }
      document.getElementById("button_add").onclick = addItems
   </script>
   ```
   + Setelah itu tambahkan tombol untuk memunculkan modal yang digunakan untuk menambahkan item, tambahkan pada `main.html` <br>
   ```html
   <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" style="margin-right: 5px;">Add Item by AJAX</button>
   <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
     <div class="modal-dialog">
       <div class="modal-content">
           <div class="modal-header">
               <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
               <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
           </div>
           <div class="modal-body">
             <form id="form" onsubmit="return false;">
               {% csrf_token %}
               <div class="mb-3">
                 <label for="name" class="col-form-label">Name:</label>
                 <input type="text" class="form-control" id="name" name="name"></input>
               </div>
               <div class="mb-3">
                 <label for="amount" class="col-form-label">Amount:</label>
                 <input type="number" class="form-control" id="amount" name="amount"></input>
               </div>
               <div class="mb-3">
                 <label for="price" class="col-form-label">Price:</label>
                 <input type="number" class="form-control" id="price" name="price"></input>
               </div>
               <div class="mb-3">
                 <label for="description" class="col-form-label">Description:</label>
                 <textarea class="form-control" id="description" name="description"></textarea>
               </div>
               <div class="mb-3">
                 <label for="category" class="col-form-label">Category:</label>
                 <input type="text" class="form-control" id="category" name="category"></input>
               </div>
             </form>
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
         </div>
       </div>
     </div>
   </div>
   ```
   + Langkah terakhir lakukanlan `python manage.py collectstatic` untuk mengumpulkan seluruh file static yang ada di project.
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
9. [Django UserCreationForm](https://www.javatpoint.com/django-usercreationform "javaTpoint")
10. [User authentication in Django](https://docs.djangoproject.com/en/4.2/topics/auth/ "Django Documentation")
11. [What are Cookies?](https://www.kaspersky.com/resource-center/definitions/cookies "Kapersky")
12. [Django Cookies](https://www.javatpoint.com/django-cookie "javaTpoint")
13. [What Are Cookies & How Do They Work?](https://blog.sucuri.net/2023/01/what-are-cookies-a-short-guide-to-managing-your-online-privacy.html "Sucuri blog")
14. [CSS Selector](https://www.w3schools.com/css/css_selectors.asp "W3Schools")
15. [HTML5 - Tags Reference](https://www.tutorialspoint.com/html5/html5_tags.htm "TutorialsPoint")
16. [Tailwind CSS vs. Bootstrap: Who is More Relevant in the Current Scenario](https://www.zenesys.com/tailwind-css-vs-bootstrap "ZENESYS")
