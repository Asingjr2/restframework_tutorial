from django.contrib import admin
from django.urls import path, include

# Creating base routing url to handle url requests, and also allow for login options during api data access
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-login/', include("rest_framework.urls")),
    path("", include("snippets.urls")),
]

