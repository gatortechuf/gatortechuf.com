# gatortechuf.com
Repository for the new GatorTech website

## To Run (with docker)

Clone the git repo

Create a `.env` file with the same format as `.env.example`

`docker-compose up --build -d`

`docker ps`

Get the container ID for `gatortech_web`

`docker exec -i -t <container id> bash`

`python manage.py createsuperuser`

Visit http://127.0.0.1:8000

## To Run (without docker, requires postgres to be running)
Clone the git repo

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py collectstatic --noinput`

`python manage.py runserver`

Visit http://127.0.0.1:8000


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
