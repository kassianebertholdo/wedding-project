from django.urls import path

from .views import reserve_gift


urlpatterns = [

    path(
        'reserve/<int:gift_id>/',
        reserve_gift,
        name='reserve_gift'
    ),

]