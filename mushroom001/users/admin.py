from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'work_id', 'nick_name', 'email', 'gender', 'address', 'mobile', 'image',
                    'join_time',
                    )
    list_filter = ('username', 'work_id', 'mobile')
    search_fields = ("username", "work_id")
    list_per_page = 20

