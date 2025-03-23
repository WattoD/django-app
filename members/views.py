from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import MessageForm, TemporaryMessageForm
from .mixins import MessageOwnerMixin, FormSuccessMixin, UserMessageCountMixin, LastMessageDateTimeMixin
from .models import Message


# Create your views here.
class MessageListView(LoginRequiredMixin, FormSuccessMixin, UserMessageCountMixin, LastMessageDateTimeMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'messages/messages_list.html'

    def get_queryset(self):
        messages = super().get_queryset()
        if self.request.user.is_superuser:
            return messages
        return messages.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            return self.message_form_valid(form, request)
        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

class MessageDeleteView(LoginRequiredMixin, MessageOwnerMixin, DeleteView):
    model = Message
    template_name = 'messages/confirm_delete.html'
    success_url = reverse_lazy('messages')

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs['id'])

class TemporaryMessageView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'temp_messages'
    template_name = 'messages/temp_message.html'

    def post(self, request, *args, **kwargs):
        form = TemporaryMessageForm(request.POST)
        if form.is_valid():
            message_value = form.cleaned_data['value']
            request.session['message'] = message_value
            return redirect('temp_message')
        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        message = self.request.session.get('message', None)
        if message:
            context['message'] = message
            self.request.session.pop('message', None)

        context['form'] = TemporaryMessageForm()
        return context