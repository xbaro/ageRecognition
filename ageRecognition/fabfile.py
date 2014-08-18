from fabric.api import local, lcd

def deploy():
    with lcd('.'):
        local('git pull .')
        local('python manage.py migrate ageRecognition')
        local('python manage.py test ageRecognition')
        local('killall python')
        local('python manage.py runserver 0.0.0.0:8005 &')
