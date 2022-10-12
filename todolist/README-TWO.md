# Tugas 6 PBP Semester Ganjil 2022/2023
### By Jeremy Alva Prathama, NPM 2106640354, kelas B
<hr>

## 1. Informasi Proyek
Pada Tugas 6 PBP ini, saya menambahkan fitur AJAX menggunakan jQuery untuk menggantikan operasi dari situs yang sebelumnya.

[Cek laman app tersebut di link berikut!](https://pbp-assignment-02.herokuapp.com/todolist)

Terima kasih.
<hr>

## 2. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming merupakan metode pemrograman yang memastikan bahwa ketika suatu operasi sedang berjalan, maka program tidak dapat melakukan operasi lain. Ini berbeda dengan asynchronous programming yang memungkinkan program untuk mengeksekusi lebih dari satu operasi bersamaan.

Sync programming bersifat single-threaded, sedangkan async programming bersifat multi-threaded.

Sync programming bersifat blocking (misal server hanya bisa menerima satu request), sedangkan async programming bersifat sebaliknya atau non-blocking.

Async programming dapat mempercepat jalannya program karena lebih dari satu operasi yang dijalankan pada suatu waktu.
<hr>

## 3. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming merupakan paradigma pemrograman dimana kode dibuat untuk merespon ke _events_. Events dapat di trigger oleh user seperti misalnya dengan menklik suatu tombol.

Program yang dibuat untuk merespon suatu event disebut dengan _event handlers_.

Contoh penerapan pada tugas kali ini adalah penggunaan method addEventListener yang dikaitkan dengan suatu DOM element. Method ini memungkinkan komponen DOM untuk bereaksi terhadap tindakan user.
<hr>

## 4. Jelaskan penerapan asynchronous programming pada AJAX.
Pada AJAX, kita menggunakan async programming ketika kita ingin program tetap berjalan meski sedang menunggu hasil suatu operasi. Contoh untuk penggunaan ini adalah ketika kita memanggil API yang membutuhkan waktu untuk mengembalikan sebuah response. Dalam project ini, API tersebut disimulasikan dengan menggunakan url khusus yang mengandung data JSON. 

Penggunaan AJAX memungkinkan program kita tetap berjalan dan membuat halaman termuat lebih cepat. Hal ini akan meningkatkan _user experience_ dari aplikasi kita. 
<hr>

## 5. Cara mengimplementasi checklist diatas
1. Buat view baru yang akan mengembalikan data dalam bentuk JSON

    ```
    @login_required(login_url='/todolist/login')
    def get_json(request):
        data = Task.objects.filter(user=request.user)

        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

2. Buat path /todolist/json/ yang mengarah ke view sebelumnya
    ```
    urlpatterns = [
        ...
        path('json/', get_json, name='get_json'),
    ]
    ```

3. Lakukan pengambilan task menggunakan ajax get. Disini, saya membuat 2 bagian fungsi, yakni createSection dan loadTaskList (karena _nature_ dari program saya membutuhkan perhitungan jumlah task terlebih dahulu)
    ```
    function createSections() {
        $.getJSON('/todolist/json/', function(data) {
            /* Control program section logic */
            var activeAmount = 0;
            var finishedAmount = 0;
    
            for (var i = 0; i < data.length; i++) {
                if (data[i].fields.is_finished) {
                    finishedAmount++;
                } else {
                    activeAmount++;
                }
            }

            if (activeAmount == 0 && finishedAmount == 0 && $("#nty").length == 0) {
                $("#top-section").append(`<p id="nty" class="text-2xl text-green-500 font-bold pt-4">No tasks yet. Start adding!</p>`);
            } else {
                if ($("#top-section").length > 0) {
                    $("#top-section").empty();
                }
                if (activeAmount > 0 && $("#section-active-task").length == 0) {

                    $("#todolist").append(
                        `<div id="section-active-task" class="flex flex-col justify-center items-center">
                            <div class="text-3xl">Active Tasks</div>
                            <div class="text-xl pb-4 pt-2 px-2">Let's do this! 
                                <span class="text-gray-500 font-bold">
                                    ${activeAmount}
                                </span> task left.
                            </div>
                        </div>      
                        
                        <div id="active-tasks" class="flex flex-col flex-wrap items-stretch pb-4">
                        </div>`
                    );
                } 
    
                if (finishedAmount > 0 && $("#section-finished-task").length == 0) {
                    $("#todolist").append(
                        `<div id="section-finished-task" class="pb-4 w-6/12">
                            <div class="flex flex-col justify-center items-center">
                                <div class="text-3xl">Finished Tasks</div>
                                <div class="text-xl pb-4 pt-2 px-2">Congrats! You have finished
                                    <span class="text-green-500 font-bold">
                                        ${finishedAmount}
                                    </span> tasks.
                                </div>
                            </div>      
                            
                            <div id="finished-tasks" class="flex flex-col flex-wrap items-stretch">  
                            </div>
                        </div>`
                    );
                }
            }
        });
    }
    ```

    ```
    function loadTasksList() {
        $.getJSON('/todolist/json/', function(data) {     
            /* Display task cards */
            
            // Empty the current task containers
            $('#active-tasks').empty();
            $('#finished-tasks').empty();
            
            for (var i = 0; i < data.length; i++) {
                var isFinished = data[i].fields.is_finished;
                var taskItem = `<div class="flex flex-col grow p-6 m-2 min-w-min max-w-sm bg-white rounded-lg border border-gray-200 shadow-md w-6/12 hover:bg-gray-200 hover:shadow-xl">
                        <p class="mb-2 text-md font-bold tracking-tight text-black-900">${data[i].fields.title}</p>
    
                        ${isFinished ? 
                            `<p class="mb-3 text-sm font-bold text-green-500">
                                Completed
                            </p>`
                            :
                            `<p class="mb-3 text-sm font-bold text-gray-500">
                                Active
                            </p>`
                        }
                        </p>
                        <p class="mb-3 text-sm font-normal text-gray-700">
                            ${data[i].fields.date}
                        </p>
                        <p class="mb-3 text-sm font-normal text-gray-700">
                            ${data[i].fields.description}
                        </p>
                        <div class="flex flex-row last:mt-auto last:pt-4">
                            ${isFinished ?
                                `<button type="submit" class="text-gray-700 hover:text-white border 
                                    border-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300
                                    font-medium rounded text-sm px-2 py-1
                                    text-center mr-1 mb-1 dark:border-gray-500 dark:text-gray-500 
                                    dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-800">
                                        <a href="/todolist/toggle-status/${data[i].pk}">
                                            Unfinish
                                        </a>
                                </button>`
                                :
                                `<button type="submit" class="text-green-700 hover:text-white border 
                                border-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300
                                font-medium rounded text-sm px-2 py-1
                                text-center mr-1 mb-1 dark:border-green-500 dark:text-green-500 
                                dark:hover:text-white dark:hover:bg-green-600 dark:focus:ring-green-800">
                                    <a href="/todolist/toggle-status/${data[i].pk}">
                                        Finish
                                    </a>
                                </button>`
                            }
                            <button type="submit" class="text-rose-700 hover:text-white border 
                            border-rose-700 hover:bg-rose-800 focus:ring-4 focus:outline-none focus:ring-rose-300
                            font-medium rounded text-sm px-2 py-1 
                            text-center mr-1 mb-1 dark:border-rose-500 dark:text-rose-500 
                            dark:hover:text-white dark:hover:bg-rose-600 dark:focus:ring-rose-800">
                                <a href="/todolist/delete/${data[i].pk}">
                                    Delete
                                </a>
                            </button>
                        </div>
                    </div>`;
                
                if (isFinished) {
                    $("#finished-tasks").append(taskItem);
                } else {
                    $("#active-tasks").append(taskItem);
                }
            }
        });
    }
    ```
4. Buat tombol Add Task yang akan membuka modal
    ```
    <button 
        id="add-task"
        data-modal-target="#modal"
        type="button"
        class="text-white bg-green-700 
        hover:bg-green-800 focus:ring-4 focus:ring-green-300 
        font-medium rounded-lg text-sm py-2 px-2
        dark:bg-green-600 dark:hover:bg-green-700 
        focus:outline-none dark:focus:ring-green-800">
        Add Task
    </button>
    ```

6. Menambahkan overlay dan modal pada kode HTML
    ```
    <div id="overlay" class=""></div>
    ```

    ```
    div id="modal" class="px-4 py-2">
            <div id="modal-header" class="flex flex-row items-center py-2 border-b-4 border-solid border-black">
                <div id="modal-header-title" class="text-xl font-bold text-green-700">
                    Fill Task Details
                </div>
                <button id="modal-close-button" style="margin-left: auto;" data-close-button
                    class="cursor-pointer border-none outline-none bg-none text-3xl font-bold text-rose-700">
                    &times;
                </button>
            </div>
            <div id="modal-body" class="flex flex-col py-2">
                <div class="flex flex-col pb-4">
                    <label class="text-lg pb-2">Title</label>
                    <input required id="title-input" type="text" name="title" placeholder="Enter title" 
                    class="border-1 rounded focus:border-2 focus:border-green-700 invalid:border-rose-500">
                </div>
                <div class="flex flex-col">
                    <label class="text-lg pb-2">Description</label>
                    <input required id="description-input" type="text" name="description" placeholder="Enter description" 
                                    class="border-1 rounded focus:border-2 focus:border-green-700 mb-2 invalid:border-rose-500">
                </div>
                <div id="modal-cta" class="flex flex-col justify-center items-center">
                    <button id="modal-add-task" type="submit" class="text-white bg-green-700 
                    hover:bg-green-800 focus:ring-4 focus:ring-green-300 
                    font-medium rounded-lg text-sm px-5 py-2.5 mr-2 
                    mb-2 dark:bg-green-600 dark:hover:bg-green-700 
                    focus:outline-none dark:focus:ring-green-800
                    my-4">
                        Add Task
                    </button>
                </div>
            </div>
        </div> 
    ```

7. Menambahkan external styling pada modal dan overlay untuk mengkustomisasi komponen
    ```
    <style>
        #overlay {
            position: fixed; 
            opacity: 0;
            top: 0; 
            left: 0; 
            right: 0;
            bottom: 0;
            height: 100%; 
            width: 100%; 
            background-color: rgba(0,0,0,0.5);
            transition: 250ms ease-in-out;
            pointer-events: none;
        }
        #overlay.active {
            opacity: 1;
            pointer-events: all;
        }

        #modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            border: 1px solid black;
            border-radius: 6px;
            z-index: 10;
            background-color: white;
            width: 500px;
            max-width: 80%;
            transition: 250ms ease-in-out;
        }

        #modal.active {
            transform: translate(-50%, -50%) scale(1);
        }
    </style>
    ```

8. Menambahkan JavaScript untuk menjalankan fungsionalitas modal
    ```
    <script type="text/javascript">
    const modal = document.querySelectorAll('#modal');
    const openModalBtn = document.querySelectorAll("[data-modal-target]");
    const closeModalBtn = document.querySelectorAll("[data-close-button]");
    const overlay = document.getElementById("overlay");
    const modalAddTask = document.getElementById("modal-add-task");

    openModalBtn.forEach(button => {
        button.addEventListener('click', () => {
            const modal = document.querySelector(button.dataset.modalTarget);
            openModal(modal);
        });
    });

    closeModalBtn.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('#modal');
            closeModal(modal);
        });
    });
    
    overlay.addEventListener('click', () => {
        const modals = document.querySelectorAll('#modal.active');
        modals.forEach(modal => {
            closeModal(modal);
        });
    });
       
    // Helper functions
    function openModal(modal) {
        if (modal == null) {
            return;
        }

        modal.classList.add('active');
        overlay.classList.add('active');
    }

    function closeModal(modal) {
        if (modal == null) {
            return;
        }

        modal.classList.remove('active');
        overlay.classList.remove('active');
    }

    ...
    </script>
    ```

8. Membuat view baru untuk menambahkan task ke dalam database
    ```
    @login_required(login_url='/todolist/login/')
    @csrf_exempt
    def create_task_ajax(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = datetime.datetime.today()

            Task.objects.create(
                user = request.user,
                title = title,
                description = description,
                date = date,
                is_finished = False,
            )

            return HttpResponseRedirect(reverse("todolist:show_todolist"))
        else:
            messages.info(request, "INPUT SALAH")

        return (request, 'show_todolist.html')
    ```

9. Membuat path /todolist/add/ yang mengarah ke view sebelumnya
    ```
    urlpatterns = [
        ...
        path('add/', create_task_ajax, name='add'),
    ]
    ```

10. Hubungkan form yang sebelumnya dibuat dengan path add tadi
    ```
    modalAddTask.addEventListener('click', () => {
        const titleVal = $("#title-input").val();
        const descVal = $("#description-input").val();

        if (titleVal == "" || descVal == "") {
            if ($("#field-error").length >  0) {
                $("#field-error").remove()
            }
            $("#modal-cta").prepend(`<p id="field-error" class="text-lg py-2 font-bold text-green-500">Please fill the empty fields!</p>`);
        } else {
            $.post({
                url: 'add/',
                type: 'post',
                data: {
                    'title': titleVal,
                    'description': descVal,
                },
                success: [createSections, loadTasksList],
            });
        }
    })   
    ```

11. Tutup modal setelah task berhasil ditambahkan (tambahkan kode ini ada event lister dari addTask)
    ```
    // Clear input box values
    $("#title-input").val("")
    $("#description-input").val("")
    $("#field-error").remove()

    // Close modal
    const modal = modalAddTask.closest("#modal.active");
    closeModal(modal)
    ```

12. Lakukan refresh secara async dengan menambahkan kode berikut pada $.post()
    ```
    success: [createSections, loadTasksList],
    ```

...


## Credits

Laman template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.