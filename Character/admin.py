from django.contrib import admin
from .models import Karakter
# Register your models here.
@admin.register(Karakter)
class CharacterAdmin(admin.ModelAdmin):
     search_fields = ['name']

