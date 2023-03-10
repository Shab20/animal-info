from django.urls import path
from info.views import family, animal
from . import views

urlpatterns = [
    path('family/<int:family_id>/', views.family, name='family'),
    path('animal/<int:animal_id>/', views.animal, name='animal'),
]
