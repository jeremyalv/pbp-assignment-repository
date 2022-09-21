from django.urls import path
from mywatchlist.views import show_mywatchlist, retrieve_html, retrieve_json, retrieve_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', retrieve_html, name='retrieve_html'),
    path('xml/', retrieve_xml, name='retrieve_xml'),
    path('json/', retrieve_json, name='retrieve_json'),
]