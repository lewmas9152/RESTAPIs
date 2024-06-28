from django.urls import path
from . import views

urlpatterns = [
    path('drink/', views.drinks, name= 'drinks'),
    path('drink/<int:pk>', views.drink_detail, name= 'drink')
]
