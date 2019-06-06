from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView

from .forms import ItemForm
from .models import UserProfile, Stuff


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
                    # return HttpResponse("<html><body>this is %s</body></html>" % request.user.username)
                    return redirect('/divar/user_profile/')
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
            login(request, user)
            return redirect('/divar/user_profile/')
    else:
        HttpResponse("<html><body>not posted.</body></html>")
    # return HttpResponse("<html><body>not posted.</body></html>")
    return render(request, 'index.html')


class ShowStuff(generic.ListView):
    template_name = 'showStuffByTime.html'
    context_object_name = 'stuffList'

    def get_queryset(self):
        return Stuff.objects.order_by('id')[:20]


def stuffDetail(request):
    stuffId = 1
    message = ""
    # stuff = get_object_or_404(Stuff, pk=stuffId)
    stuff = {}
    user = request.user
    return render(request, 'single-product-details.html', {'stuff': stuff, 'message': message})


@method_decorator([login_required], name='dispatch')
class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.request.user.userprofile.id)


@login_required
def create_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.owner = request.user.userprofile
        item.save()
        return HttpResponse("<html><body>item %s created successfully! :)</body></html>" % item.name)
    context = {
        "form": form,
    }
    return render(request, 'create_item.html', context)
