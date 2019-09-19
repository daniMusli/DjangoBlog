
from django.conf.urls import url

from .views import *

app_name = 'hesap'
urlpatterns = [
    url(r'^giris/$',login_view,name='giris'),
    url(r'^uyeol/$',register_view,name='uyeol'),
    url(r'^cikis/$',cikis_view,name='cikis'),
]
