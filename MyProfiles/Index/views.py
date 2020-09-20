from django.shortcuts import render
from passlib.hash import pbkdf2_sha256
from Index.models import Profile

# Create your views here.
def index(request):
    return render(request, 'Index/register.html')

def register(request):
    if request.method == 'POST':
        social_media_site = request.POST.get('inputSocialMedia')
        user_name = request.POST.get('inputUserName')
        passowrd = request.POST.get('inputPassowrd')
        password = pbkdf2_sha256.encrypt(passowrd, rounds = 12000, salt_size = 32)
        Profile.objects.create(
            social_media = social_media_site,
            user_name = user_name,
            password = passowrd
        )
    return render(request, 'Index/register.html')