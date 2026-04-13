# The Django Project Pattern

Just like ML has: data → clean → EDA → features → train → test
Django has its own repeatable pattern that works for ANY project.

---

## Step 1 — Setup (once per project)

```
Create project       →  django-admin startproject projectname .
Create app           →  python manage.py startapp appname
Register app         →  Add "appname" to INSTALLED_APPS in settings.py
```

---

## Step 2 — Model (once per data type, revisit when data changes)

```
Define model class   →  Write a class in models.py (fields = your database columns)
Create migration     →  python manage.py makemigrations
Apply migration      →  python manage.py migrate
```

Rule: Every time you touch models.py → run makemigrations → migrate. Always.

---

## Step 3 — Admin (once per model)

```
Register model       →  admin.site.register(YourModel) in admin.py
Create admin user    →  python manage.py createsuperuser (first time only)
Test it              →  Visit /admin/, add some test data
```

---

## Step 4 — URL → View → Template (repeat for EVERY page)

This is where you spend 80% of your time. Every new page follows this:

```
1. urls.py     →  Add a path: what URL triggers this page?
2. views.py    →  Write a function: what logic runs when that URL is visited?
3. template    →  Create HTML: what does the user see?
```

Examples of pages that all follow this exact pattern:
- Home page
- Detail page (view one item)
- List page (view all items)
- Edit page
- Delete page
- About page
- ANY page

---

## Step 5 — Forms (add to any page that takes user input)

```
1. forms.py    →  Create a form class (ModelForm links to your model automatically)
2. views.py    →  Handle two cases:
                    GET  = show empty form
                    POST = save submitted data, redirect
3. template    →  Add {{ form.as_p }} and {% csrf_token %} inside a <form> tag
```

---

## The Flow Diagram

```
START
  │
  ▼
Step 1: Setup (once)
  │
  ▼
Step 2: Model → makemigrations → migrate
  │
  ▼
Step 3: Admin (register model, test data)
  │
  ▼
Step 4: URL → View → Template  ◄──── repeat for each page
  │
  ▼
Step 5: Forms (if page needs user input)
  │
  ▼
DONE — New feature? Go back to Step 4.
        Data changed? Go back to Step 2, then continue.
```

---

## Key Files and What They Do

| File | Purpose |
|---|---|
| `settings.py` | Project config — installed apps, database, etc. |
| `models.py` | Your data — each class = one database table |
| `urls.py` | URL routing — maps URLs to view functions |
| `views.py` | Logic — what happens when a URL is visited |
| `forms.py` | Form classes — handles user input and validation |
| `admin.py` | Register models to show in admin dashboard |
| `templates/` | HTML files — what the user sees in the browser |

---

## Template Tags Cheat Sheet

| Syntax | Purpose | Example |
|---|---|---|
| `{{ }}` | Print a value | `{{ paste.content }}` |
| `{% %}` | Do something | `{% if user %}`, `{% url 'home' %}` |
| `{% csrf_token %}` | Security token | Required inside every `<form>` tag |
| `{{ form.as_p }}` | Render form fields | Auto-generates HTML inputs |

---

## Common Commands

```bash
python manage.py runserver        # Start dev server
python manage.py makemigrations   # Generate migration from model changes
python manage.py migrate          # Apply migrations to database
python manage.py createsuperuser  # Create admin account
python manage.py shell            # Interactive Python with Django loaded
```

---

## Adapting Examples from Docs

When reading Django docs or Stack Overflow examples:

- **Django keywords** (NEVER change): path, render, ModelForm, redirect, get_object_or_404, request, is_valid, urlpatterns, class Meta
- **Made-up names** (ALWAYS replace with yours): ArticleForm, NameForm, MyModel, resource, obj

Rule: If you see a name that doesn't exist in Django's vocabulary → it's the author's choice → replace it with your project's name.
