'''
 ---> Pakka running code <---
import os
from django.shortcuts import render
from django.http import HttpResponse

def s(a):
    with open(a, 'rb') as f:
        f.seek(-2, 2)
        f.tell()
        lb = f.read()
        h = lb.hex()
        if h == "6082":
            return "png"
        elif h == "ffd9":
            return "jpg"
        elif h == "0000":
            return "exe"
        elif h == "460a":
            return "pdf"
        elif h == "4553":
            return "mkv"
        elif h == "0018":
            return "mp4"
        elif h == "aaaa":
            return "mp3"
        else:
            return "none"

def process_uploaded_file(uploaded_file):
    content = uploaded_file.read()
    offset = -1
    file_extension = ""
    
    if uploaded_file.name.endswith('.jpg'):
        offset = content.find(b'\xff\xd9')
        file_extension = 'jpg'
    elif uploaded_file.name.endswith('.png'):
        offset = content.find(b'\x60\x82')
        file_extension = 'png'
    elif uploaded_file.name.endswith('.mp4'):
        offset = content.find(b'\x00\x18')
        file_extension = 'mp4'
    elif uploaded_file.name.endswith('.mp3'):
        offset = content.find(b'\xaa\xaa')
        file_extension = 'mp3'
    elif uploaded_file.name.endswith('.pdf'):
        offset = content.find(b'\x46\x0a')
        file_extension = 'pdf'
    elif uploaded_file.name.endswith('.mkv'):
        offset = content.find(b'\x45\x53')
        file_extension = 'mkv'
    elif uploaded_file.name.endswith('.exe'):
        offset = content.find(b'\x00\x00')
        file_extension = 'exe'
    
    if offset != -1:
        new_filename = f"Processed.{file_extension}"
        with open(new_filename, 'wb') as f:
            f.write(content[offset + 2:])
        return new_filename, file_extension
    return None, None

def upload_file(request):
    if request.method == 'POST' and 'uploaded_file' in request.FILES:
        uploaded_file = request.FILES['uploaded_file']
        processed_filename, file_extension = process_uploaded_file(uploaded_file)

        if processed_filename and file_extension == 'exe':
            #result_message = "Corrupted File and highly vulnerable"
            result_message = f"Processed file: {processed_filename}"
        elif processed_filename:
            #result_message = "Corrupted File and less vulnerable"
            result_message = f"Processed file: {processed_filename}"
        else:
            result_message = "Safe File"

        return render(request, 'file_processing_app/result.html', {'result_message': result_message})

    return render(request, 'file_processing_app/upload.html')

----->  <-----
'''
import os
import random
from django.shortcuts import render
from django.http import HttpResponse

def process_uploaded_file(file):
    content = file.read()
    if file.name.endswith('.jpg'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\xff\xd9':
            return "Safe File"
        elif last_4_bytes != b'\xff\xd9' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
        
    elif file.name.endswith('.png'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\x60\x82':
            return "Safe File"
        elif last_4_bytes != b'\x60\x82' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
    elif file.name.endswith('.mp4'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\x00\x18':
            return "Safe File"
        elif last_4_bytes != b'\x00\x18' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
    elif file.name.endswith('.mp3'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\xaa\xaa':
            return "Safe File"
        elif last_4_bytes != b'\xaa\xaa' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
    elif file.name.endswith('.pdf'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\x46\x0a':
            return "Safe File"
        elif last_4_bytes != b'\x46\x0a' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
    elif file.name.endswith('.mkv'):
        last_4_bytes = content[-2:]
        if last_4_bytes == b'\x45\x53':
            return "Safe File"
        elif last_4_bytes !=b'\x45\x53' and last_4_bytes != b'\x00\x00':
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
    elif file.name.endswith('.exe'):
        last_4_bytes = content[-2:]
        if (last_4_bytes == b'\x00\x00') or (last_4_bytes != b'\x00\x00' and last_4_bytes != b'\x00\x00'):
            return "Corrupted File but not highly vulnerable"
        else:
            return "Corrupted File and highly vulnerable"
        
    return None

def upload_file(request):
    if request.method == 'POST' and 'uploaded_file' in request.FILES:
        uploaded_file = request.FILES['uploaded_file']
        vulnerability_level = process_uploaded_file(uploaded_file)
        result_message = vulnerability_level
        bubble_positions = [{'top': random.randint(0, 100), 'left': random.randint(0, 100)} for _ in range(20)]
        return render(request, 'file_processing_app/result.html', {'result_message': result_message, 'bubble_positions': bubble_positions})
        #return render(request, 'file_processing_app/result.html', {'result_message': result_message})

    return render(request, 'file_processing_app/upload.html')
