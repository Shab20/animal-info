import json
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from .models import Animal, Family


def family(request, family_id):
    # Load the animal data from the JSON file
    with open('animals.json') as f:
        data = json.load(f)
    
    # Filter the list of animals to include only those in the given family
    animals = [a for a in data['animals'] if a['family'] == family_id]

    print(animals)  # Debugging statement
    
    # Get the family object with the given ID
    try:
        family = next(f for f in data['families'] if f['id'] == family_id)
    except StopIteration:
        raise Http404
    
    # Render the template with the list of animals and the family name
    return render(request, 'family_detail.html', {'animals': animals, 'family_name': family['name']})
    

def animal(request, animal_id):
    # Load the animal data from the JSON file
    with open('animals.json') as f:
        data = json.load(f)
    
    # Get the animal object with the given ID
    try:
        animal = next(a for a in data['animals'] if a['id'] == animal_id)
    except StopIteration:
        raise Http404
    
    print(animal)  # Debugging statement
    
    # Render the template with the animal data
    return render(request, 'animal_detail.html', {'animal': animal})
