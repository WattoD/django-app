from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from languages.models import Language


# Create your views here.
def languages(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    languages_list = Language.objects.all()
    return render(request, 'languages/languages_list.html', {'languages': languages_list})