from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm
from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the middleware index.")


def person(request):
    persons = Person.objects.all()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(person)
    else:
        form = PersonForm

    return render(request, 'middleware/person.html', {'form': form, 'persons': persons})


def person_update(request, person_id):
    p = get_object_or_404(Person, pk=int(person_id))
    persons = Person.objects.all()
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect(person)
    else:
        form = PersonForm(instance=p)

    return render(request, 'middleware/person.html', {'form': form, 'persons': persons})
