from django.shortcuts import render
from .models import Obituary

def view_obituaries(request):
    # Retrieve all obituaries (or implement pagination here)
    obituaries = Obituary.objects.all().order_by('-submission_date')  # Order by most recent first

    context = {'obituaries': obituaries}
    return render(request, 'obituaries.html', context)
