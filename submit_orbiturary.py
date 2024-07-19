from django.shortcuts import render, redirect
from .models import Obituary

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST.get('author', '')  # Optional field

        # Create a new obituary object
        obituary = Obituary(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, content=content, author=author)
        obituary.save()

        # Show confirmation message upon successful submission
        return render(request, 'confirmation.html', {'message': 'Obituary submitted successfully!'})

    else:
        return render(request, 'obituary_form.html')
