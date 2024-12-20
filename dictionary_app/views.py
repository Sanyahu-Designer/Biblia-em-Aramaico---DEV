from django.shortcuts import render
from .models import AramaicWord

def home(request):
    words = AramaicWord.objects.all().order_by('portuguese_translation')
    context = {
        'words': words
    }
    return render(request, 'dictionary_app/home.html', context)
