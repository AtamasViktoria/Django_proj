from django.urls import path, include
from . import views
from .views import quiz_list

urlpatterns = [
    path('', quiz_list),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]