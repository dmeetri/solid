from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='create_ticket', permanent=False)),

    path('auth/', include('users.urls')),
    path('tickets/', include('tickets.urls')),
]
