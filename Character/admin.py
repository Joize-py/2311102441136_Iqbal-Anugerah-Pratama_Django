from django.contrib import admin
from .models import Karakter, Hero
# Register your models here.
@admin.register(Karakter)
class CharacterAdmin(admin.ModelAdmin):
     search_fields = ['name']

@admin.register(Hero)
class CharacterAdmin(admin.ModelAdmin):
     search_fields = ['name']

