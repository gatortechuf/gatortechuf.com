from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import UserProfile

@method_decorator(login_required, name='dispatch')
class ProfileList(generic.ListView):
    template_name = 'profiles/list.html'
    model = User
    context_object_name = 'user_list'


@method_decorator(login_required, name='dispatch')
class Profile(generic.DetailView):
    template_name = 'profiles/index.html'
    model = User


