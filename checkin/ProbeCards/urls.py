from django.urls import path
from . import views


urlpatterns = [
    path('formpcout/', views.PCout, name="Check out Probe Cards"),
    path('formpcin/', views.PCin, name="Check in Probe Cards"),
    path('formpcinvadd/', views.PCinv, name="Add Probe Card"),
    path('formpcinvpo/', views.PCinvpo, name="Probe Card Order"),
    
    # path('PCinv/<str:rk>/', views.PCinv, name="Probe Cards Inventory"),
    # path('PCstatus/<str:sk>/', views.PCstatus, name="Probe Cards Status"),
]   