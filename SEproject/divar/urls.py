from django.conf.urls import include, url
from . import views

urlpatterns = [ url(r'^home/$', views.ShowStuff.as_view(), name='showStuff'),
                url(r'^detail/$', views.stuffDetail, name='stuffDetail'),
]
