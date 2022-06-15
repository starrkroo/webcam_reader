from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('test_stream', generate_video, name='test_stream'),
    path('stored_data', stored_data, name='stored_data')
]