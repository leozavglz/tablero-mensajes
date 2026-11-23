# mensajes/admin.py
from django.contrib import admin

from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ["texto", "autor", "fecha"]
    list_filter = ["fecha"]
    search_fields = ["texto"]
