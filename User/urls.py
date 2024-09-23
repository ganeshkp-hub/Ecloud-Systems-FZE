from django.urls import path
from .import views


urlpatterns = [
    path('',views.users.as_view()),
    path('<str:name>/',views.Modify),
    
    
]