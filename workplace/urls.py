from django.urls import path
from app_cadaster import views

urlpatterns = [
    # Rota, view responnsável, nome de referência
    # MarketPlace.com
    path('',views.home,name='home'),
]
