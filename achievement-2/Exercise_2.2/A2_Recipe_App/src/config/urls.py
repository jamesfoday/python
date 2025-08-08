from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # maps root to recipes_home view
]
