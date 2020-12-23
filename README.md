# blog-django

A simple blog application with functionality of comments and sharing post with email.

## How To Use

```shell
Note: Procfile, Runtime and Some other settings are just specified for heroku.
```

### Creating a Virtual Environment - (Optional but Recommended)

You can use any option from following:

```shell
pip install virtualenv
virtualenv venv_name
```

or

```shell
pyhton -m venv venv_name
```

### Activating Virtual Environment

To activate virtual environment run following commands in shell or cmd:

Unix/Linux:

```shell
source tutorial-env/bin/activate
```

Winddows:

```shell
venv_name\Scripts\activate
```

## Cloning and Using This Repository

Cloning repo:

```shell
git clone https://github.com/rajeshberwal/blog-django.git
```

Installing dependencies:

```shell
cd blog-django
pip install -r requiremnets.txt
```

Migrating Models:

```shell
python manage.py makemigrations
python manage.py migrate
```

Migrating Blog Models

```shell
python mannage.py makemigrations blog
python manage.py migrate
```

Creating Superuser:

```shell
python manage.py createsuperuser
```

And then enter all the required info in shell.

### Running Blog

```shell
python manage.py runserver
```

You can visit 127.0.0.1:8000/blog to check your blog and for admin pannel 127.0.0.1:8000/admin

**Have A Good Day/Night**
