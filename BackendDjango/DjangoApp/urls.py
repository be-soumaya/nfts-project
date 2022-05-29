from django.urls import re_path as url
from DjangoApp import views 
 
urlpatterns = [ 
    url(r'^api/collections$', views.collection_list),
]