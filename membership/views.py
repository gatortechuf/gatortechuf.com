from django.shortcuts import render
from django.views import generic

from .models import Leader, Coordinator

class MembershipView(generic.ListView):
    template_name = 'membership/members.html'
    model = Leader
    context_object_name = 'leader_list'

