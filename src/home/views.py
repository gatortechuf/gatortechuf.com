"""
Homepage Views
"""
from django.views import generic

from .models import HomePageHeader, HomePageButton, TextBlurb, SemesterModule

class HomePageView(generic.TemplateView):
    """
    Homepage Index
    """
    template_name = 'home/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['header'] = HomePageHeader.objects.latest('updated_at')
        context['buttons'] = HomePageButton.objects.all()
        context['blurbs'] = TextBlurb.objects.all()
        context['modules'] = SemesterModule.objects.all()
        return context