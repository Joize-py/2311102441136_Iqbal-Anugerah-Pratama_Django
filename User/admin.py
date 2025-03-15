from django.contrib import admin
from User.models import user
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat', 'telpon']
    search_fields = ['user__username']
admin.site.register(user, userAdmin)
