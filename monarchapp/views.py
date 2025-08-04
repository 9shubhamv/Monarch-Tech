from django.shortcuts import render
import os
import subprocess
from django.http import JsonResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT_DIR = os.path.join(BASE_DIR, 'txt_files')

# Create your views here.
def index(request):
    files = [
        file for file in os.listdir(TXT_DIR)
        if file.endswith('.txt')
    ]
    return render(request, 'index.html', {'files': files})

def openfile(request):
    filename = request.GET.get('filename')
    if not filename:
        return JsonResponse({'status': "error", 'message': "Missing filename"}, status=400)
    file_path = os.path.join(TXT_DIR,filename)

    if os.path.exists(file_path):
        subprocess.Popen(['notepad.exe', file_path])
        return JsonResponse({'status':"found"})
    else:
        # return JsonResponse({'status':"not found",
        # "gdrive_link": "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
        # })
        return JsonResponse({
            'status': "not found",
            'gdrive_link': "https://drive.google.com/drive/folders/1p5uwsFLMiq7BfDbA_JDxUQM1sCo7wXI4"
        })
    