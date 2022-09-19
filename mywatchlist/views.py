from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.template.loader import render_to_string
from mywatchlist.models import MyWatchList


def show_mywatchlist(request):
    response = {
        'nama': 'Jeremy Alva Prathama',
        'npm': 2106640354,
    }

    return render(request, "mywatchlist.html", response)

# Retrieve all
def retrieve_html(request):
    data_watchlist = MyWatchList.objects.all()
    response = {
        'mywatchlist': data_watchlist,
    }

    return render(request, "watchlist_html.html", response)

def retrieve_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def retrieve_json(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Retrieve by id
def retrieve_html_by_id(request, id):
    data_watchlist = MyWatchList.objects.filter(pk=id)

    response = {
        'mywatchlist': data_watchlist,
    }

    return render(request, "watchlist_html.html", response)

def retrieve_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def retrieve_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


