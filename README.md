# django
Django

# project => project can have many apps => apps can have many views

(In the terminal)
- [] Delete everything but the `.gitignore`, `LICENSE`, and `README.md`.
- [] Type `python3 -m venv thais_venv` or `py -m venv thais_venv`
- [] Type `source thais_venv/bin/activate` or `source thais_venv/Scripts/activate`
- [] Type `pip3 install django` or `py -m pip3 install django`
- [] Type `django-admin startproject thais_server`
- [] Type `cd thais_server`
- [] Type `python3 manage.py startapp toppings` or `py manage.py startapp toppings`
(In files)
- [] In the thais_server/toppings/views.py file, enter this text:

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Some toppings.")
```

- [] Make a the thais_server/toppings/urls.py file, and then enter this text:

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- [] In the thais_server/thais_server/urls.py file, replace the existing text with this text:

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('toppings/', include('toppings.urls')),
    path('admin/', admin.site.urls),
]
```
- [] In the thais_server/thais_server/settings.py file, scroll to the `TEMPLATES` variable and find the `DIRS` property. It should be an empty array. Add to it a string `templates`
- [] In the `thais_server` folder (the outer one), make a `templates` folder.
- [] In the `templates` folder, make a `zack.html` file with whatever content you want.
- [] In the thais_server/toppings/views.py file, add this text:
```
def zacks_html(request):
    template = loader.get_template("zack.html")
    return HttpResponse(template.render())
```
- [] In the thais_server/toppings/urls.py file, replace the file contents with this:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blah/', views.blah, name='blah'),
    path('hello/', views.zacks_html, name='hello'),
]
```
(In the terminal):
- [] Type `cd thais_server`
- [] Type `python3 manage.py migrate` or `py manage.py migrate`
- [] Type `python3 manage.py runserver` or `py manage.py runserver`

Your server is running on port 8000.