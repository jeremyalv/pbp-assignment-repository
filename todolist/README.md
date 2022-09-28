# Tugas 4 PBP Semester Ganjil 2022/2023
### By Jeremy Alva Prathama, NPM 2106640354, kelas B


## 1. Informasi Proyek
Pada Tugas 4 PBP ini, saya membuat aplikasi Todo list dengan fitur autentikasi, serta penambahan dan penghapusan data Task. Lebih lengkapnya, dapat dilihat di link berikut:

[Cek laman app tersebut di link berikut!](https://pbp-assignment-02.herokuapp.com/todolist)

Terima kasih.


## 2.  Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} berguna untuk melindungi situs terhadap Cross Site Request Forgery attack, suatu jenis kejahatan digital. csrf_token biasa muncul pada form pada template, gunanya adalah mencegah penyerang csrf untuk melakukan request dan pengguna dapat menggunakan website dengan aman. Bila tidak ada csrf_token, penyerang dapat dengan mudah mendapatkan csrf token dan menyerang pengguna.


## 3. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Untuk membuat form secara manual, kita dapat menggunakan tags seperti `<form>`, dan `<input>` untuk menerima input user. Selain itu, kita dapat menentukan method HTTP yang digunakan serta menambahkan label dan elemen HTML lainnya. Keuntungan dari membuat form secara manual adalah developer dapat membuat customization sendiri.


## 4.  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Pengguna melakukan pengiriman data form ke server lewat POST request. 
2. Request POST akan diterima oleh views yang akan berinteraksi dengan models, misalnya dengan menambahkan atau menghapus data. 
3. Setelah data di proses, django akan mengembalikan data yang diinginkan dengan melakukan redirect ke templates yang sudah memuat data terbaru.


## 5. Pengimplementasian checklist tugas
1. Buat aplikasi baru bernama todolist 
```
python manage.py startapp todolist
```

2. Tambahkan todolist ke INSTALLED_APPS di folder project_django
```
INSTALLED_APPS = [
    ...,
    'todolist',
]
```

3. Buat models.py pada aplikasi todolist
```
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

4. Lakukan migrasi models serta registrasi pada admin.py
```
python manage.py makemigrations
python manage.py migrate
```

Pada todolist/admin.py

```
from django.contrib import admin
from todolist.models import Task

admin.site.register(Task)
```

5. Buat views.py untuk mengatur jalannya aplikasi
Buatlah views berikut
- show_todolist untuk menunjukkan todolist utama
- register untuk memungkinkan registrasi user
- login_user untuk memungkinkan user login
- logout_user untuk memungkinkan user logout
- create_task untuk membuat suatu object Task dan menyimpannya di database
- delete_task untuk menerima suatu Task dengan id tertentu dan menghapusnya dari database
- toggle_task_status untuk mengubah status task 
  
6. Buatlah templates berupa halaman HTML
Templates yang perlu dibuat sebagai berikut:
- todolist.html
- login.html
- register.html
- create_task.html


7. Tambahkan routing pada aplikasi todolist
Di todolist/urls.py, tambahkan
```
from django.urls import path
from todolist.views import delete_task, show_todolist, register, login_user, logout_user, create_task, toggle_task_status, delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('toggle-status/<int:id>', toggle_task_status, name='toggle_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]
```


8. Daftarkan todolist pada urls.py project_django
Pada project_django/urls.py, tambahkan
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
    path('todolist/', include('todolist.urls')),
]
```

...


## Credits

Laman template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.