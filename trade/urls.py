from django.urls import path
from .views import TradeNodeListCreateView, TradeNodeRetrieveUpdateDestroyView

urlpatterns = [
    path('nodes/', TradeNodeListCreateView.as_view(), name='node-list-create'),
    path('nodes/<int:pk>/', TradeNodeRetrieveUpdateDestroyView.as_view(), name='node-retrieve-update-destroy'),
]