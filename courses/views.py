from django.shortcuts import render
from .models import Course


# Create your views here.
def courses(request):
    if not request.user.is_authenticated:
        return render_access_denied_page(request)
    return render_courses_list(request)

def render_courses_list(request):
    courses_list = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses_list})

def render_access_denied_page(request):
    return render(request, 'courses/access_denied.html')