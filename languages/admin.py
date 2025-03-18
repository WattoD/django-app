from django.contrib import admin

from courses.models import Course
from languages.models import Language

# Register your models here.
class CourseAdminInLine(admin.StackedInline):
    model = Course
    extra = 1
    fields = ('title', 'description')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'rtl', 'created_at', 'course_count')
    inlines = [CourseAdminInLine]
    list_filter = ('name', 'code')
    list_editable = ('rtl',)
    search_fields = ('name','code')
    list_per_page = 10
    ordering = ('-name',)

    fieldsets = (
        ('Basic fields', {'fields': ('name', 'code')}),
        ('Additional fields', {'fields': ('rtl',)}),
    )

    @staticmethod
    def course_count(obj):
        return Course.objects.filter(language=obj).count()

    class Media:
        js = ('js/admin_custom.js',)