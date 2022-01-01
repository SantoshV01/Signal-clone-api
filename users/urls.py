from django.urls import path
from django.urls.conf import include
from .views import userList, searchUser, profileList, profileUpdate

urlpatterns = [
    path('', userList),
    path('profileList/', profileList),
    path('profileUpdate/<str:user_id>/', profileUpdate),
    path('searchUser/<str:search>/', searchUser)
]
