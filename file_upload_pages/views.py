from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import newFile, responseInterpreter, imageList, deletePhoto
from os.path import splitext

# Create your views here.
def fileUploadForm(request):
    form = UploadFileForm()
    args = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.POST)
        
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            if request.FILES and "file" in request.FILES and request.FILES["file"]:
                imageFile = request.FILES["file"]
                imageFileName = request.POST["fileName"] if request.POST["fileName"] else splitext(request.FILES['file'].name)[0]
                imageFileExtension = splitext(request.FILES['file'].name)[1]
                imageFileName = imageFileName + imageFileExtension
                newImageObject = newFile(imageFile, imageFileName)
                responseCode = newImageObject.checkAndUpload()
                del newImageObject
                responseInterpreterInstance = responseInterpreter(responseCode)
                args["responseMessage"] = responseInterpreterInstance.getResponseMessage()
                del responseInterpreterInstance
            #return HttpResponseRedirect('')

    imageListInsance = imageList()
    imagesList = imageListInsance.getList()
    
    if "errorCode" in imagesList[0] and imagesList[0]["errorCode"] == 3:
        responseInterpreterInstance = responseInterpreter(imagesList[0]["errorCode"])
        imagesList[0]["errorMessage"] = responseInterpreterInstance.getResponseMessage()
        del responseInterpreterInstance
    args["imagesList"] = imagesList
    print(args["imagesList"])
    return render(request, 'index.html', {'form': form, 'args': args})

def readme(request):
    return render(request, 'instructions.html', {})
    
def error404(request, exception):
    return render(request, '404.html', status=404)

def error413(request, exception):
    return render(request, '413.html', status=413)
