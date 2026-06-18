from django.contrib import admin
from .models import SupportMessage

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "user", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "user", "created_at")