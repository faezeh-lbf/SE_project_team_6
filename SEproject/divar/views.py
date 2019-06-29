from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView, UpdateView
from .forms import ItemForm
from .models import UserProfile, Stuff, Favorite


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
            user = authenticate(username=mail, password=password)
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


def stuffDetail(request, stuff_id):
    message = ""
    # stuff = get_object_or_404(Stuff, pk=stuffId)
    stuff = {}
    stuff = get_object_or_404(Stuff, pk=stuff_id)
    # stuff = {}
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
        if item.picture != 'media/default.jpg':
            item.has_pic = True
        item.save()
        return HttpResponse("<html><body>item %s created successfully! :)</body></html>" % item.name)
    context = {
        "form": form,
    }
    return render(request, 'create_item.html', context)


@login_required
def user_items(request):
    all_items = Stuff.objects.filter(owner=request.user.userprofile)
    return render(request, 'user_items.html', {'all_items': all_items})


def delete_item(request, object_id):
    item = get_object_or_404(Stuff, pk=object_id)
    item.delete()
    return redirect('../../')


def user_item_detail(request, item_id):
    item = get_object_or_404(Stuff, pk=item_id)
    return render(request, 'user_item_detail.html', {'item': item})


class ItemUpdate(UpdateView):
    model = Stuff
    fields = ['name', 'price', 'city', 'location', 'description', 'picture']
    template_name = 'stuff_update_form.html'


def favorite_item(request):
    print("in favorite function")
    item = Stuff.objects.get(pk=int(request.GET.get("id")))
    user = request.user.userprofile
    favorite = Favorite.objects.create(item=item, user=user)
    favorite.save()
    data = {
        'is_favorite': True
    }
    return JsonResponse(data)


def user_favorites(request):
    all_items = []
    favorites = Favorite.objects.filter(user=request.user.userprofile)
    for favorite in favorites:
        all_items.append(favorite.item)
    return render(request, 'user_items.html', {'all_items': all_items})
