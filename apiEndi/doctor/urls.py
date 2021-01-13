from django.urls import path
from .views import getDoctors

urlpatterns = [
    path('get-doctors', getDoctors.as_view()),
]
