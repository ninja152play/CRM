from django.contrib import admin

from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']

admin.site.register(User, UserAdmin)
admin.site.register(Service)
admin.site.register(Campaign)
admin.site.register(Lead)
admin.site.register(Contract)