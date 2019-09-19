
from django.conf.urls import url

from postApp.views import *

app_name = 'post'
urlpatterns = [
    url(r'^index/$',post_index,name='index'),
    url(r'^create/$',post_create,name="create"),

    url(r'^(?P<postsSlug>[\w-]+)/$',post_detail, name='detail'),
    url(r'^(?P<postsSlug>[\w-]+)/update$',post_update,name="update"),
    url(r'^(?P<postsSlug>[\w-]+)/delete$',post_delete,name="delete"),

]
