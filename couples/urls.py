from django.urls import path

from .views import (
    home,
    couple_detail,
    dashboard  
)


urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),
    path(
    'dashboard/',
    dashboard,
    name='dashboard'
),

    path(
        '<slug:slug>/',
        couple_detail,
        name='couple_detail'
    ),

   

]