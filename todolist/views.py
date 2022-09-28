import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.forms import TaskForm


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    active_tasks = Task.objects.filter(user=request.user, is_finished=False)
    finished_tasks = Task.objects.filter(user=request.user, is_finished=True)
    context = {
        'active_tasks': active_tasks,
        'finished_tasks': finished_tasks,
        'active_tasks_on': True if len(active_tasks) > 0 else False,
        'finished_tasks_on': True if len(finished_tasks) > 0 else False,
        'active_tasks_count': len(active_tasks),
        'finished_tasks_count': len(finished_tasks),
        'username': request.user.get_username(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('todolist:login')
        
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau password salah!')
    
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        # If request is POST, process the form data

        # Create form instance and populate with data from the request object
        form = TaskForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Create new Task item and add to database
            Task.objects.create(
                user = request.user,
                date = datetime.datetime.today(),
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                is_finished = False,
            )
            
            # Redirect to a Todolist app home URL
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        # If request is not POST, create a blank form
        form = TaskForm()

    context = {
        'form': form,
    } 
    
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login')
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()

    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login')
def toggle_task_status(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.is_finished = not task.is_finished
    task.save(update_fields=['is_finished'])

    return HttpResponseRedirect(reverse("todolist:show_todolist"))


