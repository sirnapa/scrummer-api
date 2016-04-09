from fabric.api import *

env.user = 'produccion'
env.hosts = ['192.168.1.10']

def prepare_deployment_with_tag(tag_name):
    local('python manage.py test scrummer')
    local('git add -p && git commit')
    local('git checkout master && git merge develop')
    local('git tag "' + tag_name + '"')
    local('git checkout develop')

from fabric.api import lcd

def deploy():
    run("mkdir hola")

    '''
<<<<<<< HEAD
>>>>>>> develop
    with lcd('/path/to/my/prod/area/'):
=======
    with lcd('/path/to/my/prod/area/'): 
>>>>>>> develop
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
    '''