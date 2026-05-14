from django.contrib import admin

from .models import (
    Couple,
    CouplePhoto
)


admin.site.register(Couple)

admin.site.register(CouplePhoto)