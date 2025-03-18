from django.contrib import admin
from courses.models import Course


# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('title',)
    search_fields = ('title',)