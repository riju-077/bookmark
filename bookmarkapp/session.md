# Session Log — Bookmarks App (Phase 2)

## Session 1 — April 9, 2026

### What We Did
1. **Project Setup** — Django project `bookmark` inside `bookmarkapp/`, Django 6.0.4, uv, `.venv`
2. **Created `links` app** — `startapp links`, added to `INSTALLED_APPS`
3. **Bookmark Model** — user (ForeignKey), title, url, tag, importance_level (High/Med/Low), created_at. Student added importance_level on own initiative.
4. **Admin Setup** — `@admin.register`, list_display, list_filter, search_fields
5. **Test Data** — 3 users (akash, rama, riju), each with 1 bookmark via admin

### Concepts Covered
- ForeignKey, CASCADE, `__str__`, `class Meta`, `blank=True`, URLField
- Data ownership, auth_user table, superuser
- Admin customization (list_display, list_filter, search_fields)
- Python imports (package vs module vs class vs function)
- `models.Model` inheritance

---

## Session 2 — April 13, 2026

### What We Did

1. **`links/forms.py`** — Created `BookmarkForm` (ModelForm)
   - Student initially included `user` in fields — explained why it must be excluded (security)
   - Fields: title, url, tag, importance_level

2. **`links/views.py`** — Built 3 out of 6 views:
   - **home** (READ) — Claude wrote this one as a demo. Uses `@login_required`, `Bookmark.objects.filter(user=request.user)`, renders to `links/home.html`
   - **create_bookmark** (CREATE) — Student wrote this one by adapting Phase 1 paste view. Needed help with: attaching `request.user` via `commit=False` pattern, fixing template path
   - **edit_bookmark** (UPDATE) — Claude wrote this one as a demo. Key differences from create: takes `pk`, uses `get_object_or_404` with `user=request.user` for security, uses `instance=bookmark` to pre-fill form

### Concepts Covered
- **`@login_required`** — decorator that protects views from logged-out users
- **`request.user`** — the currently logged-in user, available in every view
- **`.filter(user=request.user)`** — data ownership in one line (like SQL WHERE user_id = ?)
- **`render(request, template, context)`** — takes template + data dict, sends HTML back to browser
- **`form.save(commit=False)`** — get the object without saving to DB, so you can add extra data (like user) first
- **`get_object_or_404`** — fetch object or return 404. Adding `user=request.user` prevents users editing each other's bookmarks
- **`instance=bookmark`** — pre-fills form with existing data (used in edit, not needed in create)
- **What `forms.py` is** — the layer between the user and the database. Model = what gets stored, Form = what the user sees and fills in. ModelForm auto-generates form fields from model and handles validation.

### How the Session Went
- Student got frustrated — felt like they weren't learning, couldn't navigate docs effectively
- Taught doc-reading strategy: don't read top-to-bottom, use Ctrl+F to find the ONE thing you need
- Student asked to see home and edit views done for them so they could learn the pattern — this worked well
- Student successfully wrote create_bookmark by adapting Phase 1 paste view (copy-and-adapt approach)
- Key insight: comparing create vs edit side-by-side made the differences click

---

## What's Left to Build

### Views (3 remaining):
- **delete_bookmark** — simplest view, no form needed. fetch → confirm → delete → redirect
- **register** — uses Django's built-in `UserCreationForm`, logs user in after registration
- **login/logout** — use Django's built-in `auth_views.LoginView` and `LogoutView` (no custom view code)

### URLs:
- **`links/urls.py`** — all URL routes (home, create, edit, delete, register, login, logout)
- **`bookmark/urls.py`** — connect links urls to root with `include()`

### Settings:
- Add `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL` to `settings.py`

### Templates (7 files in `links/templates/links/`):
- base.html, home.html, create.html, edit.html, confirm_delete.html, login.html, register.html

### Other:
- Django Messages — success messages for create/edit/delete actions
- Clean up old comments in create_bookmark view

---

## Next Session: Start with `delete_bookmark` view (student's turn to write it)
