from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # POST with {"username":"…","password":"…"} => {"token":"…"}
    path("login/", obtain_auth_token, name="api-login"),
]
