from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from password_dashboard.models import UserGeneratedPasswordModel

import base64

from password_dashboard.password_generating_algorithm import algorithm

from django.contrib.auth.models import User
from user_authentication.models import UserProfileModel


# website_name = None
# category = None
# include_name = None
# include_surname = None
# include_age = None
# difficuilty = None
# tags  = None

def getCategoryImages(category):
    if category == 'Sport':
        return "sport.svg"
    elif category == 'Social media':
        return "social_media.svg"
    elif category == 'Programming and IT':
        return "programming_it.svg"
    elif category == 'Coocking':
        return "cooking.svg"
    elif category == 'Art / Drawing':
        return "art_drawing.svg"
    elif category == 'Math':
        return "math.svg"
    elif category == 'Language':
        return "language.svg"
    elif category == 'Science':
        return "science.svg"
    elif category == 'Robotics':
        return "robotics.svg"
    elif category == 'Dancing':
        return "dancing.svg"
    elif category == 'Music / Singing':
        return "music_singing.svg"
    elif category == 'Video games':
        return "video_games.svg"
    elif category == 'Yoga / Mediatation':
        return "yoga_meditation.svg"
    elif category == 'Martial arts':
        return "martial_arts.svg"
    elif category == 'Design':
        return "design.svg"
    elif category == 'School / University':
        return "school_university.svg"
    
@login_required
def PasswordDashboardView(request):
    passwords_list = []
    context = {}
    if request.method == 'POST':
        generated_password_input = request.POST.get('edit_result_input')
        if generated_password_input is not None:
            cathegory_value = request.POST.get('cathegory_input_hidden')
            encrypted_gen_pass = base64.b64encode(generated_password_input.encode('ascii')).decode('ascii')
            print("Encrypted pass:",encrypted_gen_pass)
            # decr = base64.b64decode(encrypted_gen_pass.encode('ascii')).decode('ascii')
            # print("Decr:",decr)
            profile = UserProfileModel.objects.get(user=request.user)
            print("Profile:",profile)
            print("cathegory_input_hidden")
            website_name = request.POST.get('website_name_hidden')
            print("Website name:",website_name)
            cathegory_val = request.POST.get('cathegory_hidden')
            print("cathegory:",cathegory_val)
            # new_pass = UserGeneratedPasswordModel(userID=profile)

        else:
            website_name = request.POST.get('website_name')
            category = request.POST.get('cathegory_input_hidden')
            include_name = request.POST.get('include_name')
            include_surname = request.POST.get('include_surname')
            include_age = request.POST.get('include_age')
            difficuilty = request.POST.get('difficulty_level_hidden')
            tags = request.POST.get('tags_result_hidden').split(',')
            # generate_more = request.POST.get('generate_more')
            # print("Generate more:",generate_more)
            if(len(tags) and tags[0] == ''):
                tags.pop()
            print(difficuilty)
            # for d in difficuilty:
            #     print("Diff:",d)
            # print("Website name:",website_name)
            # print("Category:",category)
            # print("Include_name:",include_name)
            # print("Include surname:",include_surname)
            # print("Include age:",include_age)
            # print("Difficulty level:", difficuilty)
            print(f"###Tags: {tags}")
            profile = UserProfileModel.objects.get(user=request.user)
            algorithm.website_name = website_name
            algorithm.cathegory = category
            if include_name == None:
                algorithm.user_name = ''
            else:
                algorithm.user_name = profile.user.username
            if include_surname == None:
                algorithm.user_surname = ''
            else:
                algorithm.user_surname = profile.user.last_name
            if include_age == None:
                algorithm.user_birthday = False
                algorithm.day = 0
                algorithm.month = 0
                algorithm.year = 0
            else:
                algorithm.user_birthday = True
            algorithm.difficulty_level = int(difficuilty)
            algorithm.containing_words = tags
            date_of_birth = profile.date_of_birth
            algorithm.day = int(date_of_birth.day)
            algorithm.month = int(date_of_birth.month)
            algorithm.year = str(date_of_birth.year)
            algorithm.editDate()
            print(date_of_birth)

                
            for i in range(3):
                passwords_list.append(algorithm.newPassword())

            print(passwords_list)
            context["generated_passwords"] = passwords_list 
        passwords = UserGeneratedPasswordModel.objects.filter(userID = request.user.userprofilemodel)
        category_images = []
        new = []
        print(passwords)
        for password in passwords:
            # password.password = base64.b64decode(password.password.encode('ascii')).decode('ascii'
            password.password = base64.b64decode(password.password.encode('ascii')).decode('ascii')
            print(f'{password.password}')
            # category_images.append(getCategoryImages(password.category))
            testing = [password,f"password_dashboard/cathegories_images/{getCategoryImages(password.category)}"]
            new.append(testing)
        # passwords = [passwords,category_images]

        print(f"Date: {request.user.userprofilemodel.date_of_birth}")
        context["passwords"] = new
        context["user"] = request.user
    return render(request,'password_dashboard/dashboard.html',context)