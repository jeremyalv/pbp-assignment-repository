# Tugas 03 PBP Semester Ganjil 2022/2023
### By Jeremy Alva Prathama, NPM 2106640354, kelas B


## 1. Informasi Proyek
Dalam rangka memenuhi tugas 03 mata kuliah PBP, saya telah membuat halaman heroku yang mengimplementasikan model MVT dari framework Django serta menggunakan data delivery. Laman tersebut dapat dilihat dibawah:  

[Cek laman app tersebut di link berikut!](https://pbp-assignment-02.herokuapp.com/)

Terima kasih.


## 2. Perbedaan antara JSON, XML, HTML
JSON (JavaScript Object Notation) merupakan format *data interchange* yang tidak bergantung pada bahasa. JSON didasari oleh bahasa pemrogramman JavaScript. 

XML (Extensible Markup Language) digunakan untuk membuat halaman web dan aplikasi web.

HTML (Hypertext Markup Language) merupakan bahasa yang digunakan untuk membuat aplikasi web. HTML berguna untuk menunjukkan data. 

HTML berbeda dengan XML dalam aspek fungsionalitasnya. HTML berguna untuk menunjukkan data, sedangkan XML digunakan untuk memindahkan data. HTML bersifat statis sedangkan XML bersifat dinamis. JSON mirip dengan XML, dimana tujuannya adalah untuk memindahkan data. JSON kerap digunakan dalam membangun aplikasi berbasis web karena popularitas dari bahasa pemrograman seperti JavaScript.


## 3. Kenapa memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery agar data yang kita inginkan dapat diwujudkan dalam bentuk tampilan kepada user. Pertukaran data dari suatu platform ke platform lainnya dapat dipermudah dengan *data delivery*.


## 4. Pengimplementasian checklist diatas
1. Buatlah mywatchlist app
   ```python manage.py startapp mywatchlist```
2. Tambahkan mywatchlist ke settings.py
   ```
   INSTALLED_APPS = [
    ...
    'mywatchlist',
   ]
   ```
3. Tambahkan mywatchlist path ke project_django/urls.py
   ```
   urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
   ]
   ```
4. Buatlah model MyWatchList pada models.py
    ```
    class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
    ])
    release_date = models.CharField(max_length=10)
    review = models.TextField()
    ```
5. Lakukan migrasi data dengan ```python manage.py makemigrations``` serta migrasikan perubahan ke database dengan ```python manage.py migrate```
6. Buat sebuah JSON watchlist_data pada mywatchlist/fixtures dan isi dengan 10 obyek JSON yang anda inginkan.
7. Muat data pada tahap sebelumnya dengan ```python manage.py loaddata watchlist_data.json```
8. Import model pada views.py ```from mywatchlist.models import MyWatchList```
9. Tambahkan kode pada views.py untuk mengembalikan data dalam bentuk HTML/XML/JSON
   ```
   def retrieve_html(request):
    data_watchlist = MyWatchList.objects.all()
    response = {
        'mywatchlist': data_watchlist,
    }

    return render(request, "watchlist_html.html", response)

    def retrieve_xml(request):
        data = MyWatchList.objects.all()

        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def retrieve_json(request):
        data = MyWatchList.objects.all()

        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    # Retrieve by id
    def retrieve_html_by_id(request, id):
        data_watchlist = MyWatchList.objects.filter(pk=id)

        response = {
            'mywatchlist': data_watchlist,
        }

        return render(request, "watchlist_html.html", response)

    def retrieve_xml_by_id(request, id):
        data = MyWatchList.objects.filter(pk=id)

        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def retrieve_json_by_id(request, id):
        data = MyWatchList.objects.filter(pk=id)

        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
   
10. Buatlah file urls.py pada mywatchlist/
    ```
    from django.urls import path
    from mywatchlist.views import show_mywatchlist, retrieve_html, ...

    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_mywatchlist, name='show_mywatchlist'),
        path('html/', retrieve_html, name='retrieve_html'),
        path('xml/', retrieve_xml, name='retrieve_xml'),
        path('json/', retrieve_json, name='retrieve_json'),
        path('html/<int:id>', retrieve_html_by_id, name='retrieve_html_by_id'),
        path('xml/<int:id>', retrieve_xml_by_id, name='retrieve_xml_by_id'),
        path('json/<int:id>', retrieve_json_by_id, name='retrieve_json_by_id'),
    ]
    ```
11. Buatlah file HTML mywatchlist.html (home page) serta watchlist_html (HTML data page) untuk mendisplay data sesuai ketentuan.
12. Buatlah test cases test.py pada mywatchlist/
    ```
    from django.test import TestCase, Client
    from django.urls import reverse

    class MyWatchListTest(TestCase):
        def setUp(self):
            self.client = Client()
        def data_html_working(self):
            response = self.client.get(reverse('mywatchlist:retrieve_html'))
            self.assertEqual(response.status_code, 200)
        def data_xml_working(self):
            response = self.client.get(reverse('mywatchlist:retrieve_xml'))
            self.assertEqual(response.status_code, 200)
        def data_json_working(self):
            response = self.client.get(reverse('mywatchlist:retrieve_json'))
            self.assertEqual(response.status_code, 200)
    ```
13. Deploy data ke Heroku dengan melakukan push ke remote repository


## 5. Screenshot Postman


## Credits

Laman template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.