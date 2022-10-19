from django.shortcuts import render
# from passlib.hash import pbkdf2_sha256
from Index.models import Profile

# Create your views here.
def add(request):
    return render(request, 'Index/add_account.html')

def login(request):
    return render(request, 'Index/login.html')

def signin(request):
    if request.method == 'POST':
        if request.POST['inputPassword-1'] == request.POST['inputPassword-2']:
            return render(request, 'Index/list.html')
    return render(request, 'Index/signin.html')

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

def privacy(request):
    return render(request, 'Index/privacy.html')

def terms(request):
    return render(request, 'Index/terms.html')