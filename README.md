#Create Enviroment
python -m venv env

#Activate enviroment
env|scripts\activate

#install django
pip install django

#Start project
django-admin startproject project_name

#change folder
cd project_name

#create django app
python manage.py startapp app_name

#run project
pyhton manage.py runserver
