from django.shortcuts import render, redirect
from .models import Usern
from adhaar.otp import generateOTP
from django.http import HttpResponse

ONE_TIME_PASSWORD = 0
hacker = 0

def login(request, *args, **kwargs):
    global ONE_TIME_PASSWORD, hacker

    ONE_TIME_PASSWORD = generateOTP()
    i = 0
    count = 0
    if request.method == 'POST':
        a_login = request.POST.get('a_login', False)
        print(a_login)
        for obj in Usern.objects.all():
            count = count + 1
            b_login = str(obj.adhaar_number)
            print(b_login)
            if str(a_login) == str(b_login):
                i = 1
                break
        if i == 1:
            hacker = 0
            print('Found')
            print(str(ONE_TIME_PASSWORD))
            # my_context = {
                # "phone_number": Usern.objects.get(id=count).phone_number,
                # "count": count
                # "phone_number": obj.phone_number

            # }
            return redirect('http://127.0.0.1:8000/adhaar/otp')
    else:
            print('Not Found')
    return render(request, 'adhaarlogin.html', {})

def otp(request, *args, **kwargs):
    global hacker
    print('reached otp function')
    # One = generateOTP()
    One = ONE_TIME_PASSWORD
    hacker=hacker+1
    print('no of times site hacked'+str(hacker))
    print('otp in the function is ' + str(One))
    if request.method == 'POST':
        otp = request.POST.get('otp', False)
        print('we wrote ' + str(otp))
        if str(One) == str(otp) and hacker <= 4:
            return redirect('http://127.0.0.1:8000/crime/welcome')
        if hacker > 3:
            return redirect('http://127.0.0.1:8000/adhaar/login')
    return render(request, 'otp.html')

def welcome(request):
    global hacker
    hacker = 0
    return render(request, 'welcome.html')

