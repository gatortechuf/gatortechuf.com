"""
Membership Views
"""
from django.views import generic

from .models import Leader

class MembershipView(generic.ListView):
    """
    Membership Index View
    """
    template_name = 'membership/members.html'
    model = Leader
    context_object_name = 'leader_list'
