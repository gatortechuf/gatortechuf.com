from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProfileEditForm
from .models import UserProfile

@method_decorator(login_required, name='dispatch')
class ProfileList(generic.ListView):
    template_name = 'profiles/list.html'
    model = User
    context_object_name = 'user_list'


@method_decorator(login_required, name='dispatch')
class Profile(generic.DetailView):
    template_name = 'profiles/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['profile_id'] = int(self.kwargs['pk'])
        return context

@method_decorator(login_required, name='dispatch')
class EditProfile(generic.UpdateView):
    template_name = 'profiles/edit.html'
    model = UserProfile
    fields = ('resume', 'phone_number')

    # Checks to see if the user is trying to edit their profile
    def get_context_data(self, **kwargs):
        context = super(EditProfile, self).get_context_data(**kwargs)
        if self.kwargs['pk'] == str(self.request.user.id):
            context['can_access'] = self.kwargs['pk']

        return context

    def get_success_url(self):
        return('/')

    def form_valid(self, form):
        return super(EditProfile, self).form_valid(form)

