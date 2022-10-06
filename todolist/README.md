# Tugas 5 PBP Semester Ganjil 2022/2023
### By Jeremy Alva Prathama, NPM 2106640354, kelas B


## 1. Informasi Proyek
Pada Tugas 5 PBP ini, saya menambahkan styling menggunakan TailwindCSS pada aplikasi Todolist yang telah dibuat sebelumnya. Lebih lengkapnya, dapat dilihat di link berikut:

[Cek laman app tersebut di link berikut!](https://pbp-assignment-02.herokuapp.com/todolist)

Terima kasih.


## 2. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
    Inline CSS: menambahkan styling langsung dalam HTML tag menggunakan style attribute. Kelebihan dari metode ini adalah kita dapat menambahkan styling dengan cepat karena tinggal menambahkan attribute pada tag HTML. Selain itu, kita tidak perlu membuat file terpisah untuk melakukan styling. Namun kekurangannya adalah, cara ini tidak efektif untuk elemen yang membutuhkan styling rumit, karena kode HTMK akan menjadi berantakan akibat bercampur dengan CSS.

    Internal CSS: menambahkan styling di file HTML namun pada tag `<style>` yang diletakkan dalam section `<head>` HTML. Kelebihan dari metode ini adalah dapat membuat styling lebih rapih dibanding inline CSS, karena semua styling akan masuk di satu bagian yang sama. Selain itu, kita dapat menggunakan class dan id selector untuk memilih elemen HTML yang ingin di style. Kekurangannya adalah banyaknya kode pada suatu file HTML dapat membuat halaman kita memiliki loading yang lebih lama.

    External CSS: menambahkan styling di file .css diluar file HTML awal. Kelebihan dari metode ini adalah ia efektif untuk membuat styling yang rumit, karena kode styling dapat dipisahkan sesuai urutan logisnya. Selain itu, kita dapat menggunakan file .css yang sama untuk menerapkan styling ke HTML page berbeda. Kekurangan dari metode ini adalah halaman harus menunggu sampai external css dimuat agar bisa menampilkan styling.

## 3. Jelaskan tag HTML5 yang kamu ketahui.
    html = menggambarkan root dari dokumen HTML, container untuk semua HTML element

    head = container untuk metadata

    body = mendefinisikan body dari dokumen HTML (mengandung content HTML)

    div = mendefinisikan suatu division atau bagian dari dokumen HTML

    button = mendefinisikan suatu tombol yang dapat di klik

    p = mendefinisikan suatu paragraf

    h1, h2, ... , h6 = mendefinisikan HTML headings sesuai prioritas

    a = mendefinisikan suatu hyperlink

    table = mendefinisikan tabel HTML, dapat mengandung 1 atau lebih elemen th, tr, td

    th = mendefinisikan heading dari table

    tr = mendefinisikan row atau baris dari table

    td = mendefinisikan cell atau data dari table


## 4. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    .className = memilih semua elemen dengan class className

    #idName = memilih semua elemen dengan id idName

    * = memilih semua elemen

    element (misal div {...}) = memilih semua elemen yang bertipe element

    element.class = memilih semua elemen HTML "element" yang memiliki class "class"

    element1 > element2 = memilih semua element2 yang memiliki parent element1

    :active = memilih link yang aktif

    :focus = memilih input elemen yang sedang berstatus fokus

    :hover = memilih item yang sedang di hover mouse


## 5. Cara mengimplementasi checklist diatas
    1. Install django-tailwind dengan mengikuti instruksi di [dokumentasi](https://django-tailwind.readthedocs.io/en/latest/installation.html)

    2. Tailwind menggunakan utility-first approach, pengguna hanya perlu memasukkan class yang ada di dokumentasi Tailwind untuk memanfaatkan styling yang ada. Tambahkan styling yang sesuai untuk halaman-halaman di aplikasi todolist dengan menggunakan referensi [dokumentasi TailwindCSS](https://tailwindcss.com/)

    3. Gunakan class="flex" untuk membuat halaman menjadi responsif dengan memanfaatkan flexbox

    4. Gunakan classes seperti "text-{color}-{size}", "font-{style}", dll untuk mengatur styling elemen. Referensikan dokumentasi untuk menambahkan styling seperti card, button, dan lain-lain.

    5. Setelah menambahkan styling yang diinginkan, lakukan git add, commit, dan push ke repository remote untuk menyimpan hasil pekerjaan.

...


## Credits

Laman template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.