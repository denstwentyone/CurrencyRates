from django.urls import path, include
from . import views

urlpatterns = [
    path('currencies/', views.CurrencyList.as_view()),
    path('rates/', views.CurrencyRateList.as_view())
]