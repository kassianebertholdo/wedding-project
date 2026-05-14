from django.urls import path

from .views import (
    my_reservations,
    cancel_reservation
)


urlpatterns = [

    path(
        'my-reservations/',
        my_reservations,
        name='my_reservations'
    ),

    path(
        'cancel-reservation/<int:reservation_id>/',
        cancel_reservation,
        name='cancel_reservation'
    ),

]