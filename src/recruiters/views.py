"""
Recruiter Views
"""
from django.views import generic
from .models import RecruiterHeader, SponsorshipLevel, RecruiterLogo

class RecruiterView(generic.TemplateView):
    """
    Recruiter Index View
    """
    template_name = 'recruiters/recruiters.html'

    def get_context_data(self, **kwargs):
        context = super(RecruiterView, self).get_context_data(**kwargs)
        context['header'] = RecruiterHeader.objects.latest('updated_at')
        context['levels'] = SponsorshipLevel.objects.order_by('price')[:3]
        context['logos'] = RecruiterLogo.objects.all()
        return context
