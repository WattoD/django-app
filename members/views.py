from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from .forms import MessageForm, TemporaryMessageForm
from .models import Message


# Create your views here.
def messages(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    messages_list = Message.objects.filter(user=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('messages')
    else:
        form = MessageForm()
    return render(request, 'messages/messages_list.html', {'messages': messages_list, 'form': form})

def temp_message(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    message = ''
    if request.method == 'POST':
        form = TemporaryMessageForm(request.POST)
        if form.is_valid():
            message_value = form.cleaned_data['value']
            request.session['message'] = message_value
            return redirect('temp_message')
    else:
        form = TemporaryMessageForm()
        message = request.session.get('message', '')
        request.session.pop('message', '')
    return render(request, 'messages/temp_message.html', {'message': message, 'form': form})