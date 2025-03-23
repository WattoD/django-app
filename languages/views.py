from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from languages.models import Language


# Create your views here.
class LanguageListView(LoginRequiredMixin, ListView):
    model = Language
    context_object_name = 'languages'
    template_name = 'languages/languages_list.html'
    login_url = '/login/'

    def get_queryset(self):
        return super().get_queryset()