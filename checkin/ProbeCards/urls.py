from django.urls import path
from . import views


urlpatterns = [
    path('formpcout/', views.PCout, name="Check out Probe Cards"),

    # path('PCin/<str:qk>/', views.PCin, name="Check in Probe Cards"),
    # path('PCinv/<str:rk>/', views.PCinv, name="Probe Cards Inventory"),
    # path('PCstatus/<str:sk>/', views.PCstatus, name="Probe Cards Status"),
]   