from django.shortcuts import render, redirect
from django.conf import settings
from .forms import FileUploadForm
from .models import UploadedFile

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FileUploadForm()
    return render(request, 'upload/file_upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload/success.html')
