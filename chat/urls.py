from django.urls import path,include
from . import views


# urlpatterns = [
#     path('',views.room_list, name='rooms'),
#     path('<str:room>', views.room, name='room'),
#     ]

urlpatterns = [
    path("", views.room_list, name="room-list"),
    path("<str:room_name>/", views.room, name="room"),
]