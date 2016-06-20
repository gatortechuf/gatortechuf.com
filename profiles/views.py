from django.views import generic
from django.contrib.auth.models import User


class Profile(generic.DetailView):
    template_name = 'profiles/index.html'
    model = User