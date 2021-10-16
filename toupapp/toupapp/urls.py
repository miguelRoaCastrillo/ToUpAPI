from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toupapi.urls'),)    
    #path('api/', toupapi.site.urls),
]
