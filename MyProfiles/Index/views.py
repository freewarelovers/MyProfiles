from django.shortcuts import render
# from passlib.hash import pbkdf2_sha256
from Index.models import Profile

# Create your views here.
def index(request):
    return render(request, 'Index/register.html')

def list_sites(request):
    sites_list = {}
    count = 0
    for i in Profile.objects.all():
        sites_list[count] = {'user_name': i.user_name, 'social_media': i.social_media, 'password': i.password}
        count += 1
    print(sites_list)
    for var in sites_list:
        print(sites_list[var])
        print(sites_list[var])
        print(sites_list[var])
    return render(request, 'Index/list.html',context = sites_list)

def register(request):
    if request.method == 'POST':
        social_media_site = request.POST.get('inputSocialMedia')
        user_name = request.POST.get('inputUserName')
        password = request.POST.get('inputPassowrd')
        password = pbkdf2_sha256.encrypt(password, rounds = 12000, salt_size = 32)
        Profile.objects.create(
            social_media = social_media_site,
            user_name = user_name,
            password = password
        )
    return render(request, 'Index/success.html')

# def login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('inputUserName')
#         password = request.POST.get('inputPassword')
#         try:
#             password_check = LogIn(user_name = user_name)
#         except:
#             print('No such user')
#         if password_check == pbkdf2_sha256.encrypt(password, rounds = 12000, salt_size = 32):
#             return render(request, 'Index/list.html')
#         else:
#             print('Password Incorrect')

def remove(request):
    if request.method == 'POST':
        social_media_site = request.POST.get('inputSocialMedia')
        user_name = request.POST.get('inputUserName')
        passowrd = request.POST.get('inputPassowrd')
        password = pbkdf2_sha256.encrypt(passowrd, rounds = 12000, salt_size = 32)
        Profile.objects.delete(
            social_media = social_media_site,
            user_name = user_name,
            password = passowrd
        )
    return render(request, 'Index/success.html')

def contact(request):
    return render(request, 'Index/contact.html')