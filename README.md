# pos-api-django

Description:
---------------
This project implements django rest with jwt.

It is a typical point of sale api implementation

Installation
----------------
Navigate to project folder
install requirements
----------------
$ pip install -r requirements.text

migrate database
----------------
$python manage.py migrate 

create super user
----------------
$ python manage.py createsuperuser

Then>
----------------
$ python manage.py runserver

open your blowser and paste
List users
-----------------------
http://127.0.0.1:8000/api/users/

Get JWT Authentication token
----------------------------------
http://127.0.0.1:8000/api/auth/token/

register users
---------------------
http://127.0.0.1:8000/api/users/register/

other url routes
--------------------
urlpatterns = [
    url(r'^$', UserListAPIView.as_view(), name='user-list'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^users-details/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', UpdateAPIView.as_view(), name='edit'),
    url(r'^user-delete/(?P<pk>[0-9]+)/$', UserDeleteAPIView.as_view(), name='user-delete'),

    #permissions url patterns
    url(r'^permission-details/(?P<pk>[0-9]+)/$', PermissionDetailAPIView.as_view(), name='permission-detail'),
    url(r'^permissions', PermissionListView.as_view(), name='permissions')

]



