from django.core.mail import send_mail

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Gift

from reservations.models import Reservation


@login_required
def reserve_gift(request, gift_id):

    gift = get_object_or_404(
        Gift,
        id=gift_id
    )

    # impedir reserva duplicada
    if gift.reserved:

        return redirect(
            request.META.get('HTTP_REFERER')
        )

    # confirmar reserva
    if request.method == 'POST':

        Reservation.objects.create(
            user=request.user,
            gift=gift
        )

        # marcar presente como reservado
        gift.reserved = True
        gift.save()

        # enviar email automático
        send_mail(

            'Reserva confirmada 🎉',

            f'''
Olá {request.user.username}!

Sua reserva do presente:

{gift.name}

foi confirmada com sucesso 💍
            ''',

            'SEU_EMAIL@gmail.com',

            [request.user.email],

            fail_silently=False
        )

        return redirect(
            'my_reservations'
        )

    return render(
        request,
        'gifts/confirm_reservation.html',
        {
            'gift': gift
        }
    )