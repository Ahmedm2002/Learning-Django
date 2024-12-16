# Learning-Django

```
pip install uv                 # Install uv
uv venv venv                   # Create virtual environment
source venv/bin/activate       # Activate virtual environment
pip install django             # Install Django
django-admin startproject myproject  # Create Django project
cd myproject                   # Navigate to project directory
python manage.py runserver     # Run the development server
```

To change settings at project level update it in the settings.py present in the project folder

Urls are handeled in the url.py file

First we write the logic in the views.py file

then we write the urls.py file which tell on which url the specified data will be sent

## Templates

Settings can be changed
go to root folder and create folder named templates

HTML and CSS comest in the static folder

Add the templates folder in the settings.py file in the templates array into DIRS array to access the templates

Manage.py is most important file without it you cannot make apps or server

Make app using this command

```
python manage.py startapp appName
```

The first thing to do after creating an app is to tell the main project about the new app

goto settings.py file of project and add in installed app array

### What is Jinja in Django?

In Django, **Jinja** (often referred to as **Jinja2**) is a **templating engine**. Django uses templates to dynamically generate HTML pages based on data from your views and models. While Django comes with its own default templating engine, Jinja is a popular alternative due to its flexibility and similarity to the default engine.

#### Why are Templates (Like Jinja) Used in the First Place?

Templates help **separate the logic** (code) from the **presentation** (HTML). This separation makes your code cleaner and easier to maintain. Instead of writing HTML directly within your Python code, you can use templates to dynamically insert data into HTML files.

**The problem they solve:**

- Avoiding the mess of mixing Python code with HTML.
- Allowing frontend developers to work on HTML while backend developers work on Python logic.
- Reducing repetition by using template features like loops and conditions.

---

### Jinja Features in Django

Jinja allows you to:

1. **Inject variables**: Insert data dynamically into your HTML.
2. **Use control structures**: Include `for` loops, `if` statements, and filters.
3. **Create reusable components**: Use template inheritance to avoid repetitive code.

---

### Example of a Simple Jinja Template

Let's go through a **basic example** of using a Jinja template in a Django app.

#### 1. View in `views.py` (Django Backend)

Here's a simple Django view function that sends some data to a template:

```python
from django.shortcuts import render

def welcome_view(request):
    context = {
        'name': 'Ahmed Mujtaba',
        'courses': ['Django', 'React', 'FastAPI']
    }
    return render(request, 'welcome.html', context)
```

#### 2. Jinja Template in `welcome.html`

This template dynamically displays the data passed from the view.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Welcome Page</title>
  </head>
  <body>
    <h1>Welcome, {{ name }}!</h1>

    <h2>Your Courses:</h2>
    <ul>
      {% for course in courses %}
      <li>{{ course }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

#### Explanation of Jinja Syntax

1. **`{{ name }}`**: This injects the `name` variable into the HTML.
2. **`{% for course in courses %}`**: This is a loop that iterates over the `courses` list and displays each item.
3. **`{% endfor %}`**: Marks the end of the loop.

---

### Rendering Output

When you visit this view in your browser, you’ll see:

```
Welcome, Ahmed Mujtaba!

Your Courses:
- Django
- React
- FastAPI
```

---

### Alternatives to Jinja in Django

1. **Django's Default Templating Engine**:

   - Comes preinstalled with Django.
   - Syntax is similar to Jinja but slightly less flexible.

2. **Mako**:

   - Powerful templating engine.
   - Similar to Jinja but allows embedding full Python expressions in templates.
   - Best for more complex scenarios.

3. **Mustache/Handlebars**:

   - Simple logic-less templating engines.
   - Good for frontend-heavy projects.

4. **Jinja2**:
   - Very fast and powerful.
   - Often used in Flask, but can be integrated with Django.

---

### Summary

- **Templates** in Django (like Jinja) help separate logic and presentation.
- **Jinja** is an alternative to Django's default templating engine, known for its flexibility and speed.
- **Features** include variable injection, loops, and conditions.
- **Example** shows how data can be dynamically displayed in HTML using simple syntax.

## Migration Error on Server Start

- You never interact with the databases diretly in django instead there is a orm in django which talks to the database on your behalf
