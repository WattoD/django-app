from django.contrib import admin
from .models import Message, CustomUser

# Register your models here.
admin.site.register(Message)
# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number')
    list_filter = ('email',)
    search_fields = ('email','phone_number')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Особисті дані', {'fields': ('first_name', 'last_name'), 'classes': ('wide',)}),
    )