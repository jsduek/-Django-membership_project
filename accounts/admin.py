from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["username", "email", "phone_number", "created_at_display", "updated_at_display"]

    def created_at_display(self, obj):
        return obj.created_at

    def updated_at_display(self, obj):
        return obj.updated_at

    # 컬럼 이름 설정
    created_at_display.short_description = "Created At"
    updated_at_display.short_description = "Updated At"

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )