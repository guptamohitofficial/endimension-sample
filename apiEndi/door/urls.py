from django.urls import path
from door.views import Login, ValidateToken, GetUser

urlpatterns = [
    path('login', Login.as_view()),
    path('verify-token', ValidateToken.as_view()),
    path('get-user', GetUser.as_view()),
]
