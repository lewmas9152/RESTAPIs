from django.urls import path
from . import views

urlpatterns = [
    path('drink/', views.drinks, name= 'drinks'),
    path('drink/<int:pk>', views.drink_detail, name= 'detail'),
    path('drinkAPIView/', views.DrinksAPIView.as_view(), name= 'drinksAPIView'),
    path('drinkAPIView/<int:pk>', views.drink_detailAPIView.as_view(), name= 'DetailAPIview')
]
