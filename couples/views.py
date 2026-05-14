from django.shortcuts import (
    render,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Couple

from reservations.models import Reservation
from django.db.models import Sum


def home(request):

    couples = Couple.objects.all()

    return render(
        request,
        'home.html',
        {
            'couples': couples
        }
    )


def couple_detail(request, slug):

    couple = get_object_or_404(
        Couple,
        slug=slug
    )

    gifts = couple.gifts.all()

    return render(
        request,
        'couples/detail.html',
        {
            'couple': couple,
            'gifts': gifts
        }
    )


@login_required
def dashboard(request):

    try:

        couple = Couple.objects.get(
            user=request.user
        )

    except Couple.DoesNotExist:

        return render(
            request,
            'no_couple.html'
        )

    reservations = Reservation.objects.filter(
        gift__couple=couple
    )

    total_gifts = couple.gifts.count()

    reserved_gifts = couple.gifts.filter(
        reserved=True
    ).count()

    available_gifts = couple.gifts.filter(
        reserved=False
    ).count()

    total_amount = reservations.aggregate(
        Sum('gift__price')
    )['gift__price__sum']

    if not total_amount:
        total_amount = 0

    return render(

        request,

        'dashboard.html',

        {
            'couple': couple,
            'reservations': reservations,

            'total_gifts': total_gifts,

            'reserved_gifts': reserved_gifts,

            'available_gifts': available_gifts,

            'total_amount': total_amount
        }
    )