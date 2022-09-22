from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList


def show_mywatchlist(request):
    response = {
        'nama': 'Jeremy Alva Prathama',
        'npm': 2106640354,
    }

    return render(request, "mywatchlist.html", response)

# Retrieve all
def retrieve_html(request):
    movie_amount = MyWatchList.objects.count();
    data_watchlist = MyWatchList.objects.all()
    response = {
        'mywatchlist': data_watchlist,
        'is_binge': True if MyWatchList.objects.filter(watched=True).count() >= (movie_amount / 2) else False
    }

    return render(request, "watchlist_html.html", response)

def retrieve_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def retrieve_json(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
