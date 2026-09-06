from django.urls import path

from . import views

urlpatterns = [
    path('login', views.SolidLoginView.as_view(), name='login'),
    path('logout', views.solid_logout, name='logout')
]
