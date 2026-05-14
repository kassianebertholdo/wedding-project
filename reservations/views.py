from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Reservation


@login_required
def my_reservations(request):

    reservations = Reservation.objects.filter(
        user=request.user
    )

    return render(
        request,
        'reservations/my_reservations.html',
        {
            'reservations': reservations
        }
    )


@login_required
def cancel_reservation(request, reservation_id):

    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        user=request.user
    )

    # liberar presente
    gift = reservation.gift

    gift.reserved = False
    gift.save()

    # remover reserva
    reservation.delete()

    return redirect(
        'my_reservations'
    )