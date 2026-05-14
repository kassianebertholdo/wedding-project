from django.db import models
from django.contrib.auth.models import User
import qrcode


# =====================================
# COUPLE
# =====================================

class Couple(models.Model):

    pix_qrcode = models.ImageField(
        upload_to='pix_qrcodes/',
        blank=True,
        null=True
    )

    pix_key = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    bride_name = models.CharField(
        max_length=100
    )

    groom_name = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        unique=True
    )

    story = models.TextField()

    cover_image = models.ImageField(
        upload_to='couples/'
    )

    wedding_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def save(self, *args, **kwargs):

        # gerar QR Code
        if self.pix_key:

            qr = qrcode.make(
                self.pix_key
            )

            file_name = (
                f'{self.slug}_pix.png'
            )

            qr.save(
                f'media/pix_qrcodes/{file_name}'
            )

            self.pix_qrcode = (
                f'pix_qrcodes/{file_name}'
            )

        super().save(*args, **kwargs)


    def __str__(self):

        return (
            f"{self.bride_name} "
            f"& "
            f"{self.groom_name}"
        )


# =====================================
# GALERIA
# =====================================

class CouplePhoto(models.Model):

    couple = models.ForeignKey(
        Couple,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    image = models.ImageField(
        upload_to='couple_gallery/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'Foto de {self.couple}'