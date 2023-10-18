from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import Todo_list
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'todo_app/base.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken!')
                return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                 messages.info(request,'Email is already registered!')
                 return redirect('signup')
            else:
                if password == password2:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
                else:
                    messages.info(request,'Password does not match!')
                    return redirect('signup')
            
    return render(request, 'todo_app/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            def login(request):
                auth_login(request, user)
            login(request)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
        
    return render(request, 'todo_app/login.html')




def log_out(request):
    logout(request)
    return redirect('/')




@login_required(login_url='login')
def todo_list(request):
    todo_list = Todo_list.objects.all()
    context = {
        'todo_lists': todo_list,
    }

    return render(request, 'todo_app/todo_list.html', context=context)



@login_required(login_url='login')
def addtask(request):
    if request.method == 'POST':
        tasks = request.POST['task']
        start_time = request.POST['start_time']
        completed = request.POST['completed']
        if completed =='1':
            todo = Todo_list.objects.create(tasks=tasks, start_time=start_time, completed=True, person=request.user)
            todo.save()
            return redirect('todo_list')
        elif completed == '0':
            todo = Todo_list.objects.create(tasks=tasks, start_time=start_time, completed=False, person=request.user)
            todo.save()
            return redirect('todo_list')
        else:
            return redirect('addtask')
    
    
    return render(request, 'todo_app/addtask.html')
        

@login_required(login_url='login')
def edit(request, pk):
    task = Todo_list.objects.get(id=pk)
    context = {
        'task' : task
    }
    if request.method == 'POST':
        completed = request.POST['completed']
        if completed =='1':
            task.tasks = request.POST['task']
            task.start_time = request.POST['start_time']
            task.completed = True
            task.person = request.user
            task.save()
            
            return redirect('todo_list')
           
        elif completed == '0':
            task.tasks = request.POST['task']
            task.start_time = request.POST['start_time']
            task.completed = False
            task.person = request.user
            task.save()
            
            return redirect('todo_list')
        
        else:
            return redirect('edit')
    

    return render(request, 'todo_app/edit.html', context=context)

@login_required(login_url='login')
def viewtask(request, pk):
    task = Todo_list.objects.get(id=pk)
    context = {
        'task' : task
    }

    return render(request, 'todo_app/viewtask.html', context=context)

@login_required(login_url='login')
def delete(request, pk):
    task = Todo_list.objects.get(id=pk)
    context = {
        'task' : task
    }
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/delete.html', context=context)


@login_required(login_url='login')
def completed(request):
    todo_list = Todo_list.objects.all()
    list_len = len(todo_list)
    context = {
        'todo_lists': todo_list,
        'length': list_len,
    }

    return render(request, 'todo_app/completed.html', context=context)