from django.shortcuts import render
from .models import AramaicWord
from django.core.paginator import Paginator

def home(request):
    words_list = AramaicWord.objects.all().order_by('portuguese_translation')
    paginator = Paginator(words_list, 20)  # Show 20 words per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'words': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'dictionary_app/home.html', context)
