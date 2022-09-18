from django.urls import path
from mywatchlist.views import show_mywatchlist, retrieve_html, retrieve_html_by_id, retrieve_json, retrieve_json_by_id, retrieve_xml, retrieve_xml_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', retrieve_html, name='retrieve_html'),
    path('xml/', retrieve_xml, name='retrieve_xml'),
    path('json/', retrieve_json, name='retrieve_json'),
    path('html/<int:id>', retrieve_html_by_id, name='retrieve_html_by_id'),
    path('xml/<int:id>', retrieve_xml_by_id, name='retrieve_xml_by_id'),
    path('json/<int:id>', retrieve_json_by_id, name='retrieve_json_by_id'),
]