from django.urls import path
from .views import current_user, UserList
from django.conf.urls import url,include
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),

]