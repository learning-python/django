from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('toppings/', include('toppings.urls')),
    path('admin/', admin.site.urls),
]