from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def index(request):
    if request.method == "POST":
        # return HttpResponse("<html><body>got it!</body></html>")
        if request.POST.get('submit') == 'login':
            # return HttpResponse("<html><body>got it!</body></html>")
            mail = request.POST['mail']
            password = request.POST['password']
            user = authenticate(username=mail, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("<html><body>%s signed in successfully.</body></html>" % mail)
                else:
                    return render(request, 'index.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'index.html', {'error_message': 'Invalid login'})
        elif request.POST.get('submit') == 'register':
            mail = request.POST['mail']
            password = request.POST['password']
            phone_number = request.POST['phonenumber']
            user = User.objects.create_user(username=mail, password=password)
            user.email = mail
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.phone_number = phone_number
            user_profile.save()
            return HttpResponse("<html><body>%s signed up successfully.</body></html>" % mail)
    else:
        HttpResponse("<html><body>not posted.</body></html>")
    # return HttpResponse("<html><body>not posted.</body></html>")
    return render(request, 'index.html')

# class showStuff:
#     template_name = 'divar/showStuffByTime.html'
#     context_object_name = 'stuffList'
#
#     def get_queryset(self):
#         return Stuff.objects.order_by('id')[:20]
