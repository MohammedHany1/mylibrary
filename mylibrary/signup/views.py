from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm, UpdateForm, BookForm, BorrowForm
from .models import Book,Borrow
from django.views.generic import ListView
from signup.Borrowingfunctions.availability import checkavailability
from django.contrib.auth.decorators import login_required

def index(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('userType') == "admin":
                user = get_user_model()
                user = user.objects.get(username=request.POST.get('username'))
                user.is_staff = True
                user.is_admin = True
                user.is_superuser = True
                user.save()
            
        return redirect('signin')

    return render(request, 'signup/index.html', {'form': form})



def home(request):
    return render(request, 'signup/home.html')

def aboutus(request):
    return render(request, 'signup/aboutus.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser == True:
                return redirect('adminhome')
            else:
                return redirect('student')
        else:
            messages.error(request, 'Username or Password is Incorrect')
    return render(request, 'signup/login.html', {})


@login_required(login_url='/login/')
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if request.user.is_superuser == True:
                return redirect('adminhome')
            else:
                return redirect('student')
    else:
        form = UpdateForm(instance=request.user)
        args = {'form': form}
        return render(request, 'signup/update.html', args)


@login_required(login_url='/login/')
def updatepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('update')
    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'signup/updatepassword.html', args)


@login_required(login_url='/login/')
def student(request):
    return render(request, 'signup/student_home.html')


@login_required(login_url='/login/')
def adminhome(request):
    return render(request, 'signup/admin_home.html')


@login_required(login_url='/login/')
def logoutt(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/login/')
def browse(request):
    context= {
        'books':Book.objects.all().order_by('title'),
    }
    return render(request, 'signup/browse.html',context)


@login_required(login_url='/login/')
def addbook(request):
    if request.method == 'POST':
        add= BookForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('browse')
    context= {
        'books':Book.objects.all(),
        'form': BookForm()
    }
    return render(request, 'signup/addbook.html',context)


@login_required(login_url='/login/')   
def changebook(request, id):
    bookId= Book.objects.get(id=id)
    if request.method == 'POST':
        bookSave= BookForm(request.POST, request.FILES, instance=bookId)
        if bookSave.is_valid():
            bookSave.save()
            return redirect('browse')
    else:
        bookSave= BookForm(instance=bookId)
    context={
        'form':bookSave,
    }      
    return render(request, 'signup/changebook.html',context)


@login_required(login_url='/login/')
def borrowbook(request):
    model=Borrow
    context= {
        'books':model.objects.all().order_by('book'),
        'book':Book.objects.all(),
    }
    return render(request, 'signup/borrowbook.html',context)


@login_required(login_url='/login/')
def rentbook(request, id):
    model=Borrow
    book=Book
    booknum= book.objects.get(id=id)
    bookex=booknum
    if request.method == 'POST':
        add= BorrowForm(request.POST)
        if add.is_valid():
            add=add.save(commit=False)
            add.user=request.user
            add.book=bookex
            bookav=bookex
            add.save()
            bookav.available=False
            bookav.save()
            return redirect('borrowbook')
    context= {
        'books':model.objects.all().order_by('book'),
        'form': BorrowForm,
    }
    return render(request, 'signup/rentbook.html',context)


@login_required(login_url='/login/')   
def extendbook(request, id):
    model=Borrow
    booknum= Borrow.objects.get(id=id)
    bookex=booknum.book
    if request.method == 'POST':
        bookSave= BorrowForm(request.POST, instance=booknum)
        if bookSave.is_valid():
            bookSave=bookSave.save(commit=False)
            bookSave.user=request.user
            booknum.book=bookex
            bookSave.save()
            return redirect('borrowbook')
    else:
        bookSave= BorrowForm(instance=booknum)
        
    context= {
        'books':model.objects.all().order_by('book'),
        'form': BorrowForm,
    }      
    return render(request, 'signup/extendbook.html',context)


@login_required(login_url='/login/')   
def returnbook(request, id):
    model=Borrow
    book=Book
    booknum= Borrow.objects.get(id=id)
    bookdel=booknum
    bookex=booknum.book
    if request.method == 'POST':
        bookSave= BorrowForm(request.POST, instance=booknum)
        if bookSave.is_valid():
            bookSave=bookSave.save(commit=False)
            bookSave.user=request.user
            booknum.book=bookex
            bookex.available=True
            Borrow.objects.filter(book=bookex).delete()
            bookex.save()
            return redirect('browse')
    else:
        bookSave= BorrowForm(instance=booknum)
        
    context= {
        'books':model.objects.all().order_by('book'),
        'form': BorrowForm,
        'book': bookex
    }      
    return render(request, 'signup/returnbook.html',context)

