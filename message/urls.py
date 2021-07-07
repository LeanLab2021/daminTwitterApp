from django.urls import path

from .views import MessageListView, change_room, create_room

app_name = 'message'

urlpatterns = [
    path('', MessageListView.as_view(), name='message'),
    path('create_room/<str:to_user>/', create_room, name='create_room'),
    path('change_room/<str:user_name>/', change_room, name='change_room')
]
