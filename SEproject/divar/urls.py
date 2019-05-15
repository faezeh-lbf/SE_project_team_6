from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.ShowStuff.as_view(), name='showStuff'),
    url(r'^detail/$', views.stuffDetail, name='stuffDetail'),
    url(r'^user_profile/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^user_profile/create_item$', views.create_item, name='create_item')
]
