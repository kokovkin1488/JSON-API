from django.contrib import admin
from .models import User, Post, Rating


class UserAdmin(admin.ModelAdmin):
    list_display = ('login',)
    list_per_page = 15


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'ip')
    search_fields = ['user', 'title', 'ip']
    list_per_page = 15


class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'rating')
    search_fields = ['post', 'rating']
    list_per_page = 15


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Rating, RatingAdmin)