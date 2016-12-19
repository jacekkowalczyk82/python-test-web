# web app with diango

## setup django 

https://docs.djangoproject.com/en/1.10/intro/install/

sudo apt-get -y install python-pip
sudo pip install virtualenv
cd ~/
virtualenv virt-env-django

cd virt-env-django/
source bin/activate
#inside virtualenv 

pip install Django

python 
Python 2.7.6 (default, Jun 22 2015, 18:00:18) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
1.10.2
>>> exit ()

python -m django --version

## create web app with django 

cd Dropbox/programowanie/python/python-code/
django-admin startproject my_django_website
cd my_django_website/
python manage.py runserver 0.0.0.0:8000
python manage.py startapp mybacklog

vim mybacklog/views.py
vim my_django_website/urls.py

python manage.py runserver 0.0.0.0:8000
http://localhost:8000/mybacklog/

python manage.py migrate


##getting data from jira 
curl -D- --insecure --config ~/curl_kowalczy_config -X GET -H "Content-Type: application/json" -o out.json https://jira.tomtomgroup.com/rest/api/2/search?jql=assignee=kowalczy
python -mjson.tool out.json

curl -D- --insecure --config ~/curl_kowalczy_config -X GET -H "Content-Type: application/json" -o out.json 'https://jira.tomtomgroup.com/rest/api/2/search?jql=assignee=kowalczy&fields=id,key,self,summary'

curl -D- --insecure --config ~/curl_kowalczy_config -X GET -H "Content-Type: application/json" -o out.json 'https://jira.tomtomgroup.com/rest/api/2/search?jql=assignee=kowalczy%20AND%20project=ATF&fields=id,key,self,summary'

( = %28
) = %29 
space = %20 

curl -D- --insecure --config ~/curl_kowalczy_config -X GET -H "Content-Type: application/json" -o out.json 'https://jira.tomtomgroup.com/rest/api/2/search?jql=assignee=kowalczy%20AND%20%28project=ATF%20OR%20project=NAVAPP%29&fields=id,key,self,summary'
 


 
resource = Resource(url + '/rest/api/2/issue/%s' % key, pool_instance=None, filters=[auth])
response = resource.get(headers = {'Content-Type' : 'application/json'})
    if response.status_int == 200:
        # Not all resources will return 200 on success. There are other success status codes. Like 204. We've read
        # the documentation though and know what to expect here.
        issue = json.loads(response.body_string())
        return issue
		
		


