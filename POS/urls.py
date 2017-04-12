from userModule.views import (login_view, register_view, logout_view, home_view)
from rest_framework_jwt.views import obtain_jwt_token

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^home/',home_view, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),

    #jwt post token code url
    url(r'^api/auth/token/', obtain_jwt_token),
    #usermodule api links
    url(r'^api/users/', include("userModule.api.urls", namespace='users-api')),
]



