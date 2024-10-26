# leaves/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('leaves/', views.leave_requests, name='leave_requests'),  # Correspond à l'URL /api/leaves/
]
