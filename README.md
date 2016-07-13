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

## Important Directories/Files
### /home/static
- contains the global CSS files and images
- edit main.css to override Bootstrap and add new classes