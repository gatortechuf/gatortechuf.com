from django.views import generic
from .models import RecruiterLogo

class RecruiterView(generic.ListView):
    template_name = "recruiters/recruiters.html"
    model = RecruiterLogo
    context_object_name = "logos"
    