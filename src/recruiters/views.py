"""
Recruiter Views
"""
from django.views import generic
from .models import RecruiterHeader, SponsorshipLevels, RecruiterLogo

class RecruiterView(generic.TemplateView):
    """
    Recruiter Index View
    """
    template_name = 'recruiters/recruiters.html'
    #model = RecruiterLogo
    #context_object_name = 'logos'

    def get_context_data(self, **kwargs):
        context = super(RecruiterView, self).get_context_data(**kwargs)
        context['header'] = RecruiterHeader.objects.latest('updated_at')
        context['levels'] = SponsorshipLevels.objects.order_by('-price')[:3]
        context['logos'] = RecruiterLogo.objects.all()
        return context
