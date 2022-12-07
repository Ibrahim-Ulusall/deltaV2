from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def login_request(request):
    # Dashboard'a yönlendir.
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/index.html',{
                'hata':'Kullanıcı adi veya parola hatalı!'
            })
    
    return render(request,'accounts/index.html')    

def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re-password']

        userInput = [firstname,lastname,username,email,password,re_password]

        for userinput in userInput:
            if userinput == '':
                return render(request,'accounts/register.html',{
                    'ValueError':'Tüm Alanlar Doldurulmalıdır.'
                })
        # if '@gmail.com' not in email or '@hotmail.com' not in email:
        #     return render(request,'accounts/register.html',{
        #         'FormatError':'Lütfen İstenilen Formatta mail adresi giriniz.'
        #     })    
        if password != re_password:
            return render(request,'accounts/register.html',{
                'EqualsError':'Parolalar Uyuşmuyor.'
            })
        else:
            if User.objects.filter(username=username).exists():
                return render(request,'accounts/register.html',{
                    'username_used_error':'Kullanıcı Adı Kullanılıyor.'
                })
            elif User.objects.filter(email=email).exists():
                return render(request,'accounts/register.html',{
                    'email_used_error':'Email Adresi Kullanılıyor.'
                })
            else:
                user = User.objects.create_user(
                    first_name = firstname,
                    last_name = lastname,
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
                return redirect('home')

    return render(request,'accounts/register.html')

def logout_request(request):
    logout(request)
    return redirect('login')