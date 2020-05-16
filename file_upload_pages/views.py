from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
def fileUploadForm(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    args = {}


    return render(request, 'index.html', {'form': form, 'args': args})

def readme(request):
    return render(request, 'instructions.html', {})
    
def error404(request, exception):
    return render(request, '404.html', status=404)

def error413(request, exception):
    return render(request, '413.html', status=413)
