from django.db import models

from django.db import models
from django.contrib.auth.models import User

from gifts.models import Gift


class Reservation(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    gift = models.OneToOneField(
        Gift,
        on_delete=models.CASCADE
    )

    reserved_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} reservou {self.gift.name}"
