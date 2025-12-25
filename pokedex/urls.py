from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # include the routes from the core app
    path('', include('core.urls')),
]
