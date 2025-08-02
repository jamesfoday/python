# Exercise 2.2: Django Project Set Up

## What I Learned

- **Django Terminology:**  
  I learned the difference between a Django project and a Django app. A project is the entire web application structure that can contain multiple apps. Each app handles a specific functionality or module within the project. For example, a Bookstore project might have apps like books, sales, customers, and reports.

- **Project Structure:**  
  Creating a Django project using `django-admin startproject` generates a basic folder structure. Inside the root folder, there is another folder with configuration files like `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`, plus a `manage.py` file at the root level.  
  I also learned about renaming the root project folder for clarity and how the project tree looks after setup.

- **Project Configuration Files:**  
  - `settings.py` manages project settings including database configuration and installed apps.  
  - `urls.py` routes URLs to views or other apps.  
  - `wsgi.py` and `asgi.py` handle deployment and asynchronous server interfaces.

- **Running Migrations:**  
  Running `python manage.py migrate` sets up the database tables based on the default SQLite configuration. This step prepares the backend for the application and is essential before running the server.

- **Running the Server:**  
  Running the development server with `python manage.py runserver` deploys the project locally, allowing me to view the web app through a browser at `http://127.0.0.1:8000/`.

- **Creating Apps within the Project:**  
  I created a Django app (e.g., `books`) inside the project with the `python manage.py startapp books` command. The app has its own structure including files like `models.py`, `views.py`, `admin.py`, `migrations/`, and more.

- **Django Admin Interface:**  
  I learned about the built-in Django admin site, which allows managing the app’s data through a user-friendly interface. Creating a superuser with `python manage.py createsuperuser` grants full admin access to the site. This admin panel is useful for performing CRUD operations, managing users, and controlling permissions.

- **Modularity and Reusability:**  
  Django apps can be reused across multiple projects, demonstrating Django’s DRY philosophy and modular design. This helps keep code clean and maintainable across large applications.

## Summary

Exercise 2.2 deepened my understanding of how Django projects are structured and deployed. I now know how to set up a project, create apps, run migrations, start the server, and use the Django admin for backend management. This foundation prepares me to build out my Recipe application effectively using Django’s framework.
