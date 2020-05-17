# codesamples-python3-django-file-upload
Python 3 Django File Uploading App in virtualenv

# Description
File Uploading web application in style of Photo Storage

# Purposes
To demonstrate ability to create web application on Python Flask as part of homework to get Python Developer positio

# Requirements
1) Python 3
2) Django 3.0.6
3) virtualenv
4) pip
5) hachoir to get EXIF data from not only jpg files and corrupted EXIF data
6) pillow or PIL to detect if file is image or getting various Image parameters

# Installation instructions (approximate, not the last ones to follow):
1) sudo pip3 install virtualenv
2) git clone
3) virtualenv codesamples-python3-django-file-upload or use exitent one
4) source codesamples-python3-django-file-upload/bin/activate
5) python3 -m pip install Django
6) [optional] python3 -c "import django; print(django.get_version())" to test if version is 3.0.6 and works with Python 3
7) pip install flask hachoir pillow
8) [optional?] copy the file contents from github into codesamples-python3-django-file-upload/ (just near the second folder codesamples-python3-django-file-upload in codesamples-python3-django-file-upload folder), optional if git clone 
9) Overall you structure should be similar to the one in github except for the files created by virtualenv
10) python3 manage.py runserver
11) [optional, done playing?] deactivate
12) [optional] You may also clone the project into you project, but you would need to create your own virtuenv in there or install requirements into your virtual environment Linux OS

# How to run?
1) 127.0.0.1:8000 - main page
2) http://127.0.0.1:8000/readme - detailed instruction on how to use - link shoudl be on main page #Notes
3) Camera Make and Camera Model being displayed only if available in EXIF data otherwise "Not Available" text being displayed
4)Photo Created or Photo Digitized Date being displayed only if available in EXIF data otherwise "Not Available" text being displayed
5)Consider reading detailed instruction available by the link on the main page after you will run the project

# Notes
1) Why hachoir used instead of PIL:
2) Bug on Python 3.6 and PIL with reading EXIF data: https://github.com/python-pillow/Pillow/issues/2944
3) Another similar report - not reading EXIF data in all files: https://github.com/python-pillow/Pillow/issues/518
