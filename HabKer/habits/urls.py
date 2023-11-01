from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('newhabit', NewHabitView.as_view(), name='create_habit'),
    path('', Index.as_view(), name='index'),
    path('habit/<int:pk>/', HabitDetail.as_view(), name='habit_detail'),
    path('complete', Complete.as_view(), name='complete'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
