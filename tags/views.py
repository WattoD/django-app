from django.shortcuts import render
from django.core.exceptions import PermissionDenied

# Create your views here.
def custom_tags(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    return render(request, 'tags.html')