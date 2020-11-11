from django.conf.urls import url

from mysite.core import views
from mysite.core1 import views as view1


urlpatterns = [
    url(r'^$', views.UsersListView.as_view(), name='users_list'),
    url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
    url(r'^generate1/$', view1.GenerateRandomUserView.as_view(), name='generate'),
]
