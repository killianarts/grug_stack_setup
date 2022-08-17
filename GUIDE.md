# Getting started
Before making the contact form, first we need to setup the GRUG stack environment.

# Installing software

Installed via `pip`
1. django
2. django-htmx
3. django-tailwind
4. django-widget-tweaks

# Make new app
`python manage.py startapp core`

# Make static directory
Make a directory called `static` in the `core` app directory.
Make a directory called `core` in the `static` app directory (yes, really).

We'll use this directory later. Still more setup to do.

# Make templates directory
Make a directory called `templates` in the `core` app. 
Make a directory called `core` in the `templates` folder (stop asking questions, grug).

We'll use this directory later. Still more setup to do.

# Add to INSTALLED_APPS
```python
# Add these entries below the default Django applications
INSTALLED_APPS = [
    ...,
    'core',
    'django_htmx',
    'tailwind',
    'widget_tweaks',
]
```

# HTMX: Add Middleware
https://django-htmx.readthedocs.io/en/latest/installation.html
```python
MIDDLEWARE = [
    ...,
    "django_htmx.middleware.HtmxMiddleware",
    ...,
]
```

# HTMX: Download and add to static folder
1. Download HTMX [here](https://unpkg.com/htmx.org/dist/htmx.min.js)
2. Put it in the `core` app's static directory (you will put it in `core/static/core/htmx.min.js`)

We're done with HTMX for now.

# Tailwind: Create Tailwind CSS app
https://django-tailwind.readthedocs.io/en/latest/installation.html
`python manage.py tailwind init`

Follow instructions. Use default name `theme` for app.

# Tailwind: Modify `settings.py`
Add `theme` and `django_browser_reload` to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...,
    'core',
    'django_htmx',
    'tailwind',
    'widget_tweaks',
    'theme',
    'django_browser_reload',
]
```
Register the `theme` app with the following line:

```python
TAILWIND_APP_NAME = 'theme'
```

Add `INTERNAL_IPS` setting:

```python
INTERNAL_IPS = [
    '127.0.0.1'
]
```

Add `django_browser_reload` middleware:

```python
MIDDLEWARE = [
    ...,
    'django_htmx.middleware.HtmxMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    ...,
]
```

# Tailwind: Install TailwindCSS dependencies
`python manage.py tailwind install`

# Tailwind: Add `django_browser_reload` to `urls.py`

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

# Final setup
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

We need to add HTMX and _hyperscript to this file. Under `{% load static tailwind_tags %}`, add two more lines:

```html
{% load static %}
{% load django_htmx %}
```

Inside `<head>`, under `{% tailwind_css %}`, add:

```html
<script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
<script src="{% static 'htmx.min.js' %}" defer></script>
```
This is the only install step for _hyperscript.

Your `base.html` file should look like this:

```html
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
        <script src="https://unpkg.com/hyperscript.org@0.9.7"></script>
        <script src="{% static 'htmx.min.js' %}" defer></script>
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
