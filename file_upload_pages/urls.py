from django.urls import path

from .views import fileUploadForm, readme, error404

urlpatterns = [
    path('', fileUploadForm, name='file_upload'),
    path('readme', readme, name='readme')
]

handler404 = error404
