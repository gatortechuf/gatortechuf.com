from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone

from .models import CheckIn

@login_required
def index(request):
    return render(request, 'attendance/checkin.html')

@login_required
def checkin(request):
    current_time = timezone.now()
    if current_time.date().weekday() == 1 or current_time.date().weekday() == 2:
        recent_check_in = CheckIn.objects.all().filter(user=request.user, checked_in_on__gt=timezone.now() - timedelta(hours=4))
        if recent_check_in:
            context = {"message": "You have already checked in"}
        else:
            instance = CheckIn(user=request.user)
            instance.save()
            context = {"message": "Successfully checked in!"}
    else:
        context = {"message": "There is no meeting right now"}


    return render(request, 'attendance/checkin.html', context)    
