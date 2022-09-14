from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_list_katalog = CatalogItem.objects.all()
    response = {
        'nama': 'Jeremy Alva Prathama',
        'npm': '2106640354',
        'list_katalog': data_list_katalog,
    }
    return render(request, "katalog.html", response)