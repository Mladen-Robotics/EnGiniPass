from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login,logout

from datetime import datetime
import base64

from user_authentication.models import UserProfileModel


def LoginView(request):
    context = {"user_exists": True}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("User is authenticated!")
            login(request,user)
            return redirect(reverse("password_dashboard:password_dashboard"))
        else:
            print("User is not authenticated!")
            context["user_exists"] = False
    if request.user.is_authenticated == True:
        print("User HAS BEEN authenticated!")
        return redirect(reverse("password_dashboard:password_dashboard"))

    return render(request,"user_authentication/login/login.html",context)

def SignupView(request):
    context = {"error":None}
    if request.method == 'POST':
        print("HAHA")
        username = request.POST.get('signup_username')
        password = request.POST.get('signup_password')
        name = request.POST.get('signup_name')
        surname = request.POST.get('signup_surname')
        day = request.POST.get('signup_day')
        month = request.POST.get('signup_month')
        year = request.POST.get('signup_year')
        returnStatus = StoreUser(username,password,name,surname,day,month,year)
        if returnStatus[0] == True:
            # context["successful_signup"] = True
            logout(request)
            login(request,returnStatus[2])
            return redirect(reverse("password_dashboard:password_dashboard"))

        else:
            print(returnStatus[1])
            context["error"] = returnStatus[1]



    return render(request,"user_authentication/sign_up/signup.html",context)

def HomePageView(request):
    return render(request,"user_authentication/HomePage/home.html")


def StoreUser(username,password,name,surname,day,month,year):
    MONTHS = {
        "Jan." : 1,
        "Feb." : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "Aug." : 8,
        "Sept." : 9,
        "Oct." : 10,
        "Nov.": 11,
        "Dec." : 12
    }
    
    try:
        user = User.objects.get(username=username)
        print("User does exist")
        return (False,"Username already exists!")
        
    except User.DoesNotExist:
        print("User does not exist!")
        users = User.objects.all()
        new_user = None
        for user in users:
            if user.check_password(password):
                print("Password exists!")
                return (False,"Password is  already taken!")
            else:
                print("Password does not exist!")
                if day != "":
                    month_number = MONTHS.get(month)
                    birth_date = datetime(int(year),month_number,int(day))
                    new_profile = UserProfileModel(user=new_user, date_of_birth=birth_date)
                    print(birth_date)
                else:
                    print("Date wasn't provided!")
                # IMPORTANT !!!!!!!!!!!
                # b64_password = base64.b64encode(password.encode('ascii')).decode('ascii')
                # print('b64 encoded:',b64_password)
                # b64_decoded_pass = base64.b64decode(b64_password.encode('ascii')).decode('ascii')
                # print("Decoded b64:",b64_decoded_pass)
                new_user = User.objects.create_user(username=username,password=password,first_name=name,last_name=surname)
                new_profile = UserProfileModel(user=new_user)
                new_profile.save()
                return (True,"",new_user)
        # if user.check_password(password) == False:
        #     print("Password does not exist")
        #     if day == "":
        #         
        #     else:
        #         print("Date wasn't provided")
        # else:
        #     print("Password does exist")


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('login'))