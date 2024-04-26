from django.urls import path
from .import views

urlpatterns = [
    path('',views.customers_list),
    path('<int:pk>',views.customer_details)
]
