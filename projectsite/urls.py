from django.urls import path
from projectsite.views import home

urlpatterns = [
    path('', home),

]