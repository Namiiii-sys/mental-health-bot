from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('chat/', views.chat_page),  
    path('api/', views.chat_with_bot),
    path('api/affirmation/', views.affirmation_view), 
]
