import message
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import Message
from users.models import Follow
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

room_username = ''


class MessageListView(LoginRequiredMixin, ListView):
    room_username = ''
    model = Message
    template_name = "message/message.html"
    context_object_name = 'message_rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        follows = Follow.objects.filter(follow_user=self.request.user)
        context["rooms"] = [follow.follow_user for follow in follows]
        for followee in context['rooms']:
            print(dir(followee))
            print(followee.from_user.all())
        # context['from_messages'] = [
        #     message for message in User.from_user_set.filter(from_user=self.request.user)]
        # context['to_messages'] = [message for message in User.to_user_set.filter(
        #     to_user=User.objects.get(username=room_username))]
        return context


def create_room(request, to_user):
    MessageListView.room_username = to_user
    return redirect('message:message')


def change_room(request, user_name):
    receiver = get_object_or_404(User, username=user_name)
    room_username = receiver.username
    context = {
        'room_username': room_username
    }
    return redirect('message:message', context=context)
