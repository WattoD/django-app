from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TagsListView(LoginRequiredMixin, TemplateView):
    context_object_name = 'tags'
    template_name = 'tags_list.html'
    login_url = '/login/'