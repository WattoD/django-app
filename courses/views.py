from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course


# Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/courses_list.html'
    login_url = '/login/'

    def get_queryset(self):
        return super().get_queryset()