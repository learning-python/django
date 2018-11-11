# django
Django

(In the terminal)
- [] Type `python3 -m venv virtualenv`
- [] Type `source virtualenv/bin/activate`
- [] Type `pip3 install django`
- [] Type `django-admin startproject pizza`
- [] Type `cd pizza`
- [] Type `python3 manage.py startapp toppings`
(In files)
- [] In the pizza/toppings/views.py file, enter this text:

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Some toppings.")
```

- [] In the pizza/toppings/urls.py file, enter this text:

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- [] In the pizza/urls.py file, enter this text:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('toppings/', include('toppings.urls')),
    path('admin/', admin.site.urls),
]
```
(In the terminal):
- [] Type `python3 manage.py migrate`
- [] Type `python3 manage.py runserver`
