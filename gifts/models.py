from django.db import models

from couples.models import Couple


class Gift(models.Model):

    couple = models.ForeignKey(
        Couple,
        on_delete=models.CASCADE,
        related_name='gifts'
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='gifts/'
    )

    purchase_link = models.URLField(
        blank=True,
        null=True
    )

    reserved = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name