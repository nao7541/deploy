from django.contrib import admin
from .models import CustomUser, EventStock, UserFollowing
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(EventStock)
admin.site.register(UserFollowing)