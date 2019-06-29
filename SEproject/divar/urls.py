from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.ShowStuff.as_view(), name='showStuff'),
    url(r'^(?P<stuff_id>[0-9]+)/detail/$', views.stuffDetail, name='stuffDetail'),
    url(r'^user_profile/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^user_profile/create_item$', views.create_item, name='create_item'),
    url(r'^user_profile/favorites$', views.user_favorites, name='favorites'),
    url(r'^user_profile/items/$', views.user_items, name='user_items'),
    url(r'^user_profile/items/(?P<object_id>[0-9]+)/delete_item/$', views.delete_item, name='delete_item'),
    url(r'^user_profile/items/(?P<item_id>[0-9]+)/user_item_detail/$', views.user_item_detail, name='user_item_detail'),
    url(r'^user_profile/items/(?P<pk>[0-9]+)/user_item_detail/update$', views.ItemUpdate.as_view(), name='item_update'),
    url(r'^favorite$', views.favorite_item, name='favorite'),
]