# gatortechuf.com
Repository for the new GatorTech website

## To Run
Clone the git repo

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py collectstatic --noinput`

`python manage.py runserver`

Visit http://127.0.0.1:8000

### Creating groups
The groups `bloggers` and `recruiters` needs to be manually created. `bloggers` get access to all blog function, `recruiters` get access to `directory_access`.


## Important Directories/Files
### /gatortech
- contains the website config file `settings.py`
- contains the global URL file `urls.py`

### /home/static
- contains the global CSS/JS files and images
- edit main.css to override Bootstrap and add new classes

### /templates
- contains `base.html` template
- contains account related pages like log in and sign up
