from datetime import time

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from members.models import Message


class MessageOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class FormSuccessMixin:
    def message_form_valid(self, form, request):
        message = form.save(commit=False)
        message.user = request.user
        message.save()
        return redirect('messages')

class MessageContentLengthMixin:
    max_length = 10

    def form_valid(self, form):
        if len(form.cleaned_data['value']) > self.max_length:
            form.add_error('value', 'Message too long')
            return self.form_invalid(form)
        return super().form_valid(form)

class MessageSpamCheckMixin:
    spam_keywords = ['test', 'test2', 'test3']

    def form_valid(self, form):
        content = form.cleaned_data['content']
        if any(keyword in content.lower() for keyword in self.spam_keywords):
            form.add_error('content', 'Message is spam')
            return self.form_invalid(form)
        return super().form_valid(form)

class MessageTimeLimitMixin:
    time_limit = time(23, 0)

    def form_valid(self, form):
        if form.cleaned_data['timestamp'].time() > self.time_limit:
            form.add_error('timestamp', 'The message could not be sent within the specified time period.')
            return self.form_invalid(form)
        return super().form_valid(form)

class UserMessageCountMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_message_count'] = Message.objects.filter(user=self.request.user).count()
        return context

class LastMessageDateTimeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_message = Message.objects.filter(user=self.request.user).order_by('-created_at').first()
        context['last_message_date'] = last_message.created_at if last_message else None
        return context

class TotalMessagesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['total_messages'] = Message.objects.count()
        return context

class LastMessageTimeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_message = self.model.objects.filter(user=self.request.user).order_by('-created_at').first()
        context['last_message'] = last_message.value
        return context