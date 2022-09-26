The GRUG stack is a [Hypermedia-Driven Application](https://htmx.org/essays/hypermedia-driven-applications/) development
environment that enables full-stack developers to develop cutting-edge applications without the complexity of modern 
Single Page Application development.

It consists of:

1. A web framework backend like [Django](https://www.djangoproject.com/)
2. [HTMX](https://htmx.org/)
3. [_hyperscript](https://hyperscript.org/)
4. [TailwindCSS](https://tailwindcss.com/)

Some people prefer to substitute [Alpine.js](https://alpinejs.dev/) for _hyperscript. While technically different, they both occupy the same
place in the GRUG stack. I'll teach how to install both.

## The Fastest Way

If you just want to try the whole stack out fast, install Django (or your choice of backend frameworks) and then make
a `base.html` template that looks like this:

```html+django
<!DOCTYPE html>
<html lang="en">
<head>
    <title>The GRUG Stack</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <!-- HTMX library -->
    <script src="https://unpkg.com/htmx.org@1.8.0"
            integrity="sha384-cZuAZ+ZbwkNRnrKi05G/fjBX+azI9DNOkNYysZ0I/X5ZFgsmMiBXgDZof30F5ofc"
            crossorigin="anonymous"></script>

    <!-- Choose _hyperscript or Alpine.js -->
    <!-- _hyperscript library -->
    <script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
    <!-- Alpine.js library -->
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <!-- TailwindCSS styles -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>

   <body>
        {% block content %} {% endblock %}
   </body>
</html>
```

You are now ready to develop the latest Hypermedia-Driven Applications.

However, if you want to make an environment that you can later use in production, follow the rest of this tutorial.

## Summary

For the busy developer:

1. Install software `pip install ...`
    - [Django](https://www.djangoproject.com/)
    - [django-htmx](https://pypi.org/project/django-htmx/)
    - [django-tailwind](https://pypi.org/project/django-tailwind/)
    - [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)
    - [django-render-block](https://pypi.org/project/django-render-block/)
2. Follow their install and configuration procedures.
3. django-tailwind provides a `base.html` template. Add the _hyperscript or Alpine.js scripts to the head of the HTML.

Your `base.html` file should look like this when you're finished:

```html+django
{% load static tailwind_tags %}
{% load static %}
{% load django_htmx %}
<!DOCTYPE html>
<html lang="en">
   <head>
       <title>Django Tailwind</title>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
   
       {% tailwind_css %}
       <!-- Choose _hyperscript or Alpine.js -->
       <!-- _hyperscript library -->
       <script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
       <!-- Alpine.js library -->
       <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
       <script src="{% static 'core/htmx.min.js' %}" defer></script>
   </head>
   
   <body class="bg-gray-50 font-serif leading-normal tracking-normal">
      <div class="container mx-auto">
          <section class="flex items-center justify-center h-screen">
              <h1 class="text-5xl">Django + Tailwind = ❤️</h1>
          </section>
      </div>
   </body>
</html>
```

## Detailed Instructions

After installing everything via `pip`, continue with the following:

### Make new app

`python manage.py startapp core`

### Make static directory

Make a directory called `static` in the `core` app directory.
Make a directory called `core` in the `static` app directory (yes, really).

We'll use this directory later. Still more setup to do.

### Make templates directory

Make a directory called `templates` in the `core` app.
Make a directory called `core` in the `templates` folder (stop asking questions, grug).

We'll use this directory later. Still more setup to do.

### Add to `INSTALLED_APPS`

```diff
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   'core',
+   'django_htmx',
+   'tailwind',
+   'widget_tweaks',
+   'render_block',
]
```

### HTMX: Add Middleware

```diff
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
+   'django_htmx.middleware.HtmxMiddleware',
]
```

### HTMX: Download and add to static folder

1. Download HTMX [here](https://unpkg.com/htmx.org/dist/htmx.min.js)
2. Put it in the `core` app's static directory (you will put it in `core/static/core/htmx.min.js`)

We're done with HTMX for now.

### Tailwind: Create Tailwind CSS app

Run django-tailwind initialization script.

`python manage.py tailwind init`

Follow instructions. Use default name `theme` for app.

### Tailwind: Modify `settings.py`

```diff
INSTALLED_APPS = [
    ...,
    'core',
    'django_htmx',
    'tailwind',
    'widget_tweaks',
    'render_block',
+   'theme',
+   'django_browser_reload',
]

+ TAILWIND_APP_NAME = 'theme'


+ INTERNAL_IPS = [ '127.0.0.1' ]


MIDDLEWARE = [
    ...,
    'django_htmx.middleware.HtmxMiddleware',
+    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```

### Tailwind: Install TailwindCSS dependencies

`python manage.py tailwind install`

### Tailwind: Add `django_browser_reload` to `urls.py`

```python
## contact/contact/urls.py

# Add 'include' to imports
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
```

When we created the `theme` app with `python manage.py tailwind init`,
`django-tailwind` very kindly provided us a `base.html` file in the `theme/templates` folder.
Let's edit it.

### Final setup

The default `base.html` file provided by `django-tailwind` looks like this:

```html
{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en">
   <head>
       <title>Django Tailwind</title>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       {% tailwind_css %}
   </head>
   
   <body class="bg-gray-50 font-serif leading-normal tracking-normal">
      <div class="container mx-auto">
         <section class="flex items-center justify-center h-screen">
             <h1 class="text-5xl">Django + Tailwind = ❤️</h1>
         </section>
      </div>
   </body>
</html>
```

We need to add HTMX and _hyperscript (or Alpine.js) to this file. Under `{% load static tailwind_tags %}`, add two more
lines:

```django
{% load static %}
{% load django_htmx %}
```

Inside `<head>`, under `{% tailwind_css %}`, add:

```html

<script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
<script src="{% static 'htmx.min.js' %}" defer></script>
```

This is the only install step for _hyperscript (or Alpine.js).

Your `base.html` file should look like this:

```html+django
{% load static tailwind_tags %}
{% load static %}
{% load django_htmx %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Django Tailwind</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        
        {% tailwind_css %}
        <!-- Choose _hyperscript or Alpine.js -->
        <!-- _hyperscript library -->
        <script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
        <!-- Alpine.js library -->
        <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
        <script src="{% static 'core/htmx.min.js' %}" defer></script>
	</head>

   <body class="bg-gray-50 font-serif leading-normal tracking-normal">
      <div class="container mx-auto">
         <section class="flex items-center justify-center h-screen">
            <h1 class="text-5xl">Django + Tailwind = ❤️</h1>
         </section>
        </div>
   </body>
</html>
```

Phew! Setup complete, grug brother. 

You are now ready to start building your next Hypermedia-Driven Application

## One last thing

We didn't touch on why we installed `django-widget-tweaks` and `django-render-block`.

In a future guide you will see a practical example of how these are used and why they are part of the
GRUG stack development environment. To put it simply:

1. `django-widget-tweaks` lets us style Django forms in the template, rather than in the `forms.py` file. That allows us to follow the principle of [Locality of Behavior](https://htmx.org/essays/locality-of-behaviour/). It also makes using Tailwind much easier.
2. `django-render-block` similarly lets us include [template fragments](https://htmx.org/essays/template-fragments/) inside main template files, again allowing us to follow the principle of Locality of Behavior.

Because much of the action in a Hypermedia-Driven Application is in the hypermedia (i.e. HTML), 
it's important to install these two Django extensions to make working in Django templates easier.